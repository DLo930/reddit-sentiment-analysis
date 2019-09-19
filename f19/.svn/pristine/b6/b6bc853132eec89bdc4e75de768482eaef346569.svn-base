#include <stdlib.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"
#include "queue.h"

typedef struct list_node list;
struct list_node {
  void* data;
  list* next;
};

bool is_inclusive_segment(list* start, list* end, int i) {
  if (i < 0) return false;
  if (i == 0) return start == NULL;
  if (i == 1) return start != NULL && start == end && start->next == NULL;
  return start != NULL && start != end
    && is_inclusive_segment(start->next, end, i-1);
}
typedef struct queue_header queue;
struct queue_header {
  list* front;
  list* back;
  size_t size;
};

bool is_queue(queue* Q) {
  if (Q == NULL) return false;
  return is_inclusive_segment(Q->front, Q->back, Q->size);
}

queue* queue_new()
//@ensures is_queue(\result);
{
  queue* Q = xmalloc(sizeof(queue));
  Q->front = NULL;
  Q->size = 0;
  ENSURES(is_queue(Q));
  return Q;
}

size_t queue_size(queue* Q)
//@requires is_queue(Q);
{
  REQUIRES(is_queue(Q));
  return Q->size;
}

void enq(queue* Q, void* x)
//@requires is_queue(Q);
//@ensures is_queue(Q);
{
  REQUIRES(is_queue(Q));
  (Q->size)++;
  if (Q->front == NULL) {
    Q->front = xmalloc(sizeof(list));
    Q->back = Q->front;
  } else {
    Q->back->next = xmalloc(sizeof(list));
    Q->back = Q->back->next;
  }
  Q->back->data = x;
  Q->back->next = NULL;
}

void* deq(queue* Q)
//@requires is_queue(Q);
//@ensures is_queue(Q);
{
  REQUIRES(is_queue(Q));
  REQUIRES(queue_size(Q) > 0);
  (Q->size)--;
  void* x = Q->front->data;
  list* L = Q->front;
  Q->front = Q->front->next;
  free(L);
  return x;
}

void* queue_peek(queue* Q, size_t i)
//@requires is_queue(Q);
{
  REQUIRES(is_queue(Q) && i < queue_size(Q));
  list* L = Q->front;

  for (size_t j = 0; j < i; j++)
  //@loop_invariant 0 <= j && j <= i;
  //@loop_invariant is_inclusive_segment(L, Q->back, Q->size - j);
  {
    L = L->next;
  }

  return L->data;
}

void queue_reverse(queue* Q)
//@requires is_queue(Q);
//@ensures is_queue(Q);
{
  REQUIRES(is_queue(Q));
  if (Q->size <= 1) return;

  list* trail = Q->front;
  list* lead = Q->front->next;
  trail->next = NULL;

  for (size_t i = 1; i < Q->size; i++)
  //@loop_invariant 0 <= i && i <= Q->size;
  //@loop_invariant is_inclusive_segment(trail, Q->front, i);
  //@loop_invariant is_inclusive_segment(lead, Q->back, Q->size - i);
  {
    list* ahead = lead->next;
    lead->next = trail;
    trail = lead;
    lead = ahead;
  }

  Q->back = Q->front;
  Q->front = trail;
}

bool queue_all(queue* Q, check_property_fn* P)
//@requires is_queue(Q);
{
  REQUIRES(is_queue(Q) && P != NULL);
  list* L = Q->front;

  for (size_t i = 0; i < Q->size; i++)
  //@loop_invariant 0 <= i && i <= Q->size;
  //@loop_invariant is_inclusive_segment(L, Q->back, Q->size - i);
  {
    if (!(*P)(L->data)) return false;
    L = L->next;
  }

  return true;
}

/* O(n) worst case, assuming accum is O(1) */
void* queue_iterate(queue* Q, void* accum, iterate_fn* F) {
  REQUIRES(is_queue(Q) && F != NULL);
  list* L = Q->front;

  for (size_t i = 0; i < Q->size; i++)
  //@loop_invariant 0 <= i && i <= Q->size;
  //@loop_invariant is_inclusive_segment(L, Q->back, Q->size - i);
  {
    accum = (*F)(accum, L->data);
    L = L->next;
  }

  return accum;
}

void queue_free(queue* Q, free_fn* F) {
  REQUIRES(is_queue(Q));
  list* q;
  for (list* p = Q->front; p != NULL; p = q) {
    if (F != NULL) (*F)(p->data);
    q = p->next;
    free(p);
  }
  free(Q);
}
