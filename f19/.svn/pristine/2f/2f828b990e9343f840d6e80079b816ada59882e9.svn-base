#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include "lib/bitvector.h"
#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "lib/boardutil.h"
#include "lib/queue.h"
#include "board-ht.h"

// Flips a bit, but only if it's a valid position
bitvector flip_maybe(bitvector b, int r, int c, uint8_t w, uint8_t h) {
  if (is_valid_pos(r, c, w, h))
    return bitvector_flip(b, get_index(r, c, w, h));
  return b;
}

// A button press in lights out toggles the r/c light as well as all
// touching lights
bitvector press_button(bitvector arr, int r, int c, uint8_t w, uint8_t h) {
  arr = bitvector_flip(arr, get_index(r, c, w, w));
  arr = flip_maybe(arr, r+1, c, w, h);
  arr = flip_maybe(arr, r-1, c, w, h);
  arr = flip_maybe(arr, r, c+1, w, h);
  arr = flip_maybe(arr, r, c-1, w, h);
  return arr;
}

// Takes a bitmask and prints out the solution
void print_solution(bitvector B, hdict_t H, uint8_t width, uint8_t height,
                    struct board_data* P) {
  REQUIRES(P != NULL);

  print_board(P->board, width, height);
  if (bitvector_equal(B, P->board)) return;
  uint8_t move = P->test;
  uint8_t r = move / width;
  uint8_t c = move % width;
  bitvector B2 = press_button(P->board, r, c, width, height);
  printf("%d:%d\n", r, c);
  print_solution(B, H, width, height, ht_lookup(H, B2));
}

// Count the number of lights on a board
uint8_t num_lights(bitvector arr, uint8_t width, uint8_t height) {
  uint8_t n = 0;
  for (uint8_t row = 0; row < height; row++)
    for (uint8_t col = 0; col < width; col++)
      if (bitvector_get(arr, get_index(row, col, width, height)))
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
  bitvector board;
  uint8_t width;
  uint8_t height;
  if (!file_read(argv[1], &board, &width, &height)) {
    fprintf(stderr, "Error: unable to read file %s\n", argv[1]);
    return 1;
  }

  print_board(board, width, height);

  // Make sure there's anything to do!
  uint8_t min = num_lights(board, width, height);
  fprintf(stderr, "Starting with %d lights.\n", min);
  if (min == 0) return 0;

  queue_t Q = queue_new();
  hdict_t H = ht_new(1000000);
  struct board_data *P = xmalloc(sizeof(struct board_data));
  P->test = 0;
  P->board = board;
  enq(Q, P);
  ht_insert(H, P);

  while(!queue_empty(Q)) {
    P = (struct board_data*)deq(Q);

    for (uint8_t row = 0; row < height; row++) {
      for (uint8_t col = 0; col < width; col++) {
        // Only make unmade moves
        uint8_t i = get_index(row, col, width, height);
        bitvector newboard = press_button(P->board, row, col, width, height);

        if (num_lights(newboard, width, height) == 0) {
          print_board(newboard, width, height);
          printf("%d:%d\n", row, col);
          print_solution(board, H, width, height, P);
          queue_free(Q, NULL);
          hdict_free(H);
          return 0;
        }

        if (ht_lookup(H, newboard) == NULL) {
          // Oh, it's a new board!
          // fprintf(stderr, "========\n");
          // print_board(newboard, width, height);
          struct board_data *N = xmalloc(sizeof(struct board_data));
          N->test = i;
          N->board = newboard;
          ht_insert(H, N);
          enq(Q, N);
        }
      }
    }
  }

  fprintf(stderr, "No solution!\n");
  queue_free(Q, NULL);
  hdict_free(H);
  return 1;
}

