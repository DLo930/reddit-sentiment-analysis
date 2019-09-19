#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"

struct point {
    int x;
    int y;
  };

void increment(int *p) {
  REQUIRES(p != NULL);
  *p = *p + 1;
}

int main() {

  // Arrays and pointer arithmetic

  A[1] = 7;
  A[2] = A[1] + 5;
  A[4] = 1;

  for (int i=0; i < 5; i++)
    printf("A[%d] is %d\n", i, A[i]);

  //printf("A[...] is %d\n", A[...]);


  // Aliasing
  /*
  int *B = ...

  */


  // Pointer casting
  /*
  char *C = ...
  printf("The 16th char in C is %d\n", C[16]);

  struct point *D = ...
  printf("(x1,y1) = (%d, %d)\n", D[0].x, D[0].y);
  printf("(x2,y2) = (%d, %d)\n", D[1].x, D[1].y);

  // thermonuclear_device_controller *danger = ...
  */


  // Stack-allocated arrays
  /*
  int n = 10;
  int E[n];
  for (int i=0; i<n; i++)
    E[i] = i*i;
  (void)E;

  int F[] = {2, 4, 56, 8, 3};
  (void)F;
  */


  // Stack-allocated structs
  /*
  struct point p;
  p.x = 3;
  p.y = 7;
  printf("p is (%d,%d)\n", p.x, p.y);
  */


  // Strings
  /*
  char *s1 = "hello";                                   // Text-allocated (read-only)
  char *s2 = xmalloc((strlen(s1)) * sizeof(char));  // ?? Heap-allocated
  char s3[] = "world";                                  // Stack-allocated
  char s4[] = {'f', 'i', 'n', 'e'};                 // ?? Stack-allocated
  // s1[0] = 'm';                                       // Writing to read-only memory
  printf("s1 is %c%c%c%c%c\n", s1[0], s1[1], s1[2], s1[3], s1[4]);
  printf("s1 is also %s\n", s1);
  strcpy(s2, s1);
  s2[0] = 'Y';
  printf("%s became %s\n", s1, s2);
  s3[2] = 'u';
  printf("%s %s\n", s4, s3);
  free(s1);                     // ??
  free(s2);                     // ??
  free(s3);                     // ??
  free(s4);                     // ??
  */


  // Address-of
  /*
  int i = 42;
  increment(...);
  printf("i = %d\n", i);

  increment(...);
  printf("p is (%d,%d)\n", p.x, p.y);

  struct point* p2 = xcalloc(1, sizeof(struct point));
  // increment(...);
  printf("p2 is (%d,%d)\n", p2->x, p2->y);

  increment(&A[3]);
  printf("A[3] is now %d\n", A[3]);
  */

  // something about A;
}
