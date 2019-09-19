#include <stdbool.h>
#include "lib/bitvector.h"
#include "lib/contracts.h"
#include "lib/xalloc.h"

bitvector bitvector_new() {
  bitvector V = xcalloc(BITVECTOR_LIMIT, sizeof(char));
  return V;  
}

bool bitvector_get(bitvector B, uint8_t i) {
  return B ? B[i] : false;  
}

bitvector bitvector_flip(bitvector B, uint8_t i) {
  bitvector R = xcalloc(BITVECTOR_LIMIT, sizeof(char));
  if (B) {
    for (size_t j = 0; j < BITVECTOR_LIMIT; j++) {
      R[j] = B[j];
    }
  }
  
  R[i] = !R[i];

  return R;
}

bool bitvector_equal(bitvector B1, bitvector B2) {
  for (size_t j = 0; j < BITVECTOR_LIMIT; j++) {
    if (bitvector_get(B1, j) != bitvector_get(B2, j)) return false;
  }
  return true;
}
