#include <string.h>
#include <stdlib.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"
#include "queue.h"

bool nonnull(void* x) {
  return x != NULL;
}

void* id(void* accum, void* x)
//@requires accum != NULL && \hastag(int*, accum);
//@requires x != NULL && \hastag(int*, x);
{
  (void)x;
  return accum;
}

queue_t inval() {
  void** Q = xcalloc(8, 8);
  *Q = xcalloc(8, 8);
  return (queue_t)Q;
}

int c0_main(int argc, char **argv) {
  if (argc < 2) {
    fprintf(stderr, "Must pass task number on command line\n");
    fprintf(stderr, "One of task1, task2, task2, stress <n>, contracts\n");
    return 2;
  }

  char* cmd = argv[1];
  
  if (strcmp(cmd, "size_precon1") == 0) { queue_size(NULL);
  } else if (strcmp(cmd, "size_precon2") == 0) { queue_size(inval()); 
  } else if (strcmp(cmd, "enq_precon1") == 0) { enq(NULL, NULL);
  } else if (strcmp(cmd, "enq_precon2") == 0) { enq(inval(), inval());
  } else if (strcmp(cmd, "deq_precon1") == 0) { deq(NULL);
  } else if (strcmp(cmd, "deq_precon2") == 0) { deq(inval());
  } else if (strcmp(cmd, "deq_precon3") == 0) { deq(queue_new());
  } else if (strcmp(cmd, "peek_precon1") == 0) { queue_peek(NULL,0);
  } else if (strcmp(cmd, "peek_precon2") == 0) { queue_peek(inval(),0);
  } else if (strcmp(cmd, "peek_precon3") == 0) { queue_peek(queue_new(),0);
  } else if (strcmp(cmd, "peek_precon4") == 0) { queue_peek(queue_new(),-1);
  } else if (strcmp(cmd, "rev_precon1") == 0) { queue_reverse(NULL); 
  } else if (strcmp(cmd, "rev_precon2") == 0) { queue_reverse(inval()); 
  } else if (strcmp(cmd, "all_precon1") == 0) { queue_all(NULL, &nonnull);
  } else if (strcmp(cmd, "all_precon2") == 0) { queue_all(inval(), &nonnull);
  } else if (strcmp(cmd, "all_precon3") == 0) { queue_all(queue_new(), NULL);
  } else if (strcmp(cmd, "iter_precon1") == 0) { 
    queue_iterate(NULL, NULL, &id);
  } else if (strcmp(cmd, "iter_precon2") == 0) { 
    queue_iterate(inval(), NULL, &id);
  } else if (strcmp(cmd, "iter_precon3") == 0) {
    queue_iterate(queue_new(), NULL, NULL);

  } else if (strcmp(cmd, "tests") == 0) {
    queue_t Q = queue_new();
    printf("A\n");
    if (queue_size(Q) != 0) return 1;
    enq(Q, NULL);
    printf("B\n");
    if (queue_size(Q) != 1) return 1;
    enq(Q, NULL);
    enq(Q, Q);
    printf("C\n");
    if (queue_size(Q) != 3) return 1;
    if (queue_peek(Q, 0) != NULL) return 1;
    if (queue_peek(Q, 1) != NULL) return 1;
    if (queue_peek(Q, 2) != Q) return 1;
    queue_reverse(Q);
    printf("D\n");
    if (queue_size(Q) != 3) return 1;
    if (deq(Q) != Q) return 1;
    enq(Q, Q);
    if (queue_all(Q, &nonnull)) return 1;
    if (deq(Q) != NULL) return 1;
    printf("E\n");
    if (queue_size(Q) != 2) return 1;
    if (deq(Q) != NULL) return 1;
    printf("F\n");
    if (queue_size(Q) != 1) return 1;
    if (!queue_all(Q, &nonnull)) return 1;
    if (Q != queue_iterate(Q, Q, &id)) return 1;
    if (NULL != queue_iterate(Q, NULL, &id)) return 1;
    if (deq(Q) != Q) return 1;
    printf("G\n");
    if (queue_size(Q) != 0) return 1;
    free(Q);
  } else {
    assert(false);
  }

  return 0;
}
