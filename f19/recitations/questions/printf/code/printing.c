#include <stdio.h>   // this lets us use the printf function

int main() {
  int x = 64;
  printf("%d\n", x); // decimal (can also use %i)
  printf("%x\n", x); // hexadecimal
  char a = 'd';      // single quotes!
  printf("%c\n", a);
  printf("%d\n", a);
  char* s = "hello"; // double quotes!
  printf("%s\n", s);
  void* p = (void*)0xdeadbeef;
  printf("%p\n", p); // must be a void*, not any other pointer type
  size_t z = 8;
  printf("%zu\n", z);
}
