#include "lib/bitarray.h"
#include "lib/contracts.h"
#include <stdio.h>

bitarray bitarray_new()
{
  uint32_t result = 0;

  return result;
}

bool bitarray_get(bitarray n, uint8_t i)
{
  REQUIRES(i < BITARRAY_LIMIT);

  bool result = ((n >> (BITARRAY_LIMIT - i - 1)) & 0x1);

  ENSURES(result == 0 || result == 1);
  return result;
}

bitarray bitarray_flip(bitarray n, uint8_t i)
{
  REQUIRES(i < BITARRAY_LIMIT);

  bitarray result = n;

  uint32_t mask = 1 << (BITARRAY_LIMIT - i - 1);

  if (bitarray_get(n,i) == true)
  {

    mask = mask ^ ((uint32_t)(-1));

    result = result & mask;

  } else {

    result = result | mask;

  }

  ENSURES(result != n);

  return result;
}
