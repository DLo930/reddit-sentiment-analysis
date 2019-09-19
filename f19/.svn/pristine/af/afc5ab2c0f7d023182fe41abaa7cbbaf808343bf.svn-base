#include <stdbool.h>
#include <stdint.h>
#include "lib/bitarray.h"
#include "lib/contracts.h"



/* Get a new bitarray with everything set to 'false' */
bitarray bitarray_new() {
  return (bitarray)0;
}

/* Get the ith bit of the bitarray n */
bool bitarray_get(bitarray n, uint8_t i) // 0 <= i < BITARRAY_LIMIT
{
  REQUIRES(i < BITARRAY_LIMIT);
  return ((n >> i) & 1) == 1;
}

/* Toggle the ith bit of the bitarray n, returning a new bitarray */
/* The old bitarray remains unchanged (this is a persistent data structure) */
bitarray bitarray_flip(bitarray n, uint8_t i) // 0 <= i < BITARRAY_LIMIT
{
  REQUIRES(i < BITARRAY_LIMIT);
  return n ^ (1 << i);
}

