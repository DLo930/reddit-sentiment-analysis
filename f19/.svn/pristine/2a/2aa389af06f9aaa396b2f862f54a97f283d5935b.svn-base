#include <stdlib.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"

int main() {
  int* A = xmalloc(sizeof(int) * 10);
  for (int i = 1 ; i < 10 ; i++) {
    ASSERT(1 <= i);
    *(A + i) = i;
  }
  free(A+1);
  return 0;
}
