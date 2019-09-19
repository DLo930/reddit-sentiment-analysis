#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include "lib/bitarray.h"
#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "lib/boardutil.h"
#include "lib/queues.h"
#include "lib/ht.h"
#include "lib/pq.h"

// Client interface

struct position {
  bitarray moves;
  bitarray board;
  uint8_t num_moves;
  uint8_t num_lights;
};

ht_key elem_key(ht_elem e) {
  struct position* p = e;
  return &p->board;
}

bool key_equal(ht_key k1, ht_key k2) {
  bitarray b1 = *(bitarray*)k1;
  bitarray b2 = *(bitarray*)k2;
  return b1 == b2;
}

size_t key_hash(ht_key k1) {
  bitarray b = *(bitarray*)k1;
  size_t k = b;
  return k*1664525  + 1013904223;
}

unsigned int elem_priority(pq_elem e) {
  struct position* p = e;
  return p->num_lights;
}

// Flips a bit, but only if it's a valid position
bitarray flip_maybe(bitarray b, int r, int c, uint8_t w, uint8_t h) {
  if (is_valid_pos(r, c, w, h)) 
    return bitarray_flip(b, get_index(r, c, w, h));
  return b;
}

// A button press in lights out toggles the r/c light as well as all
// touching lights
bitarray press_button(bitarray arr, int r, int c, uint8_t w, uint8_t h) {
  arr = bitarray_flip(arr, get_index(r, c, w, w));
  arr = flip_maybe(arr, r+1, c, w, h);
  arr = flip_maybe(arr, r-1, c, w, h);
  arr = flip_maybe(arr, r, c+1, w, h);
  arr = flip_maybe(arr, r, c-1, w, h);
  return arr;
}

// Takes a bitmask and prints out the solution
void print_solution(bitarray b, int width, int height) {
  for (uint8_t row = 0; row < height; row++) 
    for (uint8_t col = 0; col < width; col++) 
      if (bitarray_get(b, get_index(row, col, width, height))) 
        printf("%d:%d\n", row, col);
}

// Count the number of lights on a board
uint8_t num_lights(bitarray arr, uint8_t width, uint8_t height) {
  uint8_t n = 0;
  for (uint8_t row = 0; row < height; row++) 
    for (uint8_t col = 0; col < width; col++) 
      if (bitarray_get(arr, get_index(row, col, width, height))) 
        n++;

  return n;
}

int main(int argc, char **argv) {
  // Command line arguments
  if (argc != 2) {
    fprintf(stderr, "Usage: loplayer <filename>\n");
    return 1;
  }

  // Read in board
  bitarray board;
  uint8_t width;
  uint8_t height;
  if (!file_read(argv[1], &board, &width, &height)) {
    fprintf(stderr, "Error: unable to read file %s\n", argv[1]);
    return 1;
  }

  // Make sure there's anything to do!
  uint8_t min = num_lights(board, width, height);
  uint8_t max_moves = 0;
  fprintf(stderr, "Starting with %d lights.\n", min);
  if (min == 0) return 0; 

  pq PQ = pq_new(100000, &elem_priority, NULL);
  ht H = ht_new(1000000, &elem_key, &key_equal, &key_hash, &free);
  struct position *P = xmalloc(sizeof(struct position));
  P->moves = bitarray_new();
  P->board = board;
  P->num_moves = 0;
  P->num_lights = min;
  pq_insert(PQ, P);

  while(!pq_empty(PQ)) {
    P = (struct position*)pq_delmin(PQ);
    
    if (P->num_moves > max_moves) {
      fprintf(stderr, "Now considering boards after %d moves\n", P->num_moves);
      max_moves = P->num_moves;
    }

    // fprintf(stderr, "========\n");
    // print_board(P->board, width, height);

    for (uint8_t row = 0; row < height; row++) {
      for (uint8_t col = 0; col < width; col++) {
        // Only make unmade moves
        uint8_t i = get_index(row, col, width, height);
        if (!bitarray_get(P->moves, i)) {
          bitarray newmoves = bitarray_flip(P->moves, i);
          bitarray newboard = press_button(P->board, row, col, width, height);
          
          uint8_t num = num_lights(newboard, width, height);
          if (num == 0) {
            print_solution(newmoves, width, height); 
            pq_free(PQ);
            ht_free(H);
            return 0;
          } else if (num < min) {
            min = num;
            fprintf(stderr, "New minimum: %d\n", min);
          } 

          if (ht_lookup(H, &newboard) == NULL) {
            // Oh, it's a new board!
            struct position *N = xmalloc(sizeof(struct position));
            N->moves = newmoves;
            N->board = newboard;
            N->num_moves = P->num_moves + 1;
            N->num_lights = num;
            ht_insert(H, N);
            pq_insert(PQ, N);
          } else {
            // fprintf(stderr, "======= Already seen this one\n");
            // print_board(newboard, width, height);
          }
        }
      }
    }
  }

  fprintf(stderr, "No solution!\n");
  pq_free(PQ);
  ht_free(H);
  return 1;
}

