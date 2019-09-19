#include <assert.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

#include "lib/xalloc.h"
#include "lib/stack.h"
#include "lib/contracts.h"
#include "lib/c0v_stack.h"
#include "lib/c0vm.h"
#include "lib/c0vm_c0ffi.h"
#include "lib/c0vm_abort.h"

/* call stack frames */
typedef struct frame_info frame;
struct frame_info {
  c0v_stack_t S; /* Operand stack of C0 values */
  ubyte *P;      /* Function body */
  size_t pc;     /* Program counter */
  c0_value *V;   /* The local variables */
};

int execute(struct bc0_file *bc0) {
  (void) bc0;

  /* Variables */
  c0v_stack_t S = c0v_stack_new();
  ubyte *P = bc0->function_pool[0].code;
  size_t pc = 0;
  c0_value *V = xcalloc(bc0->function_pool[0].num_vars, sizeof(c0_value));
  (void) V;

  /* The call stack, a generic stack that should contain pointers to frames */
  /* You won't need this until you implement functions. */
  gstack_t callStack = stack_new(); 

  while (true) {
    
#ifdef DEBUG
    /* You can add extra debugging information here */
    fprintf(stderr, "Opcode %x -- Stack size: %zu -- PC: %zu\n",
            P[pc], c0v_stack_size(S), pc);
#endif
    
    switch (P[pc++]) {
      
    /* Additional stack operation: */

    case POP: {
      c0v_pop(S);
      break;
    }

    case DUP: {
      c0_value v = c0v_pop(S);
      c0v_push(S,v);
      c0v_push(S,v);
      break;
    }
      
    case SWAP:  {
      c0_value v0 = c0v_pop(S);
      c0_value v1 = c0v_pop(S);
      c0v_push(S,v0);
      c0v_push(S,v1);
      break;
    }

    /* Returning from a function.
     * This currently has a memory leak! It will need to be revised
     * when you write INVOKESTATIC. */

    case RETURN: {
      c0_value retval = c0v_pop(S);
      assert(c0v_stack_empty(S));
      
      if (stack_empty(callStack)) {
        int x = val2int(retval);
#ifdef DEBUG
        fprintf(stderr, "Returning %d from execute()\n", x);
#endif
        c0v_stack_free(S);
        free(V);
        stack_free(callStack, NULL);
        return x;
      }

      c0v_stack_free(S);
      free(V);
      frame *f = pop(callStack);
      S = f->S;
      V = f->V;
      P = f->P;
      pc = f->pc;
      free(f);
      c0v_push(S,retval);
      break;
    }

    /* Arithmetic and Logical operations */

    case IADD: {
      uint32_t y = val2int(c0v_pop(S));
      uint32_t x = val2int(c0v_pop(S));
      c0v_push(S, int2val(x+y));
      break;
    }

    case ISUB: {
      uint32_t y = val2int(c0v_pop(S));
      uint32_t x = val2int(c0v_pop(S));
      c0v_push(S, int2val(x-y));
      break;
    }

    case IMUL: {
      uint32_t y = val2int(c0v_pop(S));
      uint32_t x = val2int(c0v_pop(S));
      c0v_push(S, int2val(x*y));
      break;
    }

    case IDIV: {
      int32_t y = val2int(c0v_pop(S));
      int32_t x = val2int(c0v_pop(S));
      if (y == 0 || (y == -1 && x == INT32_MIN)) c0_arith_error("Division exception");
      uint32_t res = (uint32_t) (x/y);
      c0v_push(S, int2val(res));
      break;
    }

    case IREM: {
      int32_t y = val2int(c0v_pop(S));
      int32_t x = val2int(c0v_pop(S));
      if (y == 0 || (y == -1 && x == INT32_MIN)) c0_arith_error("Division exception");
      uint32_t res = (uint32_t) (x%y);
      c0v_push(S, int2val(res));
      break;
    }

    case IAND: {
      uint32_t y = val2int(c0v_pop(S));
      uint32_t x = val2int(c0v_pop(S));
      c0v_push(S, int2val(x & y));
      break;
    }

    case IOR: {
      uint32_t y = val2int(c0v_pop(S));
      uint32_t x = val2int(c0v_pop(S));
      c0v_push(S, int2val(x | y));
      break;
    }

    case IXOR: {
      uint32_t y = val2int(c0v_pop(S));
      uint32_t x = val2int(c0v_pop(S));
      c0v_push(S, int2val(x ^ y));
      break;
    }

    case ISHL: {
      uint32_t y = val2int(c0v_pop(S));
      uint32_t x = val2int(c0v_pop(S));
      if (y >= 32) c0_arith_error("Shift right operation");
      c0v_push(S, int2val(x << y));
      break;
    }

    case ISHR: {
      uint32_t y = val2int(c0v_pop(S));
      int32_t x = val2int(c0v_pop(S));
      if (y >= 32) c0_arith_error("Shift right operation");
      uint32_t res = x >> y;
      c0v_push(S, int2val(res));
      break;
    }      
      
    /* Pushing constants */

    case BIPUSH: {
      int32_t b = (byte)P[pc++];
      c0v_push(S, int2val(b));
      break;
    }

    case ILDC: {
      size_t c1 = P[pc++];
      size_t c2 = P[pc++];
      size_t c = (c1 << 8) | c2;
      ASSERT(c < bc0->int_count);
      c0v_push(S, int2val(bc0->int_pool[c]));
      break;
    }
      
    case ALDC: {
      size_t c1 = P[pc++];
      size_t c2 = P[pc++];
      size_t c = (c1 << 8) | c2;
      ASSERT(c < bc0->string_count);
      c0v_push(S, ptr2val(&(bc0->string_pool[c])));
      break;
    }      

    case ACONST_NULL: {
      c0v_push(S, ptr2val(NULL));
      break;
    }


    /* Operations on local variables */

    case VLOAD: {
      size_t i = P[pc++];
      c0v_push(S,V[i]);
      break;
    }
      
    case VSTORE: {
      size_t i = P[pc++];
      V[i] = c0v_pop(S);
      break;
    }
      
      
    /* Control flow operations */

    case NOP: { break; }

    case IF_CMPEQ: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 = P[pc++];
      int32_t c = (c1 << 8) | c2;
      c0_value v2 = c0v_pop(S);
      c0_value v1 = c0v_pop(S);
      if (val_equal(v1, v2)) pc += c-3;
      break;
    }
      
    case IF_CMPNE: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 = P[pc++];
      int32_t c = (c1 << 8) | c2;
      c0_value v2 = c0v_pop(S);
      c0_value v1 = c0v_pop(S);
      if (!val_equal(v1, v2)) pc += c-3;
      break;
    }
      
    case IF_ICMPLT: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 = P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = val2int(c0v_pop(S));
      int32_t x = val2int(c0v_pop(S));
      if (x < y) pc += c-3;
      break;
    }
      
    case IF_ICMPGE: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 =  P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = val2int(c0v_pop(S));
      int32_t x = val2int(c0v_pop(S));
      if (x >= y) pc += c-3;
      break;
    }
      
    case IF_ICMPGT: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 =  P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = val2int(c0v_pop(S));
      int32_t x = val2int(c0v_pop(S));
      if (x > y) pc += c-3;
      break;
    }
      
    case IF_ICMPLE: {
      int32_t c1 = (byte) P[pc++];
      uint32_t c2 =  P[pc++];
      int32_t c = (c1 << 8) | c2;
      int32_t y = val2int(c0v_pop(S));
      int32_t x = val2int(c0v_pop(S));
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
      c0_value a = c0v_pop(S);
      c0_user_error(val2ptr(a));
      break;
    }

    case ASSERT: {
      c0_value a = c0v_pop(S);
      int32_t x = val2int(c0v_pop(S));
      if (x == 0) c0_assertion_failure(val2ptr(a));
      break;
    }


    /* Function call operations: */

    case INVOKESTATIC: {
      size_t c1 =  P[pc++];
      size_t c2 = P[pc++];
      size_t c = (c1 << 8) | c2;
      ASSERT(c < bc0->function_count);
      frame *f = xmalloc(sizeof(frame));
      f->V = V;
      f->S = S;
      f->P = P;
      f->pc = pc;
      push(callStack, f);
      struct function_info *fn = bc0->function_pool+c;
      V = xmalloc(sizeof(c0_value)*fn->num_vars);
      for (size_t i = fn->num_args; 0 < i--; ) V[i] = c0v_pop(S);
      S = c0v_stack_new();
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
      for (size_t i = fn->num_args; 0 < i--; ) { 
        c0_value x = c0v_pop(S);
        //fprintf(stderr, " -- input %p, \n", x);
        args[i] = x;
      }
      c0_value v = (*g)(args);
      //fprintf(stderr, " -- output %p, \n", v);
      free(args);
      c0v_push(S,v);
      break;
    }


    /* Memory allocation operations: */

    case NEW: {
      size_t s = P[pc++];
      // Allocate NULL initialized memory.
      c0_value v = ptr2val(xcalloc(1, s));
      c0v_push(S,v);
      break;
    }

    case NEWARRAY: {
      size_t s = P[pc++];
      int32_t n = val2int(c0v_pop(S));
      // Allocate NULL initialized array.
      if (n < 0) c0_memory_error("allocation must have non-negative size ");
      c0_array *a = xmalloc(sizeof(c0_array));
      a->count = n;
      a->elt_size = s;
      if (n == 0) { a->elems = NULL; }
      else { a->elems = xcalloc(n, s); }
      c0v_push(S, ptr2val(a));
      break;
    }

    case ARRAYLENGTH: {
      c0_array *a = val2ptr(c0v_pop(S));
      c0v_push(S, int2val(a->count));
      break;
    }


    /* Memory access operations: */

    case AADDF: {
      size_t f = P[pc++];
      ubyte *v = val2ptr(c0v_pop(S));
      if (v == NULL) c0_memory_error("NULL pointer exception");
      c0v_push(S, ptr2val(v+f));
      break;
    }

    case AADDS: {
      int32_t i = val2int(c0v_pop(S));
      c0_array *a = ((c0_array*) val2ptr(c0v_pop(S)));
      if (a == NULL) c0_memory_error("Array out-of-bounds");
      char *elems = a->elems;
      if (i < 0 || i >= a->count) c0_memory_error("Array out-of-bounds");
      c0v_push(S, ptr2val(&elems[a->elt_size * i]));
      break;
    }

    case IMLOAD: {
      uint32_t *a = val2ptr(c0v_pop(S));
      if (a == NULL) c0_memory_error("NULL pointer dereference IMLOAD");
      uint32_t res = *a;
      c0v_push(S, int2val(res));
      break;
    }

    case IMSTORE: {
      uint32_t x = val2int(c0v_pop(S));
      uint32_t *a = val2ptr(c0v_pop(S));
      if (a == NULL) c0_memory_error("NULL pointer dereference IMSTORE");
      *a = x;
      break;
    }

    case AMLOAD: {
      void **a = val2ptr(c0v_pop(S));
      if (a == NULL) c0_memory_error("NULL pointer dereference AMLOAD");
      c0v_push(S, ptr2val(*a));
      break;
    }
      
    case AMSTORE: {
      void *b = val2ptr(c0v_pop(S));
      void **a = val2ptr(c0v_pop(S));
      if (a == NULL) c0_memory_error("NULL pointer dereference AMSTORE");
      *a = b;
      break;
    }
      
    case CMLOAD: {
      byte *a = val2ptr(c0v_pop(S));
      if (a == NULL) c0_memory_error("NULL pointer dereference CMLOAD");
      uint32_t x = *a;
      c0v_push(S, int2val(x));
      break;
    }

    case CMSTORE: {
      uint32_t x = val2int(c0v_pop(S));
      byte *a = val2ptr(c0v_pop(S));
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

