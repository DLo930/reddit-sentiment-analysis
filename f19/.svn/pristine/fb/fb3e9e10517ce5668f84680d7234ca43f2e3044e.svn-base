#include <stdlib.h>
#include "lib/xalloc.h"

int main() {
  int* A = xmalloc(sizeof(int) * 12);
  int* B = A;
  for (int i = 0 ; i < 12 ; i++) {
    A[i] = i;
  }
  free(A);
  for (int i = 1 ; i < 12 ; i++) {
    B[i] = B[i] + B[i-1];
  }
  free(B);
  return 0;
}
