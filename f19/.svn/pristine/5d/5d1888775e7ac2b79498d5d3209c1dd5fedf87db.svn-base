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
    bad_mult_by_2(a);
    printf("%d\n", a);
    mult_by_2(&a);
    printf("%d\n", a);
    return 0;
}
