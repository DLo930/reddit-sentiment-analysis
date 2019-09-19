/* Huffman coding
 *
 * Main file for testing
 * 15-122 Principles of Imperative Computation, Fall 2012
 */

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

#include "freqtable.h"
#include "huffman.h"

/* next line is well-know to be bad style
 * don't want to worry about separate compilation
 * and interfaces for this version of the code
 */

#include "_huffman.c"

htree* _load (char *filename)
//@ensures _is_htree(\result);
{
  freqtable F = read_freqtable(filename);
  htree *H = _build_htree(F);
  freqtable_free(F);
  return H;
}

htree* load (char *filename)
{
  freqtable F = read_freqtable(filename);
  htree *H = build_htree(F);
  freqtable_free(F);
  return H;
}

bool _roundtrip(htree *H, char *msg, htree *_H) {
  // printf("msg: \"%s\"\n", msg);
  char *bits = _encode(H, msg);
  // printf("bits: \"%s\"\n", bits);
  char *_bits = _encode(_H, msg);
  // printf("_bits: \"%s\"\n", bits);
  char *decoded = _decode(H, bits);
  // printf("decoded: \"%s\"\n", decoded);
  bool result = (strcmp(decoded, msg) == 0 /* correct */
		 && strlen(bits) == strlen(_bits)); /* and optimal */
  free(bits);
  free(_bits);
  free(decoded);
  return result;
}

/* Task 5 */
/* testing build_htree in C */
int task5 () {
  htree *B = load("inputs/binary.txt");
  assert(_is_htree(B));

  htree *_B = _load("inputs/binary.txt");

  /* for binary alphabet, output length should be equal input length */
  assert(_roundtrip(B, "", _B));
  assert(_roundtrip(B, "a", _B));
  assert(_roundtrip(B, "b", _B));
  assert(_roundtrip(B, "aa", _B));
  assert(_roundtrip(B, "ab", _B));
  assert(_roundtrip(B, "ba", _B));
  assert(_roundtrip(B, "bb", _B));
  assert(_roundtrip(B, "aaa", _B));
  assert(_roundtrip(B, "aab", _B));
  assert(_roundtrip(B, "aba", _B));
  assert(_roundtrip(B, "abb", _B));
  assert(_roundtrip(B, "baa", _B));
  assert(_roundtrip(B, "bab", _B));
  assert(_roundtrip(B, "bba", _B));
  assert(_roundtrip(B, "bbb", _B));

  htree_free(B);
  htree_free(_B);

  htree *E = load("inputs/english.txt");
  assert(_is_htree(E));

  htree *_E = _load("inputs/english.txt");

  assert(_roundtrip(E, "thequickbrownfoxjumpsoverthelazydog", _E));
  assert(_roundtrip(E, "", _E));
  assert(_roundtrip(E, "abcdefghijklmnopqrstuvwxyz", _E));
  assert(_roundtrip(E, "zyxwvutsrqponmlkjihgfedcba", _E));
  assert(_roundtrip(E, "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba", _E));

  htree_free(E);
  htree_free(_E);

  htree *A = load("inputs/ascii.txt");
  assert(_is_htree(A));

  htree *_A = load("inputs/ascii.txt");

  assert(_roundtrip(A, "We are all in this together!  Gaming Autolab (fun though it may be) doesn't really answer the question: \"How do we write good code?\"", _A));

  htree_free(A);
  htree_free(_A);

  return 0;
}

int task5a () {
  /* this should call exit(1) */
  htree *S = load("inputs/singleton.txt");
  (void)S;
  return 0;
}

int task5b () {
  /* this should abort() */
  htree *S = build_htree(NULL);
  (void)S;
  return 0;
}

/* bonus */
bool encode_eq(htree *_H, char *msg)
{
  char *_bits = _encode(_H, msg);
  char *bits = encode(_H, msg);
  bool result = (strcmp(_bits, bits) == 0);
  free(_bits);
  free(bits);
  return result;
}

int bonus () {
  htree *_B = _load("inputs/binary.txt");
  assert(encode_eq(_B, ""));
  assert(encode_eq(_B, "a"));
  assert(encode_eq(_B, "b"));
  assert(encode_eq(_B, "aa"));
  assert(encode_eq(_B, "ab"));
  assert(encode_eq(_B, "ba"));
  assert(encode_eq(_B, "bb"));
  assert(encode_eq(_B, "aaa"));
  assert(encode_eq(_B, "aab"));
  assert(encode_eq(_B, "aba"));
  assert(encode_eq(_B, "abb"));
  assert(encode_eq(_B, "baa"));
  assert(encode_eq(_B, "bab"));
  assert(encode_eq(_B, "bba"));
  assert(encode_eq(_B, "bbb"));
  htree_free(_B);

  htree *_E = _load("inputs/english.txt");
  assert(encode_eq(_E, "thequickbrowndogjumpsoverthelazyfox"));
  assert(encode_eq(_E, ""));
  assert(encode_eq(_E, "abcdefghijklmnopqrstuvwxyz"));
  assert(encode_eq(_E, "zyxwvutsrqponmlkjihgfedcba"));
  assert(encode_eq(_E, "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"));
  htree_free(_E);

  htree *_A = _load("inputs/ascii.txt");
  assert(encode_eq(_A, "Ask not what your TA can do for you---ask what you can do for your TA."));
  htree_free(_A);

  return 0;
}

int bonus_a() {
  htree *_S = _build0('a', 1);
  /* should fail contract */
  encode(_S, "aaa");
  return 0;
}

int bonus_b() {
  htree *_E = _build_htree(read_freqtable("inputs/english.txt"));
  /* should generate error since '?' is an illegal character */
  encode(_E, "whatisthisquestionmarkdoinghere?");
  return 0;
}

int c0_main (int argc, char **argv) {

  if (argc != 2) {
    fprintf(stderr, "Must pass task number on command line\n");
    return 2;
  }
  char *cmd = argv[1];
  if (strcmp(cmd, "task5") == 0)
    return task5();
  else if (strcmp(cmd, "task5a") == 0)
    return task5a();
  else if (strcmp(cmd, "task5b") == 0)
    return task5b();
  else if (strcmp(cmd, "bonus") == 0)
    return bonus();
  else if (strcmp(cmd, "bonus_a") == 0)
    return bonus_a();
  else if (strcmp(cmd, "bonus_b") == 0)
    return bonus_b();
  else {
    fprintf(stderr, "Task not recognized\n");
    return 2;
  }

  return 0;
}
