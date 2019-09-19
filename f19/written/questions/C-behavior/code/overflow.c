#include "lib/contracts.h"

int oadd(int x, int y) {
  int result = x + y;
  if (x > 0 && y > 0) ASSERT(result > 0);
  if (x < 0 && y < 0) ASSERT(result < 0);
  return result;
}

int main() {
  return oadd(0,0);
}
