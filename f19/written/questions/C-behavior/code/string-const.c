#include <stdio.h>
int main() {
  char* s = "1 is the loneliest number";
  printf("s: %s\n", s);
  *s = '0';
  printf("s: %s\n", s);
  return 0;
}
