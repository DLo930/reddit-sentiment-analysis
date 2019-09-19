#include <stdlib.h>
#include <stdio.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"

int main() {
  int* A = xmalloc(sizeof(int) * 10);
  int* B = A+3;
  for (int i = 0 ; i < 10 ; i++) {
    ASSERT(0 <= i);
    A[i] = i;
  }
  free(A);
  printf("B: %d\n", *B);
  return 0;
}
