#include <stdlib.h>
#include <stdio.h>
#include "lib/xalloc.h"

int main() {
  int* A = xmalloc(sizeof(int) * 32);
  for (int i = 0 ; i < 32 ; i++) {
    A[i] = i + 4;
  }
  int* B;
  for (B = A; *B != 0; B++) {
    printf("A[i]: %d\n", *B);
  }
  free(B);
  return 0;
}
