/*
 * Graphs
 *
 * 15-122 Principles of Imperative Computation
 */

#include <stdlib.h>
#include "xalloc.h"
#include "contracts.h"
#include "graph.h"

typedef vert_list adjlist;

typedef struct graph_header graph;
struct graph_header {
  unsigned int size;
  adjlist **adj;      // adjlist*[] adj in C0
};

// Check for the presence of a vertex in an adjacency list
bool is_in_adjlist(adjlist *L, vertex v) {
  while (L != NULL) {
    if (L->vert == v) return true;
    L = L->next;
  }
  return false;
}

/* Data structure invariants */

bool is_vertex(graph *G, vertex v) {
  REQUIRES(G != NULL);
  return v < G->size;
}

bool is_adjlist(graph *G, vertex v, adjlist *L) {
  REQUIRES(G != NULL);
  //@requires(G->size == \length(G->adj));
  while (L != NULL) {
    if (!is_vertex(G, L->vert)) return false;

    // No self loops
    if (v == L->vert) return false;

    // Every outgoing edge a corresponding edge coming back to it
    if (!is_in_adjlist(G->adj[L->vert], v)) return false;

    // Edges aren't duplicated
    if (is_in_adjlist(L->next, L->vert)) return false;

    L = L->next;
  }
  return true;
}

bool is_graph(graph *G) {
  if (G == NULL) return false;
  //@assert(G->size == \length(G->adj));
  for (unsigned int i = 0; i < G->size; i++) {
    if (!is_adjlist(G, i, G->adj[i])) return false;
  }
  return true;
}

graph *graph_new(unsigned int size) {
  graph *G = xmalloc(sizeof(graph));
  G->size = size;
  G->adj = xcalloc(size, sizeof(adjlist*));
  ENSURES(is_graph(G));
  return G;
}

void graph_free(graph *G) {
  REQUIRES(is_graph(G));
  for (unsigned int i = 0; i < G->size; i++) {
    adjlist *L = G->adj[i];
    while (L != NULL) {
      adjlist *tmp = L->next;
      free(L);
      L = tmp;
    }
  }
  free(G->adj);
  free(G);
}

unsigned int graph_size(graph *G) {
  REQUIRES(is_graph(G));
  return G->size;
}

bool graph_hasedge(graph *G, vertex v, vertex w) {
  REQUIRES(is_graph(G) && is_vertex(G, v) && is_vertex(G, w));

  for (adjlist *L = G->adj[v]; L != NULL; L = L->next) {
    if (L->vert == w) return true;
  }
  return false;
}

void graph_addedge(graph *G, vertex v, vertex w) {
  REQUIRES(is_graph(G) && is_vertex(G, v) && is_vertex(G, w));
  REQUIRES(v != w && !graph_hasedge(G, v, w));

  adjlist *L;

  L = xmalloc(sizeof(adjlist));  // add w as a neighbor of v
  L->vert = w;
  L->next = G->adj[v];
  G->adj[v] = L;

  L = xmalloc(sizeof(adjlist));  // add v as a neighbor of w
  L->vert = v;
  L->next = G->adj[w];
  G->adj[w] = L;

  ENSURES(is_graph(G));
  ENSURES(graph_hasedge(G, v, w));
}

vert_list *graph_get_neighbors(graph *G, vertex v) {
  REQUIRES(is_graph(G) && is_vertex(G, v));
  return G->adj[v];
}

// Must not free anything since neighbors are the part of the representation
// using adjacency lists
void graph_free_neighbors(vert_list *L) {
  (void)L;
}
