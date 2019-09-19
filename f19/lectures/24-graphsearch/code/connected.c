/*
 * Graph search
 *
 * 15-122 Principles of Imperative Computation
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "lib/graph.h"
#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "lib/queue.h"
#include "lib/stack.h"


bool naive_dfs(graph_t G, vertex start, vertex target) {
  REQUIRES(G != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));
  printf("    Visiting %u\n", start);

  // there is a path from start to target if
  // target == start, or
  if (target == start) return true;
  // there is an edge from start to v ...
  vert_list *nbors = graph_get_neighbors(G, start);
  for (vert_list *p = nbors; p != NULL; p = p->next) {
    vertex v = p->vert;             // v is one of start's neighbors
    if (naive_dfs(G, v, target)) {  // ... and a path from v to target
      graph_free_neighbors(nbors);
      return true;
    }
  }
  graph_free_neighbors(nbors);
  return false;
}

bool dfs_helper(graph_t G, bool *mark, vertex start, vertex target) {
  REQUIRES(G != NULL && mark != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));
  REQUIRES(!mark[start]);

  // mark start as seen
  mark[start] = true;
  printf("    Visiting %u\n", start);

  // there is an edge from start to v and a path from v to target if...
  // target == start, or
  if (target == start) return true;
  // there is an edge from start to v ...
  vert_list *nbors = graph_get_neighbors(G, start);
  for (vert_list *p = nbors; p != NULL; p = p->next) {
    vertex v = p->vert;                                // v is one of start's neighbors
    if (!mark[v] && dfs_helper(G, mark, v, target)) {  // ... and a path from v to target
      graph_free_neighbors(nbors);
      return true;
    }
  }
  graph_free_neighbors(nbors);
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
  REQUIRES(G != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));

  if (start == target) return true;

  // mark is an array containing only the start
  bool *mark = xcalloc(graph_size(G), sizeof(bool));
  mark[start] = true;

  // Q initially is a queue containing only the start
  queue_t Q = queue_new();
  enq(Q, start);

  while (!queue_empty(Q)) {
    // LI 1: every marked vertex is connected to start
    // LI 2: every vertex in Q is marked
    // LI 3: Every path from start to target goes through a vertex in Q

    // Find a node v that we haven't looked at yet
    vertex v = deq(Q);     // v is the current node
    printf("    Visiting %u\n", v);
    //   for (every vertex w adjacent to v) {
    vert_list *nbors = graph_get_neighbors(G, v);
    for (vert_list *p = nbors; p != NULL; p = p->next) {
      vertex w = p->vert;  // w is one of v's neighbors
      if (w == target) {   // if w is the target return true
        printf("    Visiting %u   Found !!!\n", w);
        graph_free_neighbors(nbors);
        queue_free(Q);
        free(mark);
        return true;
      }

      if (!mark[w]) {      // if w is not already marked
        mark[w] = true;       // Insert it into the marks
        enq(Q, w);            // Enqueue it onto the queue
      }
    }
    graph_free_neighbors(nbors);
  }
  queue_free(Q);
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
