#include <stdbool.h>
#include <stdio.h>
#include "lib/graph.h"
#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "lib/queue.h"
#include "lib/stack.h"


bool naive_dfs(graph_t G, vertex start, vertex target) {
  REQUIRES(G != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));
  printf("Visiting %u\n", start);

  // there is a path from start to target if
  // target == start, or
  // there is an edge from start to v
  // and a path from v to target

  return false;
}

bool dfs_helper(graph_t G, bool *mark, vertex start, vertex target) {
  REQUIRES(G != NULL && mark != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));
  REQUIRES(!mark[start]);

  // mark start as seen

  printf("Visiting %u\n", start);

  // there is a path from start to target if
  // target == start, or
  // there is an edge from start to v
  // and a path from v to target

  return false;
}

bool dfs(graph_t G, vertex start, vertex target) {
  REQUIRES(G != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));

  bool *mark = xcalloc(graph_size(G), sizeof(bool));
  bool connected = dfs_helper(G, mark, start, target);
  free(mark);
  return connected;
}

bool bfs(graph_t G, vertex start, vertex target) {
  REQUIRES(start < graph_size(G) && target < graph_size(G));
  REQUIRES(start < graph_size(G) && target < graph_size(G));

  if (start == target) return true;

  // mark is an array containing only the start
  bool *mark = xcalloc(graph_size(G), sizeof(bool));
  mark[start] = true;

  // Q initially is a queue containing only the start

  // while (!queue_empty(Q)) {
    // What is a useful invariant for us to think about involving the marks and the queue?
    // Find a node v that we haven't looked at yet
    // printf("    Visiting %u\n", v);
    //
    // for (every vertex w adjacent to v) {
      //
      // if w is the target
          // printf("    Visiting %u   Found !!!\n", w);
          // free(mark);
          // return true
      //
      // if w is not already marked
        // Insert it into the marks
        // Enqueue it onto the queue
  //   }
  // }

  free(mark);
  return false;
}

// Exercise: write iterative dfs by modifying the bfs code
// replacing the queue with a stack.

bool dfs_explicit_stack(graph_t G, vertex start, vertex target) {
  REQUIRES(G != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));
  REQUIRES(start < graph_size(G) && target < graph_size(G));

  return false;
}
