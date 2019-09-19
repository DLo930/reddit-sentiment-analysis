#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include "lib/bitarray.h"
#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "lib/boardutil.h"
#include "lib/queues.h"

struct position {
  bitarray moves;
  bitarray board;
};

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

void elem_free(queue_elem e) { free(e); }

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
  fprintf(stderr, "Starting with %d lights.\n", min);
  if (min == 0) return 0; 

  queue Q = queue_new();
  struct position *P = xmalloc(sizeof(struct position));
  P->moves = bitarray_new();
  P->board = board;
  enq(Q, P);

  while(!queue_empty(Q)) {
    P = (struct position*)deq(Q);
    
    for (uint8_t row = 0; row < height; row++) {
      for (uint8_t col = 0; col < width; col++) {
        // Only make unmade moves
        uint8_t i = get_index(row, col, width, height);
        if (!bitarray_get(P->moves, i)) {
          struct position *N = xmalloc(sizeof(struct position));
          N->moves = bitarray_flip(P->moves, i);
          N->board = press_button(P->board, row, col, width, height);
          
          uint8_t num = num_lights(N->board, width, height);
          if (num == 0) {
            print_solution(N->moves, width, height); 
            queue_free(Q, &free);
            return 0;
          } else if (num < min) {
            min = num;
            fprintf(stderr, "New minimum: %d\n", min);
          } 

          // print_board(N->board, width, height);
          // fprintf(stderr, "=========\n");
          
          enq(Q, N);
        }
      }
    }

    free(P);
  }

  fprintf(stderr, "No solution!\n");
  queue_free(Q, NULL);
  return 1;
}

