/*
 * Graphs - version 2: Adjacency Matrix
 *
 * 15-122 Principles of Imperative Computation
 */

#include <stdlib.h>
#include "graph.h"
#include "lib/xalloc.h"
#include "lib/contracts.h"

typedef struct graph_header graph;
struct graph_header {
  unsigned int size;
  bool **adj;        // Pointer to adjacency matrix
};

/* Data structure invariants */

bool is_vertex(graph *G, vertex v) {
  REQUIRES(G != NULL);
  return v < G->size;
}

bool is_graph(graph *G) {
  if (G == NULL) return false;
  if (G->adj == NULL) return false;
  for (unsigned int i = 0; i < G->size; i++) {
    if (G->adj[i] == NULL) return false;
  }

  // TO BE COMPLETED:





  return true;
}

graph *graph_new(unsigned int size) {
  graph *G = xmalloc(sizeof(graph));
  // TO BE COMPLETED:





  ENSURES(is_graph(G));
  return G;
}

void graph_free(graph *G) {
  REQUIRES(is_graph(G));
  // TO BE COMPLETED:





  free(G);
}

unsigned int graph_size(graph *G) {
  REQUIRES(is_graph(G));
  return G->size;
}

bool graph_hasedge(graph *G, vertex v, vertex w) {
  REQUIRES(is_graph(G) && is_vertex(G, v) && is_vertex(G, w));
  // TO BE COMPLETED:




  return false;
}

void graph_addedge(graph *G, vertex v, vertex w) {
  REQUIRES(is_graph(G) && is_vertex(G, v) && is_vertex(G, w));
  REQUIRES(v != w && !graph_hasedge(G, v, w));
  // TO BE COMPLETED:





  ENSURES(is_graph(G));
}

// EXTRA CHALLENGE:
//    implement graph_get_neighbors and graph_free_neighbors
// If you are not up for it, their code is at the bottom of this file

// vert_list *graph_get_neighbors(graph *G, vertex v) {
//  REQUIRES(is_graph(G) && is_vertex(G, v));
    // TO BE COMPLETED OPTIONALLY


// }

// void graph_free_neighbors(vert_list *L) {
    // TO BE COMPLETED OPTIONALLY


// }

// IF YOU ATTEMPTED THESE FUNCTION, COMMENT THE CODE BELOW



























vert_list *graph_get_neighbors(graph *G, vertex v) {
  REQUIRES(is_graph(G) && is_vertex(G, v));
  vert_list *L = NULL;
  for (vertex w = 0; w < graph_size(G); w++) {
    if (graph_hasedge(G, v, w)) {
      vert_list *node = xmalloc(sizeof(vert_list));
      node->vert = w;
      node->next = L;
      L = node;
    }
  }
  return L;
}

void graph_free_neighbors(vert_list *L) {
  if (L == NULL) return;
  graph_free_neighbors(L->next);
  free(L);
}
