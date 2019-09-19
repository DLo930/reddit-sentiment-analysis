/*
 * Graph Search - version 2: with adjacency matrix
 *
 * 15-122 Principles of Imperative Computation
 */

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "graph.h"
#include "graph-search.h"
#include "lib/contracts.h"
#include "lib/queue.h"
#include "lib/stack.h"
#include "lib/xalloc.h"

/* DFS Search using system stack (i.e. recursive) */

bool dfs_helper(graph_t G, bool *mark, vertex start, vertex target) {
  REQUIRES(G != NULL && mark != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));
  REQUIRES(!mark[start]);

  mark[start] = true;
  printf("    Visiting %u\n", start);

  if (target == start) return true;
  vert_list *nbors = graph_get_neighbors(G, start);
  for (vert_list *p = nbors; p != NULL; p = p->next) {
    vertex v = p->vert;
    if (!mark[v] && dfs_helper(G, mark, v, target)) {
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

  printf("DFS:\n");
  bool mark[graph_size(G)];
  for (vertex i = 0; i < graph_size(G); i++)
    mark[i] = false;
  return dfs_helper(G, mark, start, target);
}


/* BFS Search using queue */

bool bfs(graph_t G, vertex start, vertex target) {
  REQUIRES(G != NULL);
  REQUIRES(start < graph_size(G) && target < graph_size(G));

  printf("BFS:\n");

  if (start == target) return true;

  // mark is an array containing only the start
  bool mark[graph_size(G)];
  for (vertex i = 0; i < graph_size(G); i++)
    mark[i] = false;
  mark[start] = true;

  queue_t Q = queue_new();
  enq(Q, start);

  while (!queue_empty(Q)) {
    vertex v = deq(Q);     // v is the current node
    printf("    Visiting %u\n", v);
    vert_list *nbors = graph_get_neighbors(G, v);
    for (vert_list *p = nbors; p != NULL; p = p->next) {
      vertex w = p->vert;  // w is one of v's neighbors
      if (w == target) {   // if w is the target return true
        printf("    Found    %u !!!\n", w);
        queue_free(Q);
        graph_free_neighbors(nbors);
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
  return false;
}


bool connected(graph_t G) {
  REQUIRES(G != NULL);

  // TO BE COMPLETED




  return false;
}
