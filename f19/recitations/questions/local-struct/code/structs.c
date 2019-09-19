#include <stdio.h>

struct point {
    int x;
    char y;
};
int main () {
    struct point a;
    a.x = 3;
    a.y = 'c';
    struct point b = a;
    b.x = 4;
    printf("a.x, a.y: %d, %c\n", a.x, a.y); // what gets printed out here?
    printf("b.x, b.y: %d, %c\n", b.x, b.y); // how about here?
}
