#include <assert.h>
#include <limits.h>
#include <stdlib.h>

#include "lib/xalloc.h"
#include "lib/contracts.h"
#include "lib/stacks.h"

#include "include/bare.h"
#include "c0vm.h"
#include "c0vm_c0ffi.h"
#include "c0vm_abort.h"

/* call stack frames */
typedef struct frame * frame;
struct frame {
  c0_value *V; /* local variables */
  stack S;     /* operand stack */
  ubyte *P;    /* function body */
  size_t pc;   /* return address */
};

/* TODO: implement execute function */
int execute(struct bc0_file *bc0) {
  
  /* Variables used for bytecode interpreter. You will need to initialize
     these appropriately. */
  
  /* callStack to hold frames when functions are called */
  stack callStack = stack_new();
  /* initial program is the "main" function, function 0 (which must exist) */
  struct function_info *main_fn = bc0->function_pool;
  /* array to hold local variables for function */
  c0_value *V = xmalloc(sizeof(c0_value) * main_fn->num_vars);
  /* stack for operands for computations */
  stack S = stack_new();
  /* array of (unsigned) bytes that make up the program */
  ubyte *P = main_fn->code;
  /* program counter that holds "address" of next bytecode to interpret from
     program P */
  size_t pc = 0;
  
  while (true) {
    
#ifdef DEBUG
    printf("Opcode %x -- Operand stack size: %zu -- Program counter: %zu\n",
           P[pc], stack_size(S), pc);
#endif
    
    switch (P[pc++]) {
      
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

    case POP: {
      pop(S);
      break;
    }

    case DUP: {
      c0_value v = pop(S);
      push(S,v);
      push(S,v);
      break;
    }

    case SWAP: {
      c0_value v0 = pop(S);
      c0_value v1 = pop(S);
      push(S,v0);
      push(S,v1);
      break;
    }
      
     /* Arithmetic and Logical operations */

    case IADD: {
      uint32_t y = INT(pop(S));
      uint32_t x = INT(pop(S));
      push(S, VAL(x+y));
      break;
    }

    case ISUB: {
      uint32_t y = INT(pop(S));
      uint32_t x = INT(pop(S));
      push(S, VAL(x-y));
      break;
    }

    case IMUL: {
      uint32_t y = INT(pop(S));
      uint32_t x = INT(pop(S));
      push(S, VAL(x*y));
      break;
    }

    case IDIV: {
      int32_t y = INT(pop(S));
      int32_t x = INT(pop(S));
      if (y == 0 || (y == -1 && x == INT32_MIN)) c0_arith_error("Division exception");
      uint32_t res = (uint32_t) (x/y);
      push(S, VAL(res));
      break;
    }

    case IREM: {
      int32_t y = INT(pop(S));
      int32_t x = INT(pop(S));
      if (y == 0 || (y == -1 && x == INT32_MIN)) c0_arith_error("Division exception");
      uint32_t res = (uint32_t) (x%y);
      push(S, VAL(res));
      break;
    }

    case IAND: {
      uint32_t y = INT(pop(S));
      uint32_t x = INT(pop(S));
      push(S, VAL(x & y));
      break;
    }

    case IOR: {
      uint32_t y = INT(pop(S));
      uint32_t x = INT(pop(S));
      push(S, VAL(x | y));
      break;
    }

    case IXOR: {
      uint32_t y = INT(pop(S));
      uint32_t x = INT(pop(S));
      push(S, VAL(x ^ y));
      break;
    }

    case ISHL: {
      uint32_t y = INT(pop(S));
      uint32_t x = INT(pop(S));
      if (y >= 32) c0_arith_error("Shift right operation");
      push(S, VAL(x << y));
      break;
    }

    case ISHR: {
      uint32_t y = INT(pop(S));
      int32_t x = INT(pop(S));
      if (y >= 32) c0_arith_error("Shift right operation");
      uint32_t res = x >> y;
      push(S, VAL(res));
      break;
    }

    /* Pushing small constants */

    case BIPUSH: {
      int32_t b = (byte) P[pc++];
      push(S,VAL((uint32_t) b));
      break;
    }

    /* Returning from a function */

    case RETURN: {
      c0_value v = pop(S);
      if (stack_empty(callStack)) {
        stack_free(callStack, NULL);
        stack_free(S, NULL);
        free(V);
        return INT(v);
      }
      stack_free(S, NULL);
      free(V);
      frame f = pop(callStack);
      S = f->S;
      V = f->V;
      P = f->P;
      pc = f->pc;
      free(f);
      push(S,v);
      break;
    }

    /* Operations on local variables */

    case VLOAD: {
      size_t i = P[pc++];
      push(S,V[i]);
      break;
    }
      
    case VSTORE: {
      size_t i = P[pc++];
      V[i] = pop(S);
      break;
    }
      
    case ACONST_NULL: {
      push(S, NULL);
      break;
    }
      
    case ILDC: {
      size_t c1 = P[pc++];
      size_t c2 = P[pc++];
      size_t c = (c1 << 8) | c2;
      ASSERT(c < bc0->int_pool_count);
      push(S, VAL((uint32_t) bc0->int_pool[c]));
      break;
    }
      
    case ALDC: {
      size_t c1 = P[pc++];
      size_t c2 = P[pc++];
      size_t c = (c1 << 8) | c2;
      ASSERT(c < bc0->string_pool_count);
      push(S, &(bc0->string_pool[c]));
      break;
    }
      
    /* Control flow operations */

    case NOP: {
      break;
    }
      
    case IF_CMPEQ: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 = P[pc++];
      int32_t c = (c1 << 8) | c2;
      c0_value v2 = pop(S);
      c0_value v1 = pop(S);
      if (v1 == v2) pc += c-3;
      break;
    }
      
    case IF_CMPNE: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 = P[pc++];
      int32_t c = (c1 << 8) | c2;
      c0_value v2 = pop(S);
      c0_value v1 = pop(S);
      if (v1 != v2) pc += c-3;
      break;
    }
      
    case IF_ICMPLT: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 = P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = INT(pop(S));
      int32_t x = INT(pop(S));
      if (x < y) pc += c-3;
      break;
    }
      
    case IF_ICMPGE: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 =  P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = INT(pop(S));
      int32_t x = INT(pop(S));
      if (x >= y) pc += c-3;
      break;
    }
      
    case IF_ICMPGT: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 =  P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = INT(pop(S));
      int32_t x = INT(pop(S));
      if (x > y) pc += c-3;
      break;
    }
      
    case IF_ICMPLE: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 =  P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = INT(pop(S));
      int32_t x = INT(pop(S));
      if (x <= y) pc += c-3;
      break;
    }
      
    case GOTO: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 = P[pc++];
      int32_t c = (c1 << 8) | c2;
      pc += c-3;
      break;
    }
      
    case ATHROW: {
      c0_value a = pop(S);
      c0_user_error(a);
      break;
    }

    case ASSERT: {
      c0_value a = pop(S);
      int32_t x = INT(pop(S));
      if (x == 0) c0_assertion_failure(a);
      break;
    }

    /* Function call operations: */

    case INVOKESTATIC: {
      size_t c1 = P[pc++];
      size_t c2 = P[pc++];
      size_t c = (c1 << 8) | c2;
      ASSERT(c < bc0->function_count);
      frame f = xmalloc(sizeof(struct frame));
      f->V = V;
      f->S = S;
      f->P = P;
      f->pc = pc;
      push(callStack, f);
      struct function_info *fn = bc0->function_pool+c;
      V = xmalloc(sizeof(c0_value)*fn->num_vars);
      for (size_t i = fn->num_args; 0 < i--; ) V[i] = pop(S);
      S = stack_new();
      P = fn->code;
      pc = 0;
      break;
    }
      
    case INVOKENATIVE: {
      size_t c1 = P[pc++];
      size_t c2 = P[pc++];
      size_t c = (c1 << 8) | c2;
      ASSERT(c < bc0->native_count);
      struct native_info *fn = bc0->native_pool+c;
      c0_value (*g)(c0_value *) = native_function_table[fn->function_table_index];
      ASSERT(g != NULL);
      c0_value *args = xmalloc(sizeof(c0_value) * fn->num_args);
      for (size_t i = fn->num_args; 0 < i--; ) args[i] = pop(S);
      c0_value v = (*g)(args);
      free(args);
      push(S,v);
      break;
    }
      

    /* Memory allocation operations: */

    case NEW: {
      size_t s = P[pc++];
      // Allocate NULL initialized memory.
      c0_value v = xcalloc(1, s);
      push(S,v);
      break;
    }

    case NEWARRAY: {
      size_t s = P[pc++];
      int32_t n = INT(pop(S));
      // Allocate NULL initialized array.
      if (n < 0) c0_memory_error("allocation must have non-negative size ");
      struct c0_array *a = xcalloc(n * s + sizeof(struct c0_array), 1);
      a->count = n;
      a->elt_size = s;
      push(S, (c0_value) a);
      break;
    }

    case ARRAYLENGTH: {
      c0_array *a = pop(S);
      push(S, VAL(a->count));
      break;
    }


    /* Memory access operations: */

    case AADDF: {
      size_t f = P[pc++];
      ubyte *v = pop(S);
      if (v == NULL) c0_memory_error("NULL pointer exception");
      push(S, v+f);
      break;
    }

    case AADDS: {
      int32_t i = INT(pop(S));
      c0_array *a = ((c0_array *) pop(S));
      ubyte *b = (ubyte *) (a+1);
      ASSERT(a != NULL);
      if (i < 0 || i >= a->count) c0_memory_error("Array out-of-bounds");
      push(S, b + a->elt_size * i);
      break;
    }

    case IMLOAD: {
      uint32_t *a = pop(S);
      if (a == NULL) c0_memory_error("NULL pointer dereference IMLOAD");
      uint32_t res = *a;
      push(S, VAL(res));
      break;
    }

    case IMSTORE: {
      uint32_t x = INT(pop(S));
      uint32_t *a = pop(S);
      if (a == NULL) c0_memory_error("NULL pointer dereference IMSTORE");
      *a = x;
      break;
    }

    case AMLOAD: {
      c0_value *a = pop(S);
      if (a == NULL) c0_memory_error("NULL pointer dereference AMLOAD");
      push(S, *a);
      break;
    }
      
    case AMSTORE: {
      c0_value b = pop(S);
      c0_value *a = pop(S);
      if (a == NULL) c0_memory_error("NULL pointer dereference AMSTORE");
      *a = b;
      break;
    }
      
    case CMLOAD: {
      byte *a = pop(S);
      if (a == NULL) c0_memory_error("NULL pointer dereference CMLOAD");
      uint32_t x = *a;
      push(S,VAL(x));
      break;
    }

    case CMSTORE: {
      uint32_t x = INT(pop(S));
      byte *a = pop(S);
      if (a == NULL) c0_memory_error("NULL pointer dereference CMSTORE");
      *a = (byte) (x & 0x7F);
      break;
    }
      
    default:
      fprintf(stderr, "invalid opcode: 0x%02x\n", P[pc]);
      abort();
    }
  }
  
  /* cannot get here from infinite loop */
  assert(false);
}

