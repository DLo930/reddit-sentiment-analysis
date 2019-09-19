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

/*
// Used to be legal, now doesn't compile
int *bad() {
  int a = 1;
  return &a;
}
*/

int main() {

  // Arrays and pointer arithmetic
//  int *A = xmalloc(sizeof(int) * 5);  // Does not initialize array
  int *A = xcalloc(5, sizeof(int));     // Initializes array

  A[1] = 7;
  *(A+2) = *(A+1) + 5;
  *A = 42;
  A[3] = *A - 5;
  4[A] = 257;

  for (int i=0; i < 5; i++)
    printf("A[%d] is %d\n", i, A[i]);

  //printf("A[...] is %d\n", A[5]);         // Out of bounds read  (V)
  //printf("A[...] is %d\n", A[1000]);      // Out of bounds read  (V)
  //printf("A[...] is %d\n", A[-1]);        // Out of bounds read  (V)

  //printf("A[...] is %d\n", A[10000000]);  // segfault            (V!)

  //A[5] = 15122;                           // Out of bounds write (V)
  //printf("A[...] is %d\n", A[5]);         // Out of bounds read  (V)

  //A[1000] = 42;                           // Out of bounds write (no V!)
  //printf("A[...] is %d\n", A[1000]);      // Out of bounds read  (V)


  // Aliasing
  int *B = A + 2;
  assert(B[0] == A[2]);
  assert(B[1] == A[3]);
  assert(B + 1 == A + 3);
  assert(*(B + 2) == A[4]);
  B[1] = 35;
  assert(A[3] == 35);
  // free(B);                               // Unallocated memory!


  // Pointer casting
  char *C = (char *)A;
  printf("The 16th char in C is %d\n", C[16]);
  struct point *D = (struct point *)(A + 2);
  printf("(x0,y0) = (%d, %d)\n", D[0].x, D[0].y);
  //printf("(x1,y1) = (%d, %d)\n", D[1].x, D[1].y);  // Out of bound read

  //thermonuclear_device_controller *danger = (thermonuclear_device_controller *)A; // !!!!


  // Stack-allocated arrays
  int n = 10;
  int E[n];
  for (int i=0; i<n; i++)
    E[i] = i*i;
  (void)E;

  int F[] = {2, 4, 56, 8, 3};
  (void)F;


  // Stack-allocated structs
  struct point p;
  p.x = 3;
  p.y = 7;
  printf("p is (%d,%d)\n", p.x, p.y);


  // Strings
  char *s1 = "hello";                                   // Text-allocated (read-only)
  char *s2 = xmalloc((strlen(s1) + 1) * sizeof(char));  // Heap-allocated
  char s3[] = "world";                                  // Stack-allocated
  char s4[] = {'f', 'i', 'n', 'e', '\0'};               // Stack-allocated
  // s1[0] = 'm';                                       // Writing to read-only memory
  printf("s1 is %c%c%c%c%c\n", s1[0], s1[1], s1[2], s1[3], s1[4]);
  printf("s1 is also %s\n", s1);
  strcpy(s2, s1);
  s2[0] = 'Y';
  printf("%s became %s\n", s1, s2);
  s3[2] = 'u';
  printf("%s %s\n", s4, s3);
  free(s2);


  // Address-of
  int i = 42;
  increment(&i);
  printf("i = %d\n", i);

  increment(&p.y);                           // p was stack-allocated
  printf("p is (%d,%d)\n", p.x, p.y);

  struct point* p2 = xcalloc(1, sizeof(struct point));
  increment(&(p2->y));                      // p2 is heap-allocated
  printf("p2 is (%d,%d)\n", p2->x, p2->y);

  increment(&A[3]);
  printf("A[3] is now %d\n", A[3]);

  free(A);
}
