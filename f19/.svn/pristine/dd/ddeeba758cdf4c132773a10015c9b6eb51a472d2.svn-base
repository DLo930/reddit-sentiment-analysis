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

#define CHAR_MASK 0x7F

/* call stack frames */
typedef struct frame * frame;
struct frame {
  c0_value *V; /* local variables */
  stack S;     /* operand stack */
  ubyte *P;    /* function body */
  size_t pc;   /* return address */
};

// Difference between the next two functions is only return type

// pack two ubytes into an index for string or int pool
uint16_t pack_idx(ubyte c1, ubyte c2) {
    return (c1 << 8) | c2;
}

// pack ints together for a jump
int16_t pack_jump(ubyte c1, ubyte c2) {
    return (c1 << 8) | c2;
}

// calculate offest from P, to minimize code dup
int16_t prepare_jump(ubyte *P, size_t *pc) {
    ubyte o1 = P[(*pc)++];
    ubyte o2 = P[(*pc)++];
    return pack_jump(o1, o2);
}

// Adjust the pc by subtrcting 3 to correct for change already made
// and then adding the offset
void adjust_pc(size_t *pc, int16_t offset) {
    *pc -= 3; // correct for change we already made to pc
    *pc += offset;
}

int execute(struct bc0_file *bc0) {
  /* Variables used for bytecode interpreter. You will need to initialize
     these appropriately. */

  /* callStack to hold frames when functions are called */
  stack callStack = stack_new();
  /* initial program is the "main" function, function 0 (which must exist) */
  struct function_info *main_fn = bc0->function_pool;
  /* array to hold local variables for function */
  c0_value *V = xcalloc(main_fn->num_vars, sizeof(c0_value));
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

    case POP:
    {
      pop(S);
      break;
    }

    case DUP:
    {
      c0_value v = pop(S);
      push(S,v);
      push(S,v);
      break;
    }

    case SWAP:
    {
      c0_value v1 = pop(S);
      c0_value v2 = pop(S);
      push(S, v1);
      push(S, v2);
      break;
    }

     /* Arithmetic and Logical operations */

    case IADD:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        push(S, VAL(x + y));
        break;
    }

    case ISUB:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        push(S, VAL(x - y));
        break;
    }

    case IMUL:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        push(S, VAL(x * y));
        break;
    }

    case IDIV:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (y == 0 || (x == INT_MIN && y == -1)) {
            c0_arith_error("Illegal division!");
        }
        push(S, VAL(x / y));
        break;
    }

    case IREM:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (y == 0 || (x == INT_MIN && y == -1)) {
            c0_arith_error("Illegal mod!");
        }
        push(S, VAL(x % y));
        break;
    }

    case IAND:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        push(S, VAL(x & y));
        break;
    }

    case IOR:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        push(S, VAL(x | y));
        break;
    }

    case IXOR:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        push(S, VAL(x ^ y));
        break;
    }

    case ISHL:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (!(0 <= y && y < 32)) {
            c0_arith_error("Left shift by illegal amount!");
        }
        push(S, VAL(x << y));
        break;
    }

    case ISHR:
    {
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (!(0 <= y && y < 32)) {
            c0_arith_error("Right shift by illegal amount!");
        }
        push(S, VAL(x >> y));
        break;
    }


    /* Pushing small constants */

    case BIPUSH:
    {
        ubyte b = P[pc++];
        int32_t to_push = (int32_t) (byte) b; // up-cast to an int, sign extend
        push(S, VAL(to_push));
        break;
    }

    /* Returning from a function */

    case RETURN:
    {
        c0_value to_ret = pop(S);
        if (stack_empty(callStack)) {
            // We're in the main function
            // return value of main must be int
            int32_t int_ret = INT(to_ret);
            stack_free(callStack, NULL);
            stack_free(S, NULL);
            free(V);
            return int_ret;
        }
        struct frame *last = pop(callStack);

        free(V);
        V = last->V;

        stack_free(S, NULL);
        S = last->S;
        push(S, to_ret);

        P = last->P;
        pc = last->pc;

        free(last);

        break;
    }

    /* Operations on local variables */

    case VLOAD:
    {
        push(S, V[P[pc++]]);
        break;
    }

    case VSTORE:
    {
        V[P[pc++]] = pop(S);
        break;
    }

    case ACONST_NULL:
    {
        push(S, NULL);
        break;
    }

    case ILDC:
    {
        ubyte c1 = P[pc++];
        ubyte c2 = P[pc++];
        uint16_t idx = pack_idx(c1, c2);
        push(S, VAL((bc0->int_pool)[idx]));
        break;
    }

    case ALDC:
    {
        ubyte c1 = P[pc++];
        ubyte c2 = P[pc++];
        uint16_t idx = pack_idx(c1, c2);
        push(S, (bc0->string_pool) + idx);
        break;
    }


    /* Control flow operations */

    case NOP:
    {
        break;
    }

    case IF_CMPEQ:
    {
        int16_t offset = prepare_jump(P, &pc);
        c0_value val1 = pop(S);
        c0_value val2 = pop(S);
        if (val1 == val2) {
            adjust_pc(&pc, offset);
        }
        break;
    }

    case IF_CMPNE:
    {
        int16_t offset = prepare_jump(P, &pc);
        c0_value val1 = pop(S);
        c0_value val2 = pop(S);
        if (val1 != val2) {
            adjust_pc(&pc, offset);
        }
        break;
    }

    case IF_ICMPLT:
    {
        int16_t offset = prepare_jump(P, &pc);
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x < y) {
            adjust_pc(&pc, offset);
        }
        break;
    }

    case IF_ICMPGE:
    {
        int16_t offset = prepare_jump(P, &pc);
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x >= y) {
            adjust_pc(&pc, offset);
        }
        break;
    }

    case IF_ICMPGT:
    {
        int16_t offset = prepare_jump(P, &pc);
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x > y) {
            adjust_pc(&pc, offset);
        }
        break;
    }

    case IF_ICMPLE:
    {
        int16_t offset = prepare_jump(P, &pc);
        int32_t y = INT(pop(S));
        int32_t x = INT(pop(S));
        if (x <= y) {
            adjust_pc(&pc, offset);
        }
        break;
    }

    case GOTO:
    {
        int16_t offset = prepare_jump(P, &pc);
        adjust_pc(&pc, offset);
        break;
    }

    case ATHROW:
    {
      c0_value a = pop(S);
      c0_user_error(a);
      break;
    }

    case ASSERT:
    {
        char *msg = pop(S);
        int32_t cond = INT(pop(S));
        if (!cond) {
            c0_assertion_failure(msg);
        }
        break;
    }

    /* Function call operations: */

    case INVOKESTATIC:
    {
        ubyte c1 = P[pc++];
        ubyte c2 = P[pc++];
        uint16_t idx = pack_idx(c1, c2);
        struct function_info g = bc0->function_pool[idx];

        struct frame *cur_frame = xmalloc(sizeof(struct frame));
        cur_frame->V = V;
        cur_frame->S = S;
        cur_frame->P = P;
        cur_frame->pc = pc;
        push(callStack, cur_frame);

        assert(g.num_vars >= g.num_args);
        V = xcalloc(g.num_vars, sizeof(c0_value));
        for (size_t i = 0; i < g.num_args; i++) {
            V[g.num_args - 1 - i] = pop(S);
        }
        S = stack_new();
        P = g.code;
        pc = 0;

        break;
    }

    case INVOKENATIVE:
    {
        ubyte c1 = P[pc++];
        ubyte c2 = P[pc++];
        uint16_t idx = pack_idx(c1, c2);
        struct native_info g_info = bc0->native_pool[idx];
        c0_value *args = xmalloc(g_info.num_args * sizeof(c0_value));
        for (int i = 0; i < g_info.num_args; i++) {
            args[g_info.num_args - 1 - i] = pop(S);
        }
        c0_value (*g)(c0_value*) =
            native_function_table[g_info.function_table_index];
        push(S, g(args));
        free(args);
        break;
    }

    /* Memory allocation operations: */

    case NEW:
    {
        push(S, xcalloc(1,P[pc++]));
        break;
    }

    case NEWARRAY:
    {
       ubyte elt_size = P[pc++];
       int32_t num_elems = INT(pop(S));
       if (num_elems < 0) {
           c0_memory_error("Cannot allocate array with negative size!");
       }
       struct c0_array *arr =
           xcalloc(1, sizeof(struct c0_array) + elt_size*num_elems);
       arr->elt_size = elt_size;
       arr->count = num_elems;
       push(S, arr);
       break;
    }

    case ARRAYLENGTH:
    {
        struct c0_array *arr = (struct c0_array *) pop(S);
        push(S, VAL(arr->count));
        break;
    }

    /* Memory access operations: */

    case AADDF:
    {
        char *a = pop(S);
        if (a == NULL) {
            c0_memory_error("Attempt to access NULL struct!");
        }
        ubyte offset = P[pc++];
        push(S, a + offset);
        break;
    }

    case AADDS:
    {
        int32_t i = INT(pop(S));
        struct c0_array *arr = (struct c0_array *) pop(S);
        assert(arr != NULL);
        if (i < 0 || arr->count <= i) {
            c0_memory_error("invalid array access!");
        }
        push(S, (arr->elems) + (arr->elt_size * i));
        break;
    }

    case IMLOAD:
    {
       int32_t *p = pop(S);
       if (p == NULL) {
           c0_memory_error("NULL pointer dereference!");
       }
       push(S, VAL(*p));
       break;
    }

    case IMSTORE:
    {
        int32_t x = INT(pop(S));
        int32_t *p = pop(S);
        if (p == NULL) {
            c0_memory_error("NULL pointer dereference!");
        }
        *p = x;
        break;
    }

    case AMLOAD:
    {
        void** p = pop(S);
        if (p == NULL) {
            c0_memory_error("NULL pointer dereference!");
        }
        push(S, *p);
        break;
    }

    case AMSTORE:
    {
        void *b = pop(S);
        void **p = pop(S);
        if (p == NULL) {
            c0_memory_error("NULL pointer dereference!");
        }
        *p = b;
        break;
    }

    case CMLOAD:
    {
        char *p = pop(S);
        if (p == NULL) {
            c0_memory_error("NULL pointer dereference!");
        }
        char c = (*p) & CHAR_MASK;
        push(S, VAL((int) c));
        break;
    }

    case CMSTORE:
    {
        char c = INT(pop(S)) & CHAR_MASK;
        char *p = pop(S);
        if (p == NULL) {
            c0_memory_error("NULL pointer dereference!");
        }
        *p = c;
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

