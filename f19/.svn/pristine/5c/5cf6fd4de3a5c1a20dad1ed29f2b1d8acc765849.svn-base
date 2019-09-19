/* Huffman coding
 *
 * 15-122 Principles of Imperative Computation
 */

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <ctype.h>

#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "lib/file_io.h"
#include "lib/heaps.h"

#include "freqtable.h"
#include "htree.h"
#include "encode.h"
#include "bitpacking.h"

// Print error message
void error(char *msg) {
  fprintf(stderr, "%s\n", msg);
  exit(1);
}

/* in htree.h: */
/* typedef struct htree_node htree; */
struct htree_node {
  symbol_t value;
  unsigned int frequency;
  htree *left;
  htree *right;
};

/**********************************************/
/* Task 1: Checking data structure invariants */
/**********************************************/

/* forward declaration */
bool is_htree(htree *H);

bool is_htree_leaf(htree *H) {
  if (!(H != NULL))        return false;
  if (!(H->frequency > 0)) return false;
  if (!(H->left == NULL))  return false;
  if (!(H->right == NULL)) return false;
  return true;
}

bool is_htree_interior(htree *H) {
  if (!(H != NULL)) return false;
  if (!(is_htree(H->left) && is_htree(H->right)))
    return false;
  if (!(H->frequency == H->left->frequency + H->right->frequency))
    return false;
  return true;
}

bool is_htree(htree *H) {
  return is_htree_leaf(H) || is_htree_interior(H);
}


/********************************************************/
/* Task 2: Building Huffman trees from frequency tables */
/********************************************************/

// build leaf of a htree
htree *build_leaf(symbol_t c, unsigned int frequency) {
  htree *H = xmalloc(sizeof(htree));
  H->value = c;
  H->frequency = frequency;
  H->left = NULL;
  H->right = NULL;
  ENSURES(is_htree_leaf(H));
  return H;
}

// build interior node of a htree from children
htree *build_interior(htree *left, htree *right) {
  REQUIRES(is_htree(left) && is_htree(right));
  htree *H = xmalloc(sizeof(htree));
  H->frequency = left->frequency + right->frequency;
  H->left = left;
  H->right = right;
  ENSURES(is_htree_interior(H));
  return H;
}

bool htree_higher_priority(elem e1, elem e2) {
  htree *H1 = (htree *)e1;  REQUIRES(is_htree(H1));
  htree *H2 = (htree *)e2;  REQUIRES(is_htree(H2));
  return H1->frequency < H2->frequency;
}

// build a htree from a frequency table
htree* build_htree(freqtable_t table) {
  REQUIRES(is_freqtable(table));
  pq_t P = pq_new(NUM_SYMBOLS, &htree_higher_priority, NULL);
  /* initialize priority queue */
  int n = 0; // Number of non-zero letters
  for (unsigned short c = 0; c < NUM_SYMBOLS; c++)
    if (table[c] != 0) {
      htree *leaf = build_leaf((symbol_t)c, table[c]);
      pq_add(P, (elem)leaf);
      n++;
    }
  /* build tree, by removing 2 and adding 1 element n-1 times */
  if (n < 2) error("Need at least 2 elements in frequency table\n");
  for (int i = n; i >= 2; i--) {
    /* merge elements with highest priority = lowest frequency */
    htree *min1 = (htree *)pq_rem(P);
    htree *min2 = (htree *)pq_rem(P);
    htree *node = build_interior(min1, min2);
    pq_add(P, (elem)node);
  }
  htree *H = (htree *)pq_rem(P);
  ASSERT(pq_empty(P));
  pq_free(P);			/* free priority queue */
  ENSURES(is_htree_interior(H));
  return H;
}


/*******************************************/
/*  Task 3: decoding a text                */
/*******************************************/

// Decode code according to H, putting decoded length in src_len
symbol_t* decode_src(htree *H, bit_t *code, size_t *src_len) {
  REQUIRES(is_htree_interior(H));
  REQUIRES(is_bitstring(code));

  /* start by determining length of decoded msg */
  size_t len = 0;
  htree *node = H;
  size_t k = 0;

  // Determining code length
  size_t code_len = strlen(code);

  while (k < code_len)
    //@loop_invariant 0 <= k && k <= code_len;
    //@loop_invariant is_htree_interior(node);
    {
      if (code[k] == '0') {
	node = node->left;
	k++;
      } else if (code[k] == '1') {
	node = node->right;
	k++;
      } else if (code[k] == '\0') {
	error("Unexpected end of string");
      } else {
        fprintf(stderr, "Unexpectedly read '%c'(\\%02X): ", code[k], (bit_t)code[k]);
	error("Illegal character in input");
      }
      if (hleaf(node)) { // Reached leaf
	ASSERT(is_htree_leaf(node));
	len++;
	node = H;
      }
    }
  *src_len = len;

  if (!(node == H && k == code_len)) {
    error("Early string termination");
  }
  ASSERT(node == H);

  symbol_t *src = xcalloc(len, sizeof(symbol_t));
  size_t j = 0;
  k = 0;

  while (k < code_len)
    //@loop_invariant 0 <= k && k <= code_len;
    //@loop_invariant is_htree_interior(node);
    {
      if (code[k] == '0') {
	node = node->left;
	k++;
      } else if (code[k] == '1') {
	node = node->right;
	k++;
      }
      if (hleaf(node)) { // Reached leaf
	src[j] = node->value;
	j++;
	node = H;
      }
    }

  return src;
}


/****************************************************/
/* Tasks 4: Building code tables from Huffman trees */
/****************************************************/

// Insert codes in H into table prefixing them with len bits from bits
// returns true if H is a leaf and false otherwise
bool codetable_insert(htree *H, codetable_t table, bit_t *bits, unsigned int len) {
  REQUIRES(is_htree(H));
  REQUIRES(is_bitstring(bits));
  // table may contain no symbol yet

  if (hleaf(H)) {                      // leaf
    table[(symbol_t)H->value] = bits;  // store bitstring code
    return true;                       // true: reached a leaf
  }

  bit_t *str_left = xcalloc(len+2, sizeof(bit_t));
  str_left = strcat(strcpy(str_left, bits), "0");
  if (!codetable_insert(H->left, table, str_left, len+1))
    free(str_left);

  bit_t *str_right = xcalloc(len+2, sizeof(bit_t));
  str_right = strcat(strcpy(str_right, bits), "1");
  if (!codetable_insert(H->right, table, str_right, len+1))
    free(str_right);

  return false;                     // false = bits were only prefix of code
}

// Returns code table for characters in H
codetable_t htree_to_codetable(htree *H) {
  REQUIRES(is_htree(H));
  codetable_t table = xcalloc(NUM_SYMBOLS, sizeof(bitstring_t));
  /* initialized to all NULL */
  codetable_insert(H, table, "", 0);
  ENSURES(is_codetable(table));
  return table;
}


/*******************************************/
/*  Task 5: Encoding a text                */
/*******************************************/

// Compute the number of bits needed to encode string src
size_t encoded_size(codetable_t table, symbol_t *src, size_t src_len) {
  REQUIRES(is_codetable(table));
  REQUIRES(src != NULL);

  size_t code_len = 0;
  for (size_t i = 0; i < src_len; i++) {
    symbol_t c = src[i];
    bitstring_t bits = table[(unsigned int)c];
    if (bits == NULL) {
      fprintf(stderr,
              "Source symbol '%c' (0x%02X) has no associated code\n", c, c);
      exit(1);
    }
    code_len += strlen(bits);
  }
  return code_len;
}

// Encodes source according to codetable
bit_t* encode_src(codetable_t table, symbol_t *src, size_t src_len) {
  REQUIRES(is_codetable(table));
  REQUIRES(src != NULL);

  size_t code_len = encoded_size(table, src, src_len);
  bit_t *code =  xcalloc(code_len + 1, sizeof(bit_t));

  size_t k = 0;			// result index
  for (size_t i = 0; i < src_len; i++)
    //@loop_invariant 0 <= i && i <= src_len;
    {
      symbol_t c = src[i];
      bitstring_t bits = table[(unsigned int) c];
      strcpy(code + k, bits);
      k += strlen(bits);
    }
  ASSERT(k == code_len);
  code[k] = '\0';		// NUL-terminate character array

  ENSURES(is_bitstring(code));
  return code;
}


/**************************************************/
/*  Task 6: Building a frequency table from file  */
/**************************************************/

// Build a frequency table from a source file (or STDIN)
freqtable_t build_freqtable(char *fname) {
  freqtable_t table = xcalloc(NUM_SYMBOLS, sizeof(unsigned int));
  int c;

  FILE *stream = xfopen(fname, "r");
  while ((c = fgetc(stream)) != EOF)
    table[(symbol_t)c]++;
  if (fname != NULL) fclose(stream);

  ENSURES(is_freqtable(table));
  return table;
}


/************************************************/
/*  Task 7: Packing and unpacking a bitstring   */
/************************************************/

// Pack up to 8 binary digits into a byte
uint8_t pack_byte(bit_t *bits, unsigned int max) {
  REQUIRES(is_bitstring(bits));
  uint8_t byte = 0;

  unsigned char i = 0;
  while (i < 8 && i < max) {
    if (bits[i] == '1')
      byte = (byte << 1) | (uint8_t) 0x1;
    else {
      ASSERT(bits[i] == '0');
      byte = byte << 1;
    }
    i++;
  }
  while (i < 8) {
    byte = byte << 1;  // padding with zeros
    i++;
  }
  return byte;
}

// Pack a string of bits into an array of bytes; length = strlen(bits)/8
uint8_t* pack(bit_t *bits) {
  REQUIRES(is_bitstring(bits));
  unsigned int len = strlen(bits);
  uint8_t *bytes = xcalloc(num_padded_bytes(len), sizeof(uint8_t));

  for (unsigned int i = 0; 8*i < len; i++)
    bytes[i] = pack_byte(bits + 8*i, len - 8*i);

  return bytes;
}


// unpack an 8-bit byte in bit string tgt
void unpack_byte(uint8_t c, bit_t *tgt) {
  REQUIRES(tgt != NULL);
  for (uint8_t i = 0; i < 8; i++) {
    uint8_t bit = (c >> i) & 0x1;
    tgt[7-i] = bit == 1 ? '1' : '0';  // Bits are reversed
  }
}

// Unpack an array of bytes c of length len into a NUL-terminated string of ASCII bits
bit_t* unpack(uint8_t *c, size_t len) {
  REQUIRES(c != NULL);
  bit_t *s = xcalloc(8 * len + 1, sizeof(bit_t));
  for (unsigned int i = 0; i < len; i++) {
    unpack_byte(c[i], s + 8*i);
  }
  s[8 * len] = '\0';
  ENSURES(s != NULL);
  return s;
}
