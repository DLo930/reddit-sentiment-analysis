#include <stdlib.h>
#include <stdio.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"

int main() {
  int* A = xmalloc(sizeof(int) * 10);
  printf("Before: %d\n", A[0]);
  for (int i = 0 ; i < 10 ; i++) {
    ASSERT(0 <= i);
    A[i] = i;
  }
  printf("After: %d\n", A[0]);
  free(A);
  return 0;
}
