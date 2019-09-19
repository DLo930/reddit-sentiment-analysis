#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "lib/bitvector.h"

int f(char *s, int i) {
  fprintf(stderr, "%s\n", s);
  return i;
}

int c0_main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "Wrong number of args\n");
    exit(1);
  }
  char *cmd = argv[1];

  if (strcmp(cmd, "stress") == 0) {
    bitvector B = bitvector_new();

    // Check vector initially 0
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      if (!(bitvector_get(B, i) == false)) return f("A",1);
    }

    // Check all single 0->1 flips
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      bitvector Bi = bitvector_flip(B, i);
      for (uint8_t j = 0; j < BITVECTOR_LIMIT; j++) {
        if (i == j) {
          if (!(bitvector_get(Bi, j) == true)) return f("B",1);
        } else {
          if (!(bitvector_get(Bi, j) == false)) return f("C",1);
        }
      }
    }

    // Spectrum flip low-to-high
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      B = bitvector_flip(B, i);
      for (uint8_t j = 0; j < BITVECTOR_LIMIT; j++) {
        if (i >= j) {
          if (!(bitvector_get(B, j) == true)) return f("D",1);
        } else {
          if (!(bitvector_get(B, j) == false)) return f("E",1);
        }
      }
    }

    // Check all 1->0 flips
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      bitvector Bi = bitvector_flip(B, i);
      for (uint8_t j = 0; j < BITVECTOR_LIMIT; j++) {
        if (i == j) {
          if (!(bitvector_get(Bi, j) == false)) return f("F",1);
        } else {
          if (!(bitvector_get(Bi, j) == true)) return f("G",1);
        }
      }
    }

    // Spectrum flip high-to-low
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i--) {
      B = bitvector_flip(B, BITVECTOR_LIMIT-i-1);
      for (uint8_t j = 0; j < BITVECTOR_LIMIT; j++) {
        if (BITVECTOR_LIMIT-i-1 > j) {
          if (!(bitvector_get(B, j) == true)) return 1;
        } else {
          if (!(bitvector_get(B, j) == false)) return 1;
        }
      }
    }

    // Testing bit_equal
    if (!bitvector_equal(B, B)) return 1;
    bitvector BB = B;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      BB = bitvector_flip(BB, i);
      if (!bitvector_equal(BB, BB)) return 1;
      if (bitvector_equal(B, BB)) return 1;
    }

  } else if  (strcmp(cmd, "toobig1") == 0) {
    bitvector B = bitvector_new();
    bitvector_flip(B, BITVECTOR_LIMIT);

  } else if  (strcmp(cmd, "toobig2") == 0) {
    bitvector B = bitvector_new();
    bitvector_flip(B, UINT8_MAX);

  } else {
    fprintf(stderr, "Wrong argument\n");
    exit(1);
  }

  return 0;
}
