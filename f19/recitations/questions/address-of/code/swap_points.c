#include <stdio.h>
#include "lib/contracts.h"
struct point {
  int x;
  int y;
};
void swap_points(struct point* P) {
  REQUIRES(P != NULL);
  int temp = P->x;
  P->x = P->y;
  P->y = temp;
}
int main() {
  struct point A;
  A.x = 122;
  A.y = 15;
  swap_points(&A);
  printf("A: (%d, %d)\n", A.x, A.y);
  return 0;
}
