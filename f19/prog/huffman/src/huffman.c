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

/* forward declaration -- DO NOT MODIFY */
bool is_htree(htree *H);

bool is_htree_leaf(htree *H) {
  // WRITE ME
  (void)H;       // bogus
  return true;  // bogus
}

bool is_htree_interior(htree *H) {
  // WRITE ME
  (void)H;       // bogus
  return true;  // bogus
}

bool is_htree(htree *H) {
  // WRITE ME
  (void)H;       // bogus
  return false;  // bogus
}


/********************************************************/
/* Task 2: Building Huffman trees from frequency tables */
/********************************************************/

/* for libs/heaps.c */
bool htree_higher_priority(elem e1, elem e2) {
  // WRITE ME
  (void)e1;     // bogus
  (void)e2;     // bogus
  return false; // bogus
}

// build a htree from a frequency table
htree* build_htree(freqtable_t table) {
  // WRITE ME
  (void)table; // bogus
  return NULL; // bogus
}


/*******************************************/
/*  Task 3: decoding a text                */
/*******************************************/

// Decode code according to H, putting decoded length in src_len
symbol_t* decode_src(htree *H, bit_t *code, size_t *src_len) {
  // WRITE ME
  (void)H; (void)code; (void)src_len; // bogus
  return NULL; // bogus
}


/****************************************************/
/* Tasks 4: Building code tables from Huffman trees */
/****************************************************/

// Returns code table for characters in H
codetable_t htree_to_codetable(htree *H) {
  // WRITE ME
  (void)H;     // bogus
  return NULL; // bogus
}


/*******************************************/
/*  Task 5: Encoding a text                */
/*******************************************/

// Encodes source according to codetable
bit_t* encode_src(codetable_t table, symbol_t *src, size_t src_len) {
  // WRITE ME
  (void)table; (void)src; (void)src_len; // bogus
  return NULL; // bogus
}


/**************************************************/
/*  Task 6: Building a frequency table from file  */
/**************************************************/

// Build a frequency table from a source file (or STDIN)
freqtable_t build_freqtable(char *fname) {
  // WRITE ME
  (void)fname; // bogus
  return NULL; // bogus
}



/************************************************/
/*  Task 7: Packing and unpacking a bitstring   */
/************************************************/

// Pack a string of bits into an array of bytes; length = strlen(bits)/8
uint8_t* pack(bit_t *bits) {
  // WRITE ME
  (void)bits;  // bogus
  return NULL; // bogus
}

// Unpack an array of bytes c of length len into a NUL-terminated string of ASCII bits
bit_t* unpack(uint8_t *c, size_t len) {
  // WRITE ME
  (void)c; (void)len;  // bogus
  return NULL;         // bogus
}
