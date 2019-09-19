/*
 * Graphs
 *
 * 15-122 Principles of Imperative Computation
 */

#ifndef _GRAPH_H
#define _GRAPH_H

#include <stdbool.h>

typedef unsigned int vertex;
typedef struct graph_header *graph_t;

graph_t graph_new(unsigned int numvert); // New graph with numvert vertices
//@ensures \result != NULL;

void graph_free(graph_t G);
//@requires G != NULL;

unsigned int graph_size(graph_t G);  // Number of vertices in the graph
//@requires G != NULL;

bool graph_hasedge(graph_t G, vertex v, vertex w);
//@requires G != NULL;
//@requires v < graph_size(G) && w < graph_size(G);

void graph_addedge(graph_t G, vertex v, vertex w); // Edge can't be in graph!
//@requires G != NULL;
//@requires v < graph_size(G) && w < graph_size(G);
//@requires v != w && !graph_hasedge(G, v, w);

typedef struct vert_list_node vert_list;
struct vert_list_node {
  vertex vert;
  vert_list *next;
};

vert_list* graph_get_neighbors(graph_t G, vertex v);
//@requires G != NULL;
//@requires v < graph_size(G);

void graph_free_neighbors(vert_list* neighbors);

#endif
