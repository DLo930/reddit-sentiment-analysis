#include <iostream>
#include <string.h>
#include <algorithm>
#include <assert.h>
#include "outputBMP.h"
using namespace std;

struct edge_t{
  int v1, v2;
  bool isRight;
};

int myrandom (int i) { return std::rand()%i;}

int alias(int* aliases, int i){
  while (aliases[i] >= 0){
    i = aliases[i];
  }
  return i;
}

void fillPixels(int* pixels, int imgWidth, int x1, int y1, int width, int height, int color){
  for (int x = x1; x < x1+width; x++){
    for (int y = y1; y < y1+height; y++){
      pixels[y*imgWidth+x] = color;
    }
  }
}

void kruskal(int num_vertices, int num_edges, int* graph, edge_t* edges){
  int count = 0;
  int* aliases = (int*) malloc(num_vertices * sizeof(int));
  fill_n(aliases, num_vertices, -1);
  int i=0;
  while (count < num_vertices - 1){
    int v1Alias = alias(aliases, edges[i].v1);
    int v2Alias = alias(aliases, edges[i].v2);
    if (v1Alias != v2Alias){ // Not already connected
      // Connect on graph
      if (edges[i].isRight){
        graph[edges[i].v1] |= 0b10;
      }else{
        graph[edges[i].v1] |= 0b01;
      }
      // Make aliases
      if (aliases[v1Alias] < aliases[v2Alias]){
          aliases[v2Alias] = v1Alias;
      }else if (aliases[v2Alias] < aliases[v1Alias]){
          aliases[v1Alias] = v2Alias;
      }else{ // Trees have same height
          aliases[v2Alias] = v1Alias;
          aliases[v1Alias] -= 1;
      }
      count++;
    }
    i++;
  }
  free(aliases);
}

int main(int argc, char** argv) {
  int width;
  int height;
  const char* filename;
  if (argc > 1){
    assert(argc == 4);
    width = atoi(argv[1]);
    height = atoi(argv[2]);
    filename = (const char*) argv[3];
  }else{
    width = 100;
    height = 100;
    filename = "maze.bmp";
  }
  int* graph = (int*) calloc(width*height, sizeof(int));

  int num_edges = width * height * 2 - width - height;
  edge_t* edges = (edge_t*) malloc(num_edges * sizeof(edge_t));
  int i=0;
  for (int y=0; y<height; y++){
    for (int x=0; x<width; x++){
        if (x!=width-1){
          edges[i].v1 = y*width+x;
          edges[i].v2 = y*width+x+1;
          edges[i].isRight = true;
          i++;
        }
        if (y!=height-1){
          edges[i].v1 = y*width+x;
          edges[i].v2 = (y+1)*width+x;
          edges[i].isRight = false;
          i++;
        }
    }
  }
  srand(time(0));
  random_shuffle(&edges[0], &edges[num_edges], myrandom);

  kruskal(width*height, num_edges, graph, edges);
  free(edges);

  int bSize = 2;
  int cSize = 2;
  cSize *= bSize;
  int imgWidth = (bSize*width) + (cSize*width) + bSize;
  int imgHeight = (bSize*height) + (cSize*height) + bSize;
  int* pixels = (int*)malloc(imgWidth*imgHeight * sizeof(int));
  fill_n(pixels, imgWidth*imgHeight, 0xFFFFFF);
  i=0;
  fillPixels(pixels, imgWidth, bSize+cSize, 0, imgWidth-bSize-cSize, bSize, 0); // Top
  fillPixels(pixels, imgWidth, 0, 0, bSize, imgHeight-bSize, 0); // Left
  graph[width*height-1] = 0b01; // Open Bottom Left
  for (int y=0; y<height; y++){
    for (int x=0; x<width; x++){
      if ((graph[i] & 0b10) == 0) // Vertical Walls
        fillPixels(pixels, imgWidth, (x+1)*(bSize+cSize), y*(bSize+cSize), bSize, bSize+cSize+bSize, 0);
      if ((graph[i] & 0b01) == 0) // Horizontal Walls
        fillPixels(pixels, imgWidth, x*(bSize+cSize), (y+1)*(bSize+cSize), bSize+cSize+bSize, bSize, 0);
      i++;
    }
  }
  free(graph);

  saveBMP(filename, imgWidth, imgHeight, pixels);
  free(pixels);
}
