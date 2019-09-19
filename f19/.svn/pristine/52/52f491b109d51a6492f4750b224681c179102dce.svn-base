
#define _POSIX_C_SOURCE 200809L
#define _GNU_SOURCE


#include <assert.h>
#include <limits.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

#include "lib/xalloc.h"
#include "lib/contracts.h"
#include "lib/stacks.h"

#include "include/bare.h"
#include "c0vm.h"
#include "c0vm_c0ffi.h"

#include <sys/mman.h>
#include <errno.h>
#include <string.h>

#define DEBUG

#ifdef DEBUG

#define NEXT break
#define INST(I) case I
typedef ubyte inst_t;
#define GET_INST(I) I
#define GET_PC *pc++

#else

#define NEXT goto **pc++
#define INST(I) inst_##I
typedef void * inst_t; 
#define GET_INST(I) &&inst_##I
#define GET_PC (uintptr_t) *pc++

#pragma GCC diagnostic ignored "-pedantic"

#endif

/* call stack frames */
typedef struct frame * frame;
struct frame {
    c0_value *V; /* local variables */
    stack S;     /* operand stack */
    ubyte *P;    /* function body */
    size_t pc;      /* return address */
};

/* functions for handling errors */
void c0_memory_error(char *err) {
    fprintf(stderr, "Memory error: %s\n", err);
    raise(SIGUSR1);
    //raise(SIGSEGV);
}

void c0_division_error(char *err) {
    fprintf(stderr, "Division error: %s\n", err);
    raise(SIGUSR2);
    //raise(SIGFPE);
}

unsigned long numofpages;
ssize_t pagesize;
ubyte *stack_top;
struct sigaction org_sa;

static void stack_handler(int sigx, struct siginfo *si, void *unused)
{
  struct sigaction mysa;
  (void) unused;
  (void) sigx;
  if (sigaction(SIGSEGV, &org_sa, &mysa)) 
    c0_memory_error("stack allocation error; sigaction disable");
  if (si->si_addr >= (void *) stack_top && 
      si->si_addr <= (void *) (stack_top + pagesize))
  {
    stack_top = mmap(stack_top - pagesize, pagesize, PROT_NONE, 
                     MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (stack_top == MAP_FAILED) c0_memory_error("Unable to expand stack");
    numofpages++;
    if (mprotect(stack_top + pagesize, pagesize, PROT_READ|PROT_WRITE)) 
      c0_memory_error("Unable to obtain read / write on stack");
    if (sigaction(SIGSEGV, &mysa, &org_sa)) 
      c0_memory_error("sigaction enb stack allocation error");
    return;
  }
  else raise(SIGSEGV);
  return;
}

void copy_args(inst_t *t, ubyte *b, size_t i) {
  while (i-- > 0)
  {
    *t++ = (inst_t) (uintptr_t) *b++;
  }
  return;
}

ssize_t max(ssize_t a, ssize_t b)
{
  return a < b ? b : a;
}

/* TODO: implement execute function */
int execute(struct bc0_file *bc0) {

  pagesize = sysconf(_SC_PAGESIZE);
  if (pagesize == -1) c0_memory_error("Unable to get _SC_PAGESIZE");

  inst_t **function_table = xmalloc(sizeof(inst_t *) * bc0->function_count);

  ssize_t max_arg_var_diff = 0;

#ifdef DEBUG
  for (size_t i = 0; i < bc0->function_count; i++)
  {
    struct function_info *fn = bc0->function_pool+i;
    function_table[i] = fn->code;
    max_arg_var_diff = max(fn->num_vars - fn->num_args, max_arg_var_diff);
  }

#else
  // Convert bytecode to sequences of labels

  // Copies the instructions
#define COPYI(I,J,K) function_table[I][J] = &&inst_##K; J++;
  // Copies the arguments embedding in instructions. It would be nice with a general arity array.
#define COPYA(I,J,C) copy_args(function_table[I]+J, fn->code+J, C); J+=C; break;

  for (size_t i = 0; i < bc0->function_count; i++)
  {
    struct function_info *fn = bc0->function_pool+i;
    max_arg_var_diff = max(fn->num_vars - fn->num_args, max_arg_var_diff);
    size_t length = fn->code_length;
    function_table[i] = xmalloc(length * sizeof(inst_t));
    for (size_t j = 0; j < length; )
    {
      switch (fn->code[j]) {
        case IADD: { COPYI(i,j,IADD); COPYA(i,j,0); }
        case IAND: { COPYI(i,j,IAND); COPYA(i,j,0); }
        case IDIV: { COPYI(i,j,IDIV); COPYA(i,j,0); }
        case IMUL: { COPYI(i,j,IMUL); COPYA(i,j,0); }
        case IOR:  { COPYI(i,j,IOR);  COPYA(i,j,0); }
        case IREM: { COPYI(i,j,IREM); COPYA(i,j,0); }
        case ISHL: { COPYI(i,j,ISHL); COPYA(i,j,0); }
        case ISHR: { COPYI(i,j,ISHR); COPYA(i,j,0); }
        case ISUB: { COPYI(i,j,ISUB); COPYA(i,j,0); }
        case IXOR: { COPYI(i,j,IXOR); COPYA(i,j,0); }

        case DUP:  { COPYI(i,j,DUP);  COPYA(i,j,0); }
        case POP:  { COPYI(i,j,POP);  COPYA(i,j,0); }
        case SWAP: { COPYI(i,j,SWAP); COPYA(i,j,0); }

        case NEWARRAY:    { COPYI(i,j,NEWARRAY);    COPYA(i,j,1); }
        case ARRAYLENGTH: { COPYI(i,j,ARRAYLENGTH); COPYA(i,j,0); }
        case NEW:         { COPYI(i,j,NEW);         COPYA(i,j,1); }

        case AADDF:   { COPYI(i,j,AADDF);   COPYA(i,j,1); }
        case AADDS:   { COPYI(i,j,AADDS);   COPYA(i,j,0); }
        case IMLOAD:  { COPYI(i,j,IMLOAD);  COPYA(i,j,0); }
        case AMLOAD:  { COPYI(i,j,AMLOAD);  COPYA(i,j,0); }
        case IMSTORE: { COPYI(i,j,IMSTORE); COPYA(i,j,0); }
        case AMSTORE: { COPYI(i,j,AMSTORE); COPYA(i,j,0); }
        case CMLOAD:  { COPYI(i,j,CMLOAD);  COPYA(i,j,0); }
        case CMSTORE: { COPYI(i,j,CMSTORE); COPYA(i,j,0); }

        case VLOAD:  { COPYI(i,j,VLOAD);  COPYA(i,j,1); }
        case VSTORE: { COPYI(i,j,VSTORE); COPYA(i,j,1); }

        case ACONST_NULL: { COPYI(i,j,ACONST_NULL); COPYA(i,j,0); }
        case BIPUSH:      { COPYI(i,j,BIPUSH);      COPYA(i,j,1); }
        case ILDC:        { COPYI(i,j,ILDC);        COPYA(i,j,2); }
        case ALDC:        { COPYI(i,j,ALDC);        COPYA(i,j,2); }

        case IF_CMPEQ:  { COPYI(i,j,IF_CMPEQ);  COPYA(i,j,2); }
        case IF_CMPNE:  { COPYI(i,j,IF_CMPNE);  COPYA(i,j,2); }
        case IF_ICMPLT: { COPYI(i,j,IF_ICMPLT); COPYA(i,j,2); }
        case IF_ICMPGE: { COPYI(i,j,IF_ICMPGE); COPYA(i,j,2); }
        case IF_ICMPGT: { COPYI(i,j,IF_ICMPGT); COPYA(i,j,2); }
        case IF_ICMPLE: { COPYI(i,j,IF_ICMPLE); COPYA(i,j,2); }
        case NOP:       { COPYI(i,j,NOP);       COPYA(i,j,0); }
        case GOTO:      { COPYI(i,j,GOTO);      COPYA(i,j,2); }

        case INVOKESTATIC: { COPYI(i,j,INVOKESTATIC); COPYA(i,j,2); }
        case INVOKENATIVE: { COPYI(i,j,INVOKENATIVE); COPYA(i,j,2); }
        case RETURN:       { COPYI(i,j,RETURN);       COPYA(i,j,0); }

        default: { fprintf(stderr, "invalid opcode: 0x%02x\n", fn->code[j]); abort(); }
      }
    }
  }

#endif

  max_arg_var_diff += 3;
  max_arg_var_diff *= sizeof(c0_value);
  if (max_arg_var_diff > (INT32_MAX >> 2)) 
    c0_memory_error("Unable to allocate stack. max_arg_var_diff too big");
  // Make sure that our pagesize is so big that a function call 
  // cannot jump over a page without writing to it.
  while (max_arg_var_diff > pagesize) pagesize <<= 1;

  // Minimum 64k pagesize
  if (pagesize < (1 << 16)) pagesize = 1 << 16;

  uintptr_t pagemask = ~(pagesize - 1);

  struct sigaction sa;
  ubyte * istack;
  // On 64 bit machines put our stack in the virtual address space 32GB below the host stack
  if (sizeof(void *) >= 8) 
     istack =  ((ubyte *) &sa) - ((size_t) (32) * (size_t) (0x40000000));
  // On 32 bit machine  put it 128 MB below the host stack
  else 
     istack = ((ubyte *) &sa) - 0x8000000;
  istack = (ubyte *) ((uintptr_t) istack & pagemask);
  // Allocate two pages for the stack
  stack_top = mmap(istack, 2*pagesize, PROT_READ | PROT_WRITE, 
                   MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
  if (stack_top == MAP_FAILED) c0_memory_error("Unable to allocate initial stack, mmap failed");
  numofpages = 2;
  // istack is now a pointer to the last page of the stack
//  istack = stack_top + 2 * pagesize;
  // Protect the bottom page of the stack.
  // The SIGSEGV stack_handler will increase the stack when needed
  if (mprotect(stack_top, pagesize, PROT_NONE)) 
    c0_memory_error("Unable to protect end of stack");

  // Stack pointer. Grows down, *S and below is free
  register c0_value * S = (c0_value *) (((byte *) stack_top) + 2*pagesize - sizeof(c0_value));

  register c0_value * B = S;
  sa.sa_flags = SA_SIGINFO;
  sigemptyset(&sa.sa_mask);
  sa.sa_sigaction = stack_handler;
  if (sigaction(SIGSEGV, &sa, &org_sa) == -1) c0_memory_error("stack segment handler issue");

#define pop(S) *++S
#define push(S,V) *S-- = V

  push(S,"Program start");

#define IEXIT 0xFF

  // Initial program. Call main and exit successfully.
  register inst_t * pc = xcalloc(20, sizeof(inst_t));
  pc[0] = GET_INST(NOP);
  pc[1] = GET_INST(NOP);
  pc[2] = GET_INST(INVOKESTATIC);
  pc[5] = GET_INST(IEXIT);

  inst_t *original_pc = pc;

  while (true) {

#ifdef DEBUG
    //printf("Executing opcode %x at %p --- \n", *pc, pc);

    switch (*pc++) {

#else
    NEXT;
#endif

        /* GENERAL INSTRUCTIONS: Implement the following cases for each of the
           possible bytecodes.  Read the instructions in the assignment to see
           how far you should go before you test your code at each stage.  Do
           not try to write all of the code below at once!  Remember to update
           the program counter (pc) for each case, depending on the number of
           bytes needed for each bytecode operation.  See PROG_HINTS.txt for
           a few more hints.

           IMPORTANT NOTE: For each case, the case should end with a break
           statement to prevent the execution from continuing on into the
           next case.  See the POP case for an example.  To introduce new
           local variables in a case, use curly braces to create a new block.
           See the DUP case for an example.

           See C_IDIOMS.txt for further information on idioms you may find
           useful.
        */

      /* Additional stack operation: */

      INST(POP): {
        (void) pop(S);
        NEXT;
      }

      INST(DUP): {
        c0_value v = pop(S);
        push(S, v);
        push(S, v);
        NEXT;
      }

      INST(SWAP): {
        c0_value v0 = pop(S);
        c0_value v1 = pop(S);
        push(S,v0);
        push(S,v1);
        NEXT;
      }


       /* Arithmetic and Logical operations */

      INST(IADD):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        push(S, VAL(x+y));
        NEXT;
      }

      INST(ISUB):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        push(S, VAL(x-y));
        NEXT;
      }

      INST(IMUL):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        push(S, VAL(x*y));
        NEXT;
      }

      INST(IDIV):
      {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (y == 0 || (y == -1 && x == INT32_MIN)) c0_division_error("Division exception");
        uint32_t res = (uint32_t) (x/y);
        push(S, VAL(res));
        NEXT;
      }

      INST(IREM):
      {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (y == 0 || (y == -1 && x == INT32_MIN)) c0_division_error("Division exception");
        uint32_t res = (uint32_t) (x%y);
        push(S, VAL(res));
        NEXT;
      }

      INST(IAND):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        push(S, VAL(x & y));
        NEXT;
      }

      INST(IOR):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        push(S, VAL(x | y));
        NEXT;
      }

      INST(IXOR):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        push(S, VAL(x ^ y));
        NEXT;
      }

      INST(ISHL):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        push(S, VAL(x << (y & 0x1F)));
        NEXT;
      }

      INST(ISHR):
      {
        uint32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        uint32_t res = x >> (y & 0x1F);
        push(S, VAL(res));
        NEXT;
      }


      /* Pushing small constants */

      INST(BIPUSH):
      {
        int32_t b = (byte) GET_PC;
        push(S,VAL((uint32_t) b));
        NEXT;
      }

      /* Returning from a function */

      INST(RETURN):
      {
        c0_value v = pop(S);
        S = B;
        B = (c0_value *) pop(S);
        pc = (inst_t *) pop(S);
        (void) pop(S);
        push(S,v);
        NEXT;
      }

      /* Operations on local variables */

      INST(VLOAD):
      {
        ssize_t i = (ubyte) GET_PC;
        push(S,B[-i]);
        NEXT;
      }

      INST(VSTORE):
      {
        ssize_t i = (ubyte) GET_PC;
        B[-i] = pop(S);
        NEXT;
      }

      INST(ACONST_NULL):
      {
        push(S, NULL);
        NEXT;
      }

      INST(ILDC):
      {
        size_t c1 = GET_PC;
        size_t c2 = GET_PC;
        size_t c = (c1 << 8) | c2;
        ASSERT(c < bc0->int_pool_count);
        push(S, VAL((uint32_t) bc0->int_pool[c]));
        NEXT;
      }

      INST(ALDC):
      {
        size_t c1 = GET_PC;
        size_t c2 = GET_PC;
        size_t c = (c1 << 8) | c2;
        ASSERT(c < bc0->string_pool_count);
        push(S, &(bc0->string_pool[c]));
        NEXT;
      }


      /* Control flow operations */

      INST(NOP):
      {
        NEXT;
      }

      INST(IF_CMPEQ):
      {
        int32_t c1 = (byte) GET_PC;
        uint32_t c2 = GET_PC;
        int32_t c = (c1 << 8) | c2;
        c0_value v2 = pop(S);
        c0_value v1 = pop(S);
        if (v1 == v2) pc += c-3;
        NEXT;
      }

      INST(IF_CMPNE):
      {
        int32_t c1 = (byte) GET_PC;
        uint32_t c2 = GET_PC;
        int32_t c = (c1 << 8) | c2;
        c0_value v2 = pop(S);
        c0_value v1 = pop(S);
        if (v1 != v2) pc += c-3;
        NEXT;
      }
      INST(IF_ICMPLT):
      {
        int32_t c1 = (byte) GET_PC;
        uint32_t c2 = GET_PC;
        int32_t c = (c1 << 8) | c2;
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x < y) pc += c-3;
        NEXT;
      }

      INST(IF_ICMPGE):
      {
        int32_t c1 = (byte) GET_PC;
        uint32_t c2 = GET_PC;
        int32_t c = (c1 << 8) | c2;
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x >= y) pc += c-3;
        NEXT;
      }

      INST(IF_ICMPGT):
      {
        int32_t c1 = (byte) GET_PC;
        uint32_t c2 = GET_PC;
        int32_t c = (c1 << 8) | c2;
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x > y) pc += c-3;
        NEXT;
      }

      INST(IF_ICMPLE):
      {
        int32_t c1 = (byte) GET_PC;
        uint32_t c2 = GET_PC;
        int32_t c = (c1 << 8) | c2;
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x <= y) pc += c-3;
        NEXT;
      }

      INST(GOTO):
      {
        int32_t c1 = (byte) GET_PC;
        uint32_t c2 = GET_PC;
        int32_t c = (c1 << 8) | c2;
        pc += c-3;
        NEXT;
      }


      /* Function call operations: */

      INST(INVOKESTATIC):
      {
        size_t c1 = GET_PC;
        size_t c2 = GET_PC;
        size_t c = (c1 << 8) | c2;
        ASSERT(c < bc0->function_count);
        struct function_info *fn = bc0->function_pool+c;
        ASSERT(fn->num_vars >= fn->num_args);
        size_t d = fn->num_vars - fn->num_args;
        S = S - 3 - d;
        void ** B2 = S + fn->num_vars;
        for (size_t i = 0; i++ < fn->num_args; ) S[d + i] = S[d + i + 3]; 
        B2[3] = (c0_value) 0x0;
        B2[2] = (c0_value) pc;
        B2[1] = (c0_value) B;
        B = B2;
        //P = function_table[c];
        pc = function_table[c];
        NEXT;
      }

      INST(INVOKENATIVE):
      {
        size_t c1 = GET_PC;
        size_t c2 = GET_PC;
        size_t c = (c1 << 8) | c2;
        ASSERT(c < bc0->native_count);
        struct native_info *fn = bc0->native_pool+c;
        c0_value (*g)(c0_value *) = native_function_table[fn->function_table_index];
        ASSERT(g != NULL);
        for (size_t i = 0; i < fn->num_args/2; i++)
        {
          c0_value tmp = S[fn->num_args - i];
          S[fn->num_args - i] = S[1+i];
          S[1+i] = tmp;
        }
        c0_value v = (*g)(S + 1);
        S += fn->num_args;
        push(S,v);
        NEXT;
      }


      /* Memory allocation operations: */

      INST(NEW):
      {
        size_t s = GET_PC;
        // Allocate NULL initialized memory.
        c0_value v = xcalloc(1, s);
        push(S,v);
        NEXT;
      }

      INST(NEWARRAY):
      {
        size_t s = GET_PC;
        int32_t n = INT(pop(S));
        // Allocate NULL initialized array.
        if (n < 0) c0_memory_error("allocation must have non-negative size ");
        struct c0_array *a = xcalloc(n * s + sizeof(struct c0_array), 1);
        a->count = n;
        a->elt_size = s;
        push(S, (c0_value) a);
        NEXT;
      }

      INST(ARRAYLENGTH):
      {
        c0_array *a = pop(S);
        push(S, VAL(a->count));
        NEXT;
      }


      /* Memory access operations: */

      INST(AADDF):
      {
        size_t f = GET_PC;
        ubyte *v = pop(S);
        if (v == NULL) c0_memory_error("NULL pointer exception AADDF");
        push(S, VAL(v+f));
        NEXT;
      }

      INST(AADDS):
      {
        int32_t i = INT(pop(S));
        c0_array *a = ((c0_array *) pop(S));
        ubyte *b = (ubyte *) (a+1);
        ASSERT(a != NULL);
        if (i < 0 || i >= a->count) c0_memory_error("Array out-of-bounds AADDS");
        push(S, VAL(b + a->elt_size * i));
        NEXT;
      }

      INST(IMLOAD):
      {
        uint32_t *a = pop(S);
        if (a == NULL) c0_memory_error("NULL pointer dereference IMLOAD");
        uint32_t res = *a;
        push(S, VAL(res));
        NEXT;
      }

      INST(IMSTORE):
      {
        uint32_t x = INT(pop(S));
        uint32_t *a = pop(S);
        if (a == NULL) c0_memory_error("NULL pointer dereference IMSTORE");
        *a = x;
        NEXT;
      }

      INST(AMLOAD):
      {
        c0_value *a = pop(S);
        if (a == NULL) c0_memory_error("NULL pointer dereference AMLOAD");
        push(S, *a);
        NEXT;
      }

      INST(AMSTORE):
      {
        c0_value b = pop(S);
        c0_value *a = pop(S);
        if (a == NULL) c0_memory_error("NULL pointer dereference AMSTORE");
        *a = b;
        NEXT;
      }

      INST(CMLOAD):
      {
        byte *a = pop(S);
        if (a == NULL) c0_memory_error("NULL pointer dereference CMLOAD");
        uint32_t x = *a;
        push(S,VAL(x));
        NEXT;
      }

      INST(CMSTORE):
      {
        uint32_t x = INT(pop(S));
        byte *a = pop(S);
        if (a == NULL) c0_memory_error("NULL pointer dereference CMSTORE");
        *a = (byte) (x & 0x7F);
        NEXT;
      }

      INST(IEXIT):
      {
        int v = INT(pop(S));
        struct sigaction mysa;
        if (sigaction(SIGSEGV, &org_sa, &mysa)) 
          c0_memory_error("exit; sigaction disable error");
        free(function_table);
        free(original_pc);
        if (munmap(stack_top, numofpages * pagesize) != 0) 
        {
          int err = errno;
          char *errmsg = strerror(err);
          c0_memory_error(errmsg);
        }
        return v;
      }

#ifdef DEBUG
      default:
        fprintf(stderr, "invalid opcode: 0x%02x\n", *(pc-1));
        abort();
    }
#endif
  }

  /* cannot get here from infinite loop */
  assert(false);
}

