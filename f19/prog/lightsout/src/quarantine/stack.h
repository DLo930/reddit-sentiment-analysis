/* 
 * Stacks 
 *
 * 15-122 Principles of Imperative Computation */

#include <stdbool.h>

#ifndef _STACK_H_
#define _STACK_H_

/*********************/
/* Client interface */
/*********************/

// typedef ______ stack_elem;
typedef void *stack_elem;

typedef void stack_elem_free_fn(stack_elem x);

/*********************/
/* Library interface */
/*********************/

// typedef ______* stack__t;
typedef struct stack_header *stack_t;

bool stack_empty(stack_t S)
  /*@requires S != NULL; @*/ ;

stack_t stack_new()
  /*@ensures \result != NULL; @*/ ;

void push(stack_t S, stack_elem x) 
  /*@requires S != NULL; @*/ ;

stack_elem pop(stack_t S)
  /*@requires S != NULL; @*/ ;

void stack_free(stack_t S, stack_elem_free_fn* elem_free)
  /*@requires S != NULL; @*/ 
  /* if elem_free is NULL, then elements will not be freed */ ;

#endif
