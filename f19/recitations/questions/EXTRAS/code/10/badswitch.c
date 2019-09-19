#include <stdio.h>
#include <stdlib.h>
int main(int argc, char** argv) {
    if (argc > 1) {
        int a = atoi(argv[1]);
        switch (a % 2) {
            case 0:
                printf("x is even!\n");
            default:
                printf("x is odd!\n");
        }
    }
    return 0;
}
