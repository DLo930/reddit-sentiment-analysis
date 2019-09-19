#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <limits.h>
#include <string.h>
#include <float.h>
#include <math.h>

#include "lib/xalloc.h"
#include "lib/contracts.h"

#define PI 3.14159265

typedef struct ltree leafytree;
struct ltree {
  unsigned leafcount;  // number of leaves
  int type;            // 0=empty, 1=leaf, 2=inner
  int data;            // data in leaves
  leafytree *left;     // subtrees in inner nodes
  leafytree *right;
};

bool is_tree(leafytree *T) {
  if (T == NULL) return false;

  switch (T->type) {
  case 0:
    return T->leafcount == 0;
    // No need for break since we return

  case 1:
    return T->leafcount == 1;

  case 2:
    (void)0;   // Empty statement to make the compiler happy
    leafytree *L = T->left;
    leafytree *R = T->right;
    return is_tree(L) && is_tree(R)
        && T->leafcount == L->leafcount + R->leafcount;

  default:  // Not needed, but makes the compiler happy
    return false;
  }
}

leafytree *mk_empty() { // Make an empty node
  leafytree *T = xmalloc(sizeof(leafytree));
  T->type = 0;
  T->leafcount = 0;
  ASSERT(is_tree(T));
  return T;
}
leafytree *mk_leaf(int data) { // Make a leaf node
  leafytree *T = malloc(sizeof(leafytree));
  T->type = 1;
  T->leafcount = 1;
  T->data = data;
  ASSERT(is_tree(T));
  return T;
}
// Make an inner node
leafytree *mk_inner(leafytree *T_left, leafytree *T_right) {
  ASSERT(is_tree(T_left) && is_tree(T_right));
  leafytree *T = malloc(sizeof(leafytree));
  T->type = 2;
  T->leafcount = T_left->leafcount + T_right->leafcount;
  T->left  = T_left;
  T->right = T_right;
  ASSERT(is_tree(T));
  return T;
}

// Add all the data in a tree
int add_tree(leafytree *T) {
  ASSERT(is_tree(T));
  int n = 0;
  switch (T->type) {
  case 2:
    n += add_tree(T->left);
    n += add_tree(T->right);
    break;

  case 1:
    n = T->data;
    break;

  default:
    n = 0;
  }

  return n;
}


int main () {

  // Floats

  //  for (float res = 0.0; res != 5.0; res += 0.1) {
  //    printf("res = %f\n", res);
  //  }


  // Enums, unions, and switch
  leafytree *T0 = mk_empty();
  leafytree *T1 = mk_leaf(42);
  leafytree *T2 = mk_inner(T0, T1);
  printf("add_tree(T) = %d\n", add_tree(T2));

  printf("\n");
}
