#include <stdio.h>
#define MULT(X,Y) (X*Y)
int main() {
  int c = MULT(3+4,4+5);
  printf("(3+4)*(4+5) is = %d\n", c);
  return 0;
}
