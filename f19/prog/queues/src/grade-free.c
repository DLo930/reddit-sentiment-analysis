#include <stdlib.h>
#include <string.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"
#include "queue.h"

void queue_freer(void* Q) {
  queue_free((queue_t)Q, &free);
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
  
  if (strcmp(cmd, "free_precon1") == 0) { queue_size(NULL);
  } else if (strcmp(cmd, "free_precon2") == 0) { queue_size(inval()); 
  } else if (strcmp(cmd, "tests") == 0) {
    queue_t Q = queue_new();
    queue_t R;

    R = queue_new();
    queue_free(R, &queue_freer);
    R = queue_new();
    queue_free(R, &free);
    R = queue_new();
    queue_free(R, NULL);

    R = queue_new();
    enq(R, R);
    enq(R, R);
    enq(R, R);
    enq(R, R);
    queue_free(R, NULL);

    R = queue_new();
    enq(R, xmalloc(4));
    enq(R, xmalloc(4));
    enq(R, xmalloc(4));
    enq(Q, R);

    R = queue_new();
    enq(R, xmalloc(4));
    enq(R, xmalloc(4));
    enq(Q, R);
    
    R = queue_new();
    enq(Q, R);

    R = queue_new();
    enq(R, xmalloc(4));
    enq(R, xmalloc(4));
    enq(Q, R);

    queue_free(Q, &queue_freer);
  } else {
    assert(false);
  }

  return 0;
}
