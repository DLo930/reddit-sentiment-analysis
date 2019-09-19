#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include "lib/bitarray.h"
#include "lib/contracts.h"

bitarray bitarray_new() {
  bitarray zeroes = 0;
  bitarray ones = zeroes - 1;
  return ones;
}

bool bitarray_get(bitarray n, uint8_t i) {
  REQUIRES(i < 64);
  uint8_t offset = BITARRAY_LIMIT - i - 1;
  uint64_t mask = 1 << offset;
  return (n & mask) == 0;
}

bitarray bitarray_flip(bitarray n, uint8_t i) {
  REQUIRES(i < 64);
  uint8_t offset = BITARRAY_LIMIT - i - 1;
  uint64_t mask = 1 << offset;
  return n ^ mask;
}


