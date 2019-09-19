#include <stdlib.h>
#include <stdio.h>
#include "lib/bitvector.h"
#include "lib/contracts.h"
#include "lib/boardutil.h"

/* Read from standard input, ignore whitespace */
static inline char read_non_space() {
  char c;
  do c = fgetc(stdin);
  while (c == ' ' || c == '\n' || c == '\t');
  return c;
}

/* Interprets a char as a digit, returns -1 if it isn't one */
static inline int digit(char c) {
  if ('0' <= c && c <= '9')
    return c - '0';
  return -1;
}

/* Flips a bit, but only if it's a valid position */
static inline bitvector flip_maybe(bitvector b,
                                  int r, int c, uint8_t w, uint8_t h) {
  if (is_valid_pos(r, c, w, h))
    return bitvector_flip(b, get_index(r, c, w, h));
  return b;
}

int main(int argc, char **argv) {
  // Command line arguments
  if (argc != 2) {
    fprintf(stderr, "Usage: loplayer <filename>\n");
    return 1;
  }

  // Read in board
  bitvector arr;
  uint8_t width;
  uint8_t height;
  if (!file_read(argv[1], &arr, &width, &height)) {
    fprintf(stderr, "Error: unable to read file %s\n", argv[1]);
    return 1;
  }

  while(true) {
    print_board(arr, width, height);

    int j = 0;
    for (int i = 0; i < width*height; i++) {
      if (bitvector_get(arr, i)) j++;
    }
    if (j == 0) {
      printf("You got all the lights out!\n");
      return 0;
    }

    char c = read_non_space();
    if (c == EOF) {
      printf("Goodbye\n");
      return 1;
    }
    int row = digit(c);
    if (row < 0 || row >= height) {
      printf("Invalid character '%c' (expected a digit <= %d)\n", c, height);
      return 1;
    }
    if (read_non_space() != ':') {
      printf("Invalid character '%c' (expected ':')\n", c);
      return 1;
    }
    c = read_non_space();
    int col = digit(c);
    if (col < 0 || col >= width) {
      printf("Invalid character '%c' (expected a digit <= %d)\n", c, width);
      return 1;
    }

    printf("Flipping %d:%d\n", row, col);
    arr = bitvector_flip(arr, get_index(row, col, width, height));
    arr = flip_maybe(arr, row+1, col, width, height);
    arr = flip_maybe(arr, row-1, col, width, height);
    arr = flip_maybe(arr, row, col+1, width, height);
    arr = flip_maybe(arr, row, col-1, width, height);
  }
}
