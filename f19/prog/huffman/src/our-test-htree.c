/* Huffman coding
 *
 * Main file for testing is_htree
 * 15-122 Principles of Imperative Computation
 */

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <ctype.h>

#include "lib/xalloc.h"
#include "lib/contracts.h"

#include "htree.h"

struct htree_node {
  symbol_t value;
  unsigned int frequency;
  htree *left;
  htree *right;
};

bool is_htree(htree *H);
bool is_htree_leaf(htree *H);
bool is_htree_interior(htree *H);

htree* mk_hleaf(symbol_t value, unsigned int freq) {
  htree *H = xmalloc(sizeof(htree));
  H->left = NULL;
  H->right = NULL;
  H->value = value;
  H->frequency = freq;
  return H;
}
htree* mk_hinner(htree *left, htree *right, unsigned int freq) {
  htree *H = xmalloc(sizeof(htree));
  H->left = left;
  H->right = right;
  H->frequency = freq;
  return H;
}

int main (int argc, char **argv) {
  // Write tests for is_tree here

  if (argc != 2) {
    printf("Need 1 argument to run, got %d", argc);
    exit(1);
  }

  // Some simple htrees
  htree *H0 = mk_hleaf('a', 13);
  htree *H1 = mk_hleaf('x', 1);
  htree *H2 = mk_hleaf('y', 15122);
  htree *H3 = mk_hinner(H1, H2, 15123);
  htree *H4 = mk_hinner(H0, H3, 15136);

  htree *X0 = mk_hleaf('w', 0);
  htree *X1 = mk_hleaf('z', 3); X1->left = H1;
  htree *X2 = mk_hleaf('u', 4); X2->right = H2;
  htree *X3 = mk_hinner(H1, H2, 42);
  htree *X4 = mk_hinner(X0, H1, 1);

  if (strcmp(argv[1], "is_htree-edge") == 0) {
      assert(!is_htree_leaf(NULL));
      assert(!is_htree_interior(NULL));
      assert(!is_htree(NULL));
    }

  else if (strcmp(argv[1], "is_htree-bad-leaf1") == 0) {
      assert(!is_htree_leaf(X0));
      assert(!is_htree(X0));
    }
  else if (strcmp(argv[1], "is_htree-bad-leaf2") == 0) {
      assert(!is_htree_leaf(X1));
      assert(!is_htree(X1));
    }
  else if (strcmp(argv[1], "is_htree-bad-leaf3") == 0) {
      assert(!is_htree_leaf(X2));
      assert(!is_htree(X2));
    }
  else if (strcmp(argv[1], "is_htree-bad-leaf4") == 0) {
      assert(!is_htree_leaf(H3));
    }

  else if (strcmp(argv[1], "is_htree-bad-interior1") == 0) {
      assert(!is_htree_interior(X3));
      assert(!is_htree(X3));
    }
  else if (strcmp(argv[1], "is_htree-bad-interior2") == 0) {
      assert(!is_htree_interior(X4));
      assert(!is_htree(X4));
    }

  else if (strcmp(argv[1], "is_htree-good-leaf") == 0) {
      assert(is_htree_leaf(H1));
      assert(is_htree(H1));

      assert(is_htree_leaf(H2));
      assert(is_htree(H2));
    }

  else if (strcmp(argv[1], "is_htree-good-interior") == 0) {
      assert(is_htree_interior(H3));
      assert(is_htree(H3));

      assert(is_htree_interior(H4));
      assert(is_htree(H4));
    }

  else if (strcmp(argv[1], "is_htree-exclusive") == 0) {
    assert(!is_htree_interior(H1));
    assert(!is_htree_interior(H2));
    assert(!is_htree_leaf(H3));
    assert(!is_htree_leaf(H4));
  }

  else if (strcmp(argv[1], "is_htree-free_coffee") == 0) {
    char *fname = "data/htree/free_coffee.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }
  else if (strcmp(argv[1], "is_htree-more_free_coffee") == 0) {
    char *fname = "data/htree/more_free_coffee.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }
  else if (strcmp(argv[1], "is_htree-nobody") == 0) {
    char *fname = "data/htree/nobody.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }

  else if (strcmp(argv[1], "is_htree-more_free_coffee2") == 0) {
    char *fname = "data/htree/more_free_coffeeNL.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }
  else if (strcmp(argv[1], "is_htree-room_for_creme") == 0) {
    char *fname = "data/htree/room_for_cremeNL.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }
  else if (strcmp(argv[1], "is_htree-sonnets") == 0) {
    char *fname = "data/htree/sonnets.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }
  else if (strcmp(argv[1], "is_htree-shakespeare") == 0) {
    char *fname = "data/htree/shakespeare.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }
  else if (strcmp(argv[1], "is_htree-g5") == 0) {
    char *fname = "data/htree/g5.htr";
    htree *H = htree_from_codetable(read_codetable(fname));
    assert(is_htree(H));
  }

  else {
    printf("Unknown option %s", argv[1]);
    exit(1);
  }
}
