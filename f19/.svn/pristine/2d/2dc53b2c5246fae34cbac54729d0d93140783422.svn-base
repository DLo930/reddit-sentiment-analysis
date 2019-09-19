
// A fast VM written by Carsten Varming
// If compiled with -DDEBUG instruction dispatch is implemented by a switch statement,
// otherwise we use computed gotos. We have to ignore -pedantic to get GCC's computed gotos.

#define _POSIX_C_SOURCE 200809L
#define _GNU_SOURCE


#include <assert.h>
#include <limits.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

#include "lib/xalloc.h"
#include "lib/contracts.h"

#include "include/bare.h"
#include "c0vm.h"
#include "c0vm_c0ffi.h"

#include <sys/mman.h>
#include <errno.h>
#include <string.h>

#ifndef DEBUG
//#define DEBUG
#endif

#ifdef DEBUG

#define NEXT break
#define INST(I) case I
typedef ubyte inst_t;
#define GET_INST(I) I
#define GET_PC(i) pc[i]

#else

#define NEXT goto **pc++
#define INST(I) inst_##I
typedef void * inst_t; 
#define GET_INST(I) &&inst_##I
#define GET_PC(i) (uintptr_t) pc[i]

// ISO C forbids computed gotos, but the jumps to a switch statement slows us down.
#pragma GCC diagnostic ignored "-pedantic"

static int arity[256] = {
  // Every opcode not mentioned has arity 0.
  [NEWARRAY] = 1,
  [NEW] = 1,
  [AADDF] = 1,
  [VLOAD] = 1,
  [VSTORE] = 1,
  [BIPUSH] = 1,
  [ILDC] = 2,
  [ALDC] = 2,
  [IF_CMPEQ] = 2,
  [IF_CMPNE] = 2,
  [IF_ICMPLT] = 2,
  [IF_ICMPGE] = 2,
  [IF_ICMPGT] = 2,
  [IF_ICMPLE] = 2,
  [GOTO] = 2,
  [INVOKESTATIC] = 2,
  [INVOKENATIVE] = 2
};

#endif

#ifndef UNSAFE
/* functions for handling errors */
static void c0_memory_error(char *err) {
    fprintf(stderr, "Memory error: %s\n", err);
    raise(SIGUSR1);
    //raise(SIGSEGV);
    //kill(getpid(), SIGSEGV);
}

static void c0_division_error(char *err) {
    fprintf(stderr, "Division error: %s\n", err);
    raise(SIGUSR2);
    //raise(SIGFPE);
    //kill(getpid(), SIGFPE);
}

#else

static void c0_memory_error(char *err) {
  (void) err;
  return;
}

static void c0_division_error(char *err) {
  (void) err;
  return;
}

#endif

static unsigned long numofpages;
static ssize_t pagesize;
static ubyte *stack_top;
static struct sigaction org_sa;

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

#ifndef DEBUG
static void copy_args(inst_t *t, ubyte *b, size_t i) {
  while (i-- > 0)
  {
    *t++ = (inst_t) (uintptr_t) *b++;
  }
  return;
}
#endif // DEBUG

static ssize_t max(ssize_t a, ssize_t b)
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
  // Convert bytecodes to labels

  inst_t inst_table[256] = {
    [IADD]         = GET_INST(IADD),
    [IAND]         = GET_INST(IAND),
    [IDIV]         = GET_INST(IDIV),
    [IMUL]         = GET_INST(IMUL),
    [IOR]          = GET_INST(IOR),
    [IREM]         = GET_INST(IREM),
    [ISHL]         = GET_INST(ISHL),
    [ISHR]         = GET_INST(ISHR),
    [ISUB]         = GET_INST(ISUB),
    [IXOR]         = GET_INST(IXOR),
    [DUP]          = GET_INST(DUP),
    [POP]          = GET_INST(POP),
    [SWAP]         = GET_INST(SWAP),
    [NEWARRAY]     = GET_INST(NEWARRAY),
    [ARRAYLENGTH]  = GET_INST(ARRAYLENGTH),
    [NEW]          = GET_INST(NEW),
    [AADDF]        = GET_INST(AADDF),
    [AADDS]        = GET_INST(AADDS),
    [IMLOAD]       = GET_INST(IMLOAD),
    [AMLOAD]       = GET_INST(AMLOAD),
    [IMSTORE]      = GET_INST(IMSTORE),
    [AMSTORE]      = GET_INST(AMSTORE),
    [CMLOAD]       = GET_INST(CMLOAD),
    [CMSTORE]      = GET_INST(CMSTORE),
    [VLOAD]        = GET_INST(VLOAD),
    [VSTORE]       = GET_INST(VSTORE),
    [ACONST_NULL]  = GET_INST(ACONST_NULL),
    [BIPUSH]       = GET_INST(BIPUSH),
    [ILDC]         = GET_INST(ILDC),
    [ALDC]         = GET_INST(ALDC),
    [NOP]          = GET_INST(NOP),
    [IF_CMPEQ]     = GET_INST(IF_CMPEQ),
    [IF_CMPNE]     = GET_INST(IF_CMPNE),
    [IF_ICMPLT]    = GET_INST(IF_ICMPLT),
    [IF_ICMPGE]    = GET_INST(IF_ICMPGE),
    [IF_ICMPGT]    = GET_INST(IF_ICMPGT),
    [IF_ICMPLE]    = GET_INST(IF_ICMPLE),
    [GOTO]         = GET_INST(GOTO),
    [INVOKESTATIC] = GET_INST(INVOKESTATIC),
    [INVOKENATIVE] = GET_INST(INVOKENATIVE),
    [RETURN]       = GET_INST(RETURN) };

  for (size_t i = 0; i < bc0->function_count; i++)
  {
    struct function_info *fn = bc0->function_pool+i;
    max_arg_var_diff = max(fn->num_vars - fn->num_args, max_arg_var_diff);
    size_t length = fn->code_length;
    function_table[i] = xmalloc(length * sizeof(inst_t));
    for (size_t j = 0; j < length; )
    {
      ubyte op = fn->code[j];
      inst_t op_label = inst_table[op];
      if (op_label == NULL) 
      { 
        fprintf(stderr, "invalid opcode: 0x%02x in function %zu instruction %zu\n", op, i, j);
        abort();
      }
      function_table[i][j++] = op_label;
      copy_args(function_table[i]+j, fn->code+j, arity[op]);
      j+=arity[op];
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
  if (stack_top == MAP_FAILED)
    c0_memory_error("Unable to allocate initial stack, mmap failed");
  numofpages = 2;
  // istack is now a pointer to the last page of the stack
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
  if (sigaction(SIGSEGV, &sa, &org_sa) == -1)
    c0_memory_error("stack segment handler issue");

#define pop(S) *++S
#define push(S,V) *S-- = V

  // main with -d expects a char pointer on the stack
  push(S,"Program start");

#define IEXIT 0xFF

  // Initial program. Call main and exit successfully.
  register inst_t * pc = xcalloc(20, sizeof(inst_t));
  pc[0] = GET_INST(NOP);
  pc[1] = GET_INST(NOP);
  pc[2] = GET_INST(INVOKESTATIC);
  pc[5] = GET_INST(IEXIT);
  pc[6] = GET_INST(NOP);
  pc[7] = GET_INST(NOP);

  inst_t *original_pc = pc;

#ifdef DEBUG
  while (true) {

    //printf("Executing opcode %x at %p --- \n", *pc, pc);

    switch (*pc++) {

#else
   {
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

#define BINOP(T0,T1,TEST,OP) { T0 y = INT(pop(S)); T1 x = INT(pop(S));\
                               if (TEST) c0_division_error("Division Exception");\
                               push(S,VAL(x OP y));\
                               NEXT; }

      INST(IADD): BINOP(uint32_t, uint32_t, false, +)

      INST(ISUB): BINOP(uint32_t, uint32_t, false, -)

      INST(IMUL): BINOP(uint32_t, uint32_t, false, *)

      INST(IDIV): BINOP(int32_t, int32_t, y == 0 || (y == -1 && x == INT32_MIN), /)

      INST(IREM): BINOP(int32_t, int32_t, y == 0 || (y == -1 && x == INT32_MIN), %)

      INST(IAND): BINOP(uint32_t, uint32_t, false, &)

      INST(IOR):  BINOP(uint32_t, uint32_t, false, |)

      INST(IXOR): BINOP(uint32_t, uint32_t, false, ^)

      INST(ISHL):
      {
        uint32_t y = INT(pop(S));
        uint32_t x = INT(pop(S));
        uint32_t res = x << (y & 0x1F);
        push(S, VAL(res));
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
        int32_t b = (byte) GET_PC(0);
        pc++;
        push(S,VAL((uint32_t) b));
        NEXT;
      }

      /* Returning from a function */

      INST(RETURN):
      {
        // Layout assumption of stack B[0],..., B[- ..] are the local variables.
        // S[1] is the return value, S[2] is the caller pc, and S[3] is the caller base.
        c0_value v = pop(S);
        void * B2 = (c0_value *) pop(S);
        pc = (inst_t *) pop(S);
        S = B;
        B = B2;
        push(S,v);
        NEXT;
      }

      /* Operations on local variables */

      INST(VLOAD):
      {
        uint8_t i = GET_PC(0);
        pc++;
        push(S,*(B-i));
        NEXT;
      }

      INST(VSTORE):
      {
        uint8_t i = GET_PC(0);
        *(B-i) = pop(S);
        pc++;
        NEXT;
      }

      INST(ACONST_NULL):
      {
        push(S, NULL);
        NEXT;
      }

#define GET16_PC (uint16_t) GET_PC(0) << 8 | (uint16_t) GET_PC(1)

      INST(ILDC):
      {
        uint16_t c = GET16_PC;
        pc+=2;
        ASSERT(c < bc0->int_pool_count);
        push(S, VAL((uint32_t) bc0->int_pool[c]));
        NEXT;
      }

      INST(ALDC):
      {
        uint16_t c = GET16_PC;
        pc+=2;
        ASSERT(c < bc0->string_pool_count);
        push(S, &(bc0->string_pool[c]));
        NEXT;
      }


      /* Control flow operations */

      INST(NOP):
      {
        NEXT;
      }

#define JMP(OP) { int16_t c = GET16_PC;\
                  pc+=2;\
                  c0_value v2 = pop(S);\
                  c0_value v1 = pop(S);\
                  if (v1 OP v2) {pc -= 3; pc += c;}\
                  NEXT; }

      INST(IF_CMPEQ): JMP(==)

      INST(IF_CMPNE): JMP(!=)

#define JMPI(OP) { int16_t c = GET16_PC;\
                   pc+=2;\
                   int32_t v2 = INT(pop(S));\
                   int32_t v1 = INT(pop(S));\
                   if (v1 OP v2) { pc -= 3; pc += c;}\
                   NEXT; }

      INST(IF_ICMPLT): JMPI(<)

      INST(IF_ICMPGE): JMPI(>=)

      INST(IF_ICMPGT): JMPI(>)

      INST(IF_ICMPLE): JMPI(<=)

      INST(GOTO):
      {
        int16_t c = GET16_PC;
        pc -= 1;
        pc += c;
        NEXT;
      }


      /* Function call operations: */

      INST(INVOKESTATIC):
      {
        // Stack layout assumption
        // (S+num_args)[0], ..., S+num_args[- (num_args - 1)] are the arguments v0,...,vnum_args-1
        uint16_t c = GET16_PC;
        ASSERT(c < bc0->function_count);
        struct function_info *fn = bc0->function_pool+c;
        ASSERT(fn->num_vars >= fn->num_args);
        size_t d = fn->num_vars - fn->num_args;
        // Add num_vars - num_args to the stack.
        S = S - d;
        // (S+num_vars)[0], ... , S+num_vars[- (num_vars - 1)] are the local variables
        void ** B2 = S + fn->num_vars;
        // B2[0], ... , B2[- (num_vars - 1)] are the local variables
        push(S,pc+2);
        push(S,B);
        // B2[0], ... , B2[- (num_vars - 1)], pc, B, S[0]
        B = B2;
        pc = function_table[c];
        NEXT;
        // The stack layout:
        // B -> v0,...vn, caller pc, caller B, S[0]; B[-i] is local variable i
      }

      INST(INVOKENATIVE):
      {
        uint16_t c = GET16_PC;
        pc+=2;
        ASSERT(c <= bc0->native_count);
        struct native_info *fn = bc0->native_pool+c;
        c0_value (*g)(c0_value *) = native_function_table[fn->function_table_index];
        ASSERT(g != NULL);
        // The stack growns down so the arguments are in the wrong order
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
        size_t s = GET_PC(0);
        pc++;
        // Allocate NULL initialized memory.
        c0_value v = xcalloc(1, s);
        push(S,v);
        NEXT;
      }

      INST(NEWARRAY):
      {
        size_t s = GET_PC(0);
        pc++;
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
        size_t f = GET_PC(0);
        pc++;
        ubyte *v = pop(S);
        if (v == NULL) c0_memory_error("NULL pointer exception AADDF");
        push(S, v+f);
        NEXT;
      }

      INST(AADDS):
      {
        int32_t i = INT(pop(S));
        c0_array *a = ((c0_array *) pop(S));
        //ubyte *b = (ubyte *) (a+1);
        ASSERT(a != NULL);
        if (i < 0 || i >= a->count) c0_memory_error("Array out-of-bounds AADDS");
        push(S, a->elems + a->elt_size * i);
        NEXT;
      }

#define XLOAD(T,M,C) { T *a = pop(S); if (a == NULL) c0_memory_error(M); push(S,C(*a)); NEXT; }

      INST(IMLOAD):  XLOAD(uint32_t, "NULL pointer dereference IMLOAD", VAL)

#define XSTORE(T,M,C) { T x = C(pop(S)); T *a = pop(S); if (a == NULL) c0_memory_error(M); *a = x; NEXT; }
      INST(IMSTORE): XSTORE(uint32_t, "NULL pointer dereference IMSTORE", INT)

      INST(AMLOAD):  XLOAD(c0_value, "NULL pointer dereference AMLOAD", )

      INST(AMSTORE): XSTORE(c0_value, "NULL pointer dereference AMSTORE", )

      INST(CMLOAD):  XLOAD(ubyte, "NULL pointer dereference CMLOAD", VAL)

      INST(CMSTORE): XSTORE(ubyte, "NULL pointer dereference CMSTORE", INT)

      INST(IEXIT):
      {
        int v = INT(pop(S));
        struct sigaction mysa;
        if (sigaction(SIGSEGV, &org_sa, &mysa)) 
          c0_memory_error("exit; sigaction disable error");
#ifndef DEBUG
        for (size_t i = 0; i < bc0->function_count; i++) free(function_table[i]);
#endif
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

