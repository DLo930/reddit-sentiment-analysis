#include <stdio.h>
#include "lib/contracts.h"

void bad_mult_by_2(int x) {
    x = x * 2;
}

void mult_by_2(int* x) {
    REQUIRES(x != NULL);
    *x = *x * 2;
}

int main () {
   int a = 4;
   int b = 4;
   bad_mult_by_2(a);
   mult_by_2(&b);
   printf("a: %d   b: %d\n", a, b);
   return 0;
}
