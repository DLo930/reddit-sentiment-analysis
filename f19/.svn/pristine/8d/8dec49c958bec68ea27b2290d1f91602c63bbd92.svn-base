#include <stdio.h>
#include <assert.h>
#include "graph.h"

void graph_print(graph_t G) {
  for (vertex v = 0; v < graph_size(G); v++) {
    printf("Vertices connected to %u: ", v);
    vert_list *nbors = graph_get_neighbors(G, v);
    for (vert_list *p = nbors; p != NULL; p = p->next) {
      vertex w = p->vert;   // w is a neighbor of v
      printf(" %u,", w);
    }
    graph_free_neighbors(nbors);
    printf("\n");
  }
}

int main() {
  graph_t G = graph_new(5);

  graph_addedge(G, 0, 1); // AB

  graph_addedge(G, 1, 2); // BC
  graph_addedge(G, 2, 3); // CD
  graph_addedge(G, 0, 4); // AE
  graph_addedge(G, 1, 4); // BE
  graph_addedge(G, 2, 4); // CE

  graph_print(G);

  assert( graph_hasedge(G, 2, 4)); // CE
  assert( graph_hasedge(G, 4, 2)); // EC
  assert(!graph_hasedge(G, 0, 3)); // AD
  assert(!graph_hasedge(G, 3, 0)); // DA

  graph_free(G);
  printf("Success!\n\n");
}
