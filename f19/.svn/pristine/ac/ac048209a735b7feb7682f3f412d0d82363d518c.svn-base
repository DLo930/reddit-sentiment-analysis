/*****************************************************************************
 * Sample solution for VM Lab
 * Penny Anderson
 * June 2013
 * It would be good to rationalize the types then system test
 ******************************************************************************/
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

#define MIN_INT 0x80000000 // smallest c0 integer

/* call stack frames */
typedef struct frame * frame;
struct frame {
  c0_value *V; /* local variables */
  size_t num_vars; /*  number of local variables */
  stack S;     /* operand stack */
  ubyte *P;    /* function body */
  size_t pc;   /* return address */
};

size_t uoffset16(ubyte *P, size_t pc) {
  size_t result = (size_t)(P[pc]);
  result = (result << 8) | (P[pc+1]);
  return result;
}

int32_t offset16(ubyte *P, size_t pc) {
  int32_t result = (int32_t)(int8_t)(P[pc]); // signed high-order byte
  result = (result << 8) | (P[pc+1]); // unsigned low-order byte
  return result;
}

int execute(struct bc0_file *bc0) {
  
  /* callStack to hold frames when functions are called */
  stack callStack = stack_new();

  /* initial program is the "main" function, function 0 (which must exist) */
  struct function_info *main_fn = bc0->function_pool;

  /* array to hold local variables for function */
  c0_value *V = xcalloc(main_fn->num_vars, sizeof(c0_value));
  size_t V_size = main_fn->num_vars;
  /* stack for operands for computations */
  stack S = stack_new();
  /* array of (unsigned) bytes that make up the program */
  ubyte *P = main_fn->code;
  /* program counter that holds "address" of next bytecode to interpret from
     program P */
  size_t pc = 0;
  
  while (true) {
    switch (P[pc]) {
      
      /*  stack operations: */

      /*
       * 0x57 pop           S, v -> S
       */
    case POP: {
      pc++;
      ASSERT( ! stack_empty(S) );
      pop(S);

      break;
    }

      /*
       * 0x59 dup           S, v -> S, v, v
       */
    case DUP: {
      pc++;
      ASSERT( ! stack_empty(S) );
      c0_value v = pop(S);
      push(S,v);
      push(S,v);

      break;
    }
      
      /*
       * 0x5F swap          S, v1, v2 -> S, v2, v1
       */
    case SWAP: {
      pc++;
      ASSERT( ! stack_empty(S) );
      c0_value v1 = pop(S);
      ASSERT( ! stack_empty(S) );
      c0_value v2 = pop(S);
      push(S, v1);
      push(S, v2);

      break;
    }

     /* Arithmetic and Logical operations */

      /*
       * 0x60 iadd         S, x:w32, y:w32 -> S, x+y:w32
       */
    case IADD: {
      pc++;
      ASSERT( ! stack_empty(S) );
      uint32_t y = (uint32_t)(INT(pop(S)));
      ASSERT( ! stack_empty(S) );
      uint32_t x = (uint32_t)(INT(pop(S)));
      push(S, VAL((int32_t) (x+y)));
      
      break;
    }
      /*
       * 0x64 isub         S, x:w32, y:w32 -> S, x-y:w32
       */
    case ISUB: {
      pc++;
      ASSERT( ! stack_empty(S) );
      uint32_t y = (uint32_t)(INT(pop(S)));
      ASSERT( ! stack_empty(S) );
      uint32_t x = (uint32_t)(INT(pop(S)));
      push(S, VAL((int32_t) (x-y)));
      
      break;
    }
      /*
       * 0x68 imul         S, x:w32, y:w32 -> S, x*y:w32
       */
    case IMUL: {
      pc++;
      ASSERT( ! stack_empty(S) );
      uint32_t y = (uint32_t)(INT(pop(S)));
      ASSERT( ! stack_empty(S) );
      uint32_t x = (uint32_t)(INT(pop(S)));
      push(S, VAL((int32_t) (x*y)));
      
      break;
    }
      /*
       * 0x6C idiv         S, x:w32, y:w32 -> S, x/y:w32
       */
    case IDIV:  {
      pc++;
      ASSERT( ! stack_empty(S) );
      int32_t y = INT(pop(S));
      ASSERT( ! stack_empty(S) );
      int32_t x = INT(pop(S));
      if ( y == 0 ) {
	c0_arith_error("Error: division by zero.");
      }
      else if ( y == -1 &&  x == (int32_t) MIN_INT ) {
	c0_arith_error("Error: division causes overflow.");
      }
      else {
	push(S, VAL(x/y));
      }

      break;
    }
      /*
       * 0x70 irem         S, x:w32, y:w32 -> S, x%y:w32
       */
    case IREM: {
      pc++;
      ASSERT( ! stack_empty(S) );
      int32_t y = INT(pop(S));
      ASSERT( ! stack_empty(S) );
      int32_t x = INT(pop(S));
      if ( y == 0 ) {
	c0_arith_error("Error: modulo by zero.");
      }
      else if ( y == -1 &&  x == (int32_t) MIN_INT ) {
	c0_arith_error("Error: modulo causes overflow.");
      }
      else {
	push(S, VAL(x%y));
      }
      
      break;
    }
      /*
       * 0x7E iand         S, x:w32, y:w32 -> S, x&y:w32
       */
    case IAND: {
      pc++;
      ASSERT( ! stack_empty(S) );
      uint32_t y = (uint32_t)(INT(pop(S)));
      ASSERT( ! stack_empty(S) );
      uint32_t x = (uint32_t)(INT(pop(S)));
      push(S, VAL((int32_t) (x & y)));
      
      break;
    }
      /*
       * 0x80 ior          S, x:w32, y:w32 -> S, x|y:w32
       */
    case IOR: {
      pc++;
      ASSERT( ! stack_empty(S) );
      uint32_t y = (uint32_t)(INT(pop(S)));
      ASSERT( ! stack_empty(S) );
      uint32_t x = (uint32_t)(INT(pop(S)));
      push(S, VAL((int32_t) (x | y)));
      
      break;
    }
      /*
       * 0x82 ixor         S, x:w32, y:w32 -> S, x^y:w32
       */
    case IXOR: {
      pc++;
      ASSERT( ! stack_empty(S) );
      uint32_t y = (uint32_t)(INT(pop(S)));
      ASSERT( ! stack_empty(S) );
      uint32_t x = (uint32_t)(INT(pop(S)));
      push(S, VAL((int32_t) (x ^ y)));
      
      break;
    }
      /*
       * 0x78 ishl         S, x:w32, y:w32 -> S, x<<y:w32
       */
    case ISHL: {
      pc++;
      ASSERT( ! stack_empty(S) );
      int32_t y = INT(pop(S)); // the amount to shift
      ASSERT( ! stack_empty(S) );
      uint32_t x = (uint32_t)(INT(pop(S)));
      if ( y < 0 || y > 31 ) {
	c0_arith_error("illegal shift.");
      }
      else {
	push(S, VAL((int32_t) (x << y)));
      }
      break;
    }
      /*
       * 0x7A ishr         S, x:w32, y:w32 -> S, x>>y:w32
       */
    case ISHR: {
      pc++;
      ASSERT( ! stack_empty(S) );
      int32_t y = INT(pop(S)); // the amount to shift
      ASSERT( ! stack_empty(S) );
      int32_t x = INT(pop(S));
      if ( y < 0 || y > 31 ) {
	c0_arith_error("illegal shift.");
      }
      else {
	push(S, VAL((int32_t) (x >> y)));
      }
      break;
    }
      
    /* Pushing small constants */
      /*
       * 0x10 bipush <b>    S -> S, x:w32     (x = (w32)b, sign extended)
       */
    case BIPUSH:
      pc++;
      push(S,  VAL((int32_t)(byte)(P[pc])));
      pc++;
      break;

    /* Returning from a function */
      /*
       * 0xB0 return   ., v -> .   (return v to caller)
       */
    case RETURN:
      {
	c0_value result = 0;
	if ( ! stack_empty(S) )
	  result = pop(S);
	free(V);
	stack_free(S, NULL); // here is where memory will leak (permissibly)
	if ( stack_empty(callStack) ) { // return from main function
	  stack_free(callStack, NULL);
	  return INT(result);
	}
	else { // return from non-main c0 function
	  frame caller = pop(callStack);
	  V = caller->V;
	  V_size = caller->num_vars;
	  S = caller->S;
	  P = caller->P;
	  pc = caller->pc;
	  free(caller);
	  push(S, result);
	}
      break;
      }

    /* Operations on local variables */

      /*
       * 0x15 vload <i>      S -> S, v        v = V[i]
       */
    case VLOAD: {
      pc++;
      size_t offset = (size_t)(P[pc]);
      ASSERT( ! (offset >= V_size) );
      push(S, V[offset]); // already a c0_value
      pc++;

      break;
    }      
      /*
       * 0x36 vstore <i>     S, v -> S        V[i] = v
       */
    case VSTORE: {
      pc++;
      size_t offset = (size_t)(P[pc]);
      ASSERT( ! (offset >= V_size) );
      ASSERT( ! stack_empty(S) );
      V[offset] = pop(S);
      pc++;

      break;
    }      
      /*
       * 0x01 aconst_null   S -> S, null:*
       */
    case ACONST_NULL: {
      pc++;
      push(S, NULL);

      break;
    }      
      
      /*
       * push a constant from the constant pool
       * 0x13 ildc <c1,c2>  S -> S, x:w32     (x = int_pool[(c1<<8)|c2])
       */
    case ILDC: {
      pc++;
      size_t offset = uoffset16(P, pc);
      ASSERT ( ! (offset >= bc0->int_pool_count) );
      push(S, VAL(bc0->int_pool[offset]));
      pc += 2;
      
      break;
    }
      /*
       * push the address of a character in the string pool
       * 0x14 aldc <c1,c2>  S -> S, a:*       (a = &string_pool[(c1<<8)|c2])
       */
    case ALDC: {
      pc++;
      size_t offset = uoffset16(P, pc);
      ASSERT ( ! (offset >= bc0->string_pool_count) );
      push(S, (c0_value) (bc0->string_pool+offset)); // the offset should be in bytes
      pc += 2;
      
      break;
    }
      
    /* Control flow operations */

      /*
       * 0x00 nop               S -> S
       */
    case NOP:
      pc++;
      break;
      
    /*
	if_cmpeq <o1,o2> S, v1, v2 -> S (pc = pc+(o1<<8|o2) if v1 == v2)
    */
    case IF_CMPEQ: {
      ASSERT(! stack_empty(S));
      c0_value v2 = pop(S);
      ASSERT(! stack_empty(S));
      c0_value v1 = pop(S);
      if ( v1 == v2 ) {
	int32_t offset = offset16(P, pc+1); // signed offset
	pc += offset;
      }
      else {
	pc +=3;
      }
      break;
    }
      
    /*
	0xA0 if_cmpne <o1,o2> S, v1, v2 -> S (pc = pc+(o1<<8|o2) if v1 != v2)
    */
    case IF_CMPNE: {
      ASSERT(! stack_empty(S));
      c0_value v2 = pop(S);
      ASSERT(! stack_empty(S));
      c0_value v1 = pop(S);
      if ( v1 != v2 ) {
	int32_t offset = offset16(P, pc+1); // signed offset
	pc += offset;
      }
      else {
	pc +=3;
      }
      break;
    }

    /*
	0xA1 if_icmplt <o1,o2> S, x:w32, y:w32 -> S (pc = pc+(o1<<8|o2) if x < y)
    */
    case IF_ICMPLT: {
      ASSERT(! stack_empty(S));
      int32_t v2 = INT(pop(S));
      ASSERT(! stack_empty(S));
      int32_t v1 = INT(pop(S));
      if ( v1 < v2 ) {
	int32_t offset = offset16(P, pc+1); // signed offset
	pc += offset;
      }
      else {
	pc +=3;
      }
      break;
    }
      
      /*
	0xA2 if_icmpge <o1,o2> S, x:w32, y:w32 -> S (pc = pc+(o1<<8|o2) if x >= y)
       */
    case IF_ICMPGE: {
      ASSERT(! stack_empty(S));
      int32_t v2 = INT(pop(S));
      ASSERT(! stack_empty(S));
      int32_t v1 = INT(pop(S));
      if ( v1 >= v2 ) {
	int32_t offset = offset16(P, pc+1); // signed offset
	pc += offset;
      }
      else {
	pc +=3;
      }
      break;
    }
      
      /*
	0xA3 if_icmpgt <o1,o2> S, x:w32, y:w32 -> S (pc = pc+(o1<<8|o2) if x > y)
       */
    case IF_ICMPGT: {
      ASSERT(! stack_empty(S));
      int32_t v2 = INT(pop(S));
      ASSERT(! stack_empty(S));
      int32_t v1 = INT(pop(S));
      if ( v1 > v2 ) {
	int32_t offset = offset16(P, pc+1); // signed offset
	pc += offset;
      }
      else {
	pc +=3;
      }
      break;
    }
      
      /*
	0xA4 if_icmple <o1,o2> S, x:w32, y:w32 -> S (pc = pc+(o1<<8|o2) if x <= y)
       */
    case IF_ICMPLE: {
      ASSERT(! stack_empty(S));
      int32_t v2 = INT(pop(S));
      ASSERT(! stack_empty(S));
      int32_t v1 = INT(pop(S));
      if ( v1 <= v2 ) {
	int32_t offset = offset16(P, pc+1); // signed offset
	pc += offset;
      }
      else {
	pc +=3;
      }
      break;
    }
      
      /*
	0xA7 goto <o1,o2> S -> S (pc = pc+(o1<<8|o2))
       */
    case GOTO: {
      int32_t offset = offset16(P, pc+1); // signed offset
      pc += offset;
      break;
    }
      
    case ATHROW: {
      pc++;
      ASSERT( ! stack_empty(S) );
      c0_value a = pop(S);
      c0_user_error(a);
      break;
    }

      /*
	0xCF assert S, x:w32, a:* -> S (c0_assertion_failure(a) if x == 0)
      */
    case ASSERT: {
      ASSERT(! stack_empty(S));
      c0_value *a = (c0_value*)(pop(S));
      ASSERT(! stack_empty(S));
      int32_t x = INT(pop(S));
      if ( x == 0 ) {
	ASSERT( a != NULL );
	c0_assertion_failure((char *)a);
      }
      else {
	pc++;
      }
      
      break;
    }

    /* Function call operations: */

    /*
	0xB8 invokestatic <c1,c2> S, v1, v2, ..., vn -> S, v
        	(function_pool[c1<<8|c2] = g, g(v1,...,vn) = v)

	but in small steps:
	0xB8 invokestatic <c1,c2> S, v1, v2, ..., vn -> .
	        (new stack frame has V, S, P, pc, num_vars)
	        (pc = function_pool+(c1<<8|c2), V initialized with v1, v2, ..., vn, S is a new empty stack)
     */
    case INVOKESTATIC: {
      size_t offset = uoffset16(P, pc+1);
      ASSERT( ! ( offset >= bc0->function_count ) );
      // new stack frame for current information
      frame new_frame = xmalloc(sizeof(struct frame));
      new_frame->V = V;
      new_frame->num_vars = V_size;
      new_frame->S = S;
      new_frame->P = P;
      new_frame->pc = pc+3;
      push(callStack, new_frame);
      // set up information for called function
      struct function_info new_fn = bc0->function_pool[offset];
      V = xcalloc(new_fn.num_vars, sizeof(c0_value));
      V_size = new_fn.num_vars;
      P = new_fn.code;
      pc = 0;
      // copy function arguments
      uint16_t args = new_fn.num_args;
      while ( args > 0 ) {
	ASSERT( ! stack_empty(S) );
	args--;
	V[args] = pop(S);
      }
      S = stack_new();

      break;
    }
      
    /*
	0xB7 invokenative <c1,c2> S, v1, v2, ..., vn -> S, v
    */
    case INVOKENATIVE: {
      size_t offset = uoffset16(P, pc+1);
      ASSERT( ! ( offset >= bc0->native_count ) );
      struct native_info fn_info = bc0->native_pool[offset];
      // copy function arguments
      uint16_t num_args = fn_info.num_args;
      c0_value *args = xcalloc(num_args, sizeof(c0_value));
      while ( num_args > 0 ) {
	ASSERT( ! stack_empty(S) );
	num_args--;
	args[num_args] = pop(S);
      }
      // call it and push the result
      native_fn callee = native_function_table[fn_info.function_table_index];
      push(S, (*callee)(args));
      free(args);
      pc +=3;

      break;
    }

      

    /* Memory allocation operations: */

    /*
	0xBB new <s> S -> S, a:* (*a is now allocated, size <s>)
     */
    case NEW: {
      pc++;
      size_t bytes = (size_t)P[pc];
      byte *p = xcalloc(bytes, sizeof(byte));
      push(S, (c0_value)p);
      pc++;

      break;
    }
      
    /*
	0xBC newarray <s> S, n:w32 -> S, a:* (a[0..n) now allocated)
    */
    case NEWARRAY: {
      pc++;
      ubyte size = (P[pc]); // number of bytes per element
      ASSERT( ! stack_empty(S) );
      int32_t count = INT(pop(S)); // number of elements
      if ( count < 0 )
	c0_memory_error("illegal array size");
      struct c0_array *a = xcalloc(1, sizeof(struct c0_array) + count*size);
      a->count = count;
      a->elt_size = size;
      push(S, (c0_value)a);
      pc++;

      break;
    }
      
    /*
	0xBE arraylength S, a:* -> S, n:w32 (n = \length(a))
    */
    case ARRAYLENGTH: {
      pc++;
      ASSERT( ! stack_empty(S) );
      struct c0_array *a = (struct c0_array *)pop(S);
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	push(S, VAL(a->count));
      }

      break;
    }

    /* Memory access operations: */

    /*
        Struct addressing; the operand is an offset in bytes
	0x62 aaddf <f> S, a:* -> S, (a+f):* (a != NULL; f field offset)
     */
    case AADDF: {
      ASSERT( ! stack_empty(S) );
      c0_value a = pop(S);
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	pc++;
	uintptr_t result = (uintptr_t)(P[pc]) + (uintptr_t)(a);
	push(S, (c0_value)result);
	pc++;
      }

      break;
    }
      
      /*
	Array addressing
	0x63 aadds S, a:*, i:w32 -> S, (a+s*i):* (a != NULL, 0 <= i < \length(a))
       */
    case AADDS: {
      pc++;
      ASSERT( ! stack_empty(S) );
      int32_t index = INT(pop(S));
      ASSERT( ! stack_empty(S) );
      struct c0_array *a = (struct c0_array *)pop(S);
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	if ( 0 > index || index >= a->count ) { // bounds check
	  c0_memory_error("array index out of bounds");
	}
	else {
	  byte *base_addr = (byte *)(&(a->elems));
	  push(S, (c0_value)(base_addr + index*a->elt_size));
	}
      }      

      break;
    }

      /*
	0x2E imload S, a:* -> S, x:w32 (x = *a, a != NULL, load 4 bytes)
       */
    case IMLOAD: {
      pc++;
      ASSERT( ! stack_empty(S) );
      c0_value a = pop(S);
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	push(S, VAL(*(int32_t *)a));
      }

      break;
    }      

      /*
	0x4E imstore S, a:*, x:w32 -> S (*a = x, a != NULL, store 4 bytes)
       */
    case IMSTORE: {
      pc++;
      ASSERT( ! stack_empty(S) );
      int32_t x = INT(pop(S));
      ASSERT( ! stack_empty(S) );
      int32_t *a = (int32_t *)(pop(S));
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	*a = x;
      }      

      break;
    }
      
      /*
	0x2F amload S, a:* -> S, b:* (b = *a, a != NULL, load address)
       */
    case AMLOAD: {
      pc++;
      ASSERT( ! stack_empty(S) );
      c0_value *a = (c0_value *)(pop(S));
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	push(S, (c0_value)(*a));
      }      

      break;
    }
      
      /*
	0x4F amstore S, a:*, b:* -> S (*a = b, a != NULL, store address)
       */
    case AMSTORE: {
      pc++;
      ASSERT( ! stack_empty(S) );
      c0_value b = pop(S);
      ASSERT( ! stack_empty(S) );
      c0_value *a = (c0_value *)(pop(S));
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	*a = b;
      }      

      break;
    }

      /*
	0x34 cmload S, a:* -> S, x:w32 (x = (w32)(*a), a != NULL, load 1 byte)
       */
    case CMLOAD: {
      pc++;
      ASSERT( ! stack_empty(S) );
      c0_value a = pop(S);
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	push(S, VAL(*(ubyte *)a));
      }

      break;
    }
      
      /*
	0x55 cmstore S, a:*, x:w32 -> S (*a = x & 0x7f, a != NULL, store 1 byte)
       */
    case CMSTORE: {
      pc++;
      ASSERT( ! stack_empty(S) );
      ubyte x = (ubyte)(INT(pop(S)));
      ASSERT( ! stack_empty(S) );
      ubyte *a = (ubyte *)(pop(S));
      if ( a == NULL ) {
	c0_memory_error("attempt to dereference null pointer");
      }
      else {
	*a = x;
      }      

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

