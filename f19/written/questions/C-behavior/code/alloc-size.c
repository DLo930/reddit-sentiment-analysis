#include <stdlib.h>
#include "lib/xalloc.h"

int main() {
  int *A = xmalloc(100);
  for (int i=0; i<100; i++)
    *(A+i) = i*i;
  free(A);
  return 0;
}
