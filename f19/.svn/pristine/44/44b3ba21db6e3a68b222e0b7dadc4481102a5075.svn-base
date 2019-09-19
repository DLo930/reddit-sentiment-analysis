#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include "lib/bitvector.h"
#include "lib/contracts.h"

bitvector bitvector_new() {
  bitvector zeroes = 0;
  bitvector ones = zeroes - 1;
  return ones;
}

bool bitvector_get(bitvector n, uint8_t i) {
  REQUIRES(i < BITVECTOR_LIMIT);
  uint8_t offset = BITVECTOR_LIMIT - i - 1;
  bitvector mask = 1;
  mask = mask << offset;
  return (n & mask) == 0;
}

bitvector bitvector_flip(bitvector n, uint8_t i) {
  REQUIRES(i < BITVECTOR_LIMIT);
  uint8_t offset = BITVECTOR_LIMIT - i - 1;
  bitvector mask = 1 << offset;
  return n ^ mask;
}


