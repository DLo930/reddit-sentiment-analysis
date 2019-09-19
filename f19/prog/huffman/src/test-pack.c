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

#include "lib/file_io.h"
#include "lib/xalloc.h"
#include "lib/contracts.h"

#include "freqtable.h"
#include "htree.h"
#include "bitpacking.h"

/* Copied from solution file */
// Pack up to 8 binary digits into a byte
uint8_t _our_pack_byte(bit_t *bits, unsigned int max) {
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
uint8_t* _our_pack(bit_t *bits) {
  REQUIRES(is_bitstring(bits));
  unsigned int len = strlen(bits);
  uint8_t *bytes = xcalloc(num_padded_bytes(len), sizeof(uint8_t));

  for (unsigned int i = 0; 8*i < len; i++)
    bytes[i] = _our_pack_byte(bits + 8*i, len - 8*i);

  return bytes;
}


// unpack an 8-bit byte in bit string tgt
void _our_unpack_byte(uint8_t c, bit_t *tgt) {
  REQUIRES(tgt != NULL);
  for (uint8_t i = 0; i < 8; i++) {
    uint8_t bit = (c >> i) & 0x1;
    tgt[7-i] = bit == 1 ? '1' : '0';  // Bits are reversed
  }
}

// Unpack an array of bytes c of length len into a NUL-terminated string of ASCII bits
bit_t* _our_unpack(uint8_t *c, size_t len) {
  REQUIRES(c != NULL);
  bit_t *s = xcalloc(8 * len + 1, sizeof(bit_t));
  for (unsigned int i = 0; i < len; i++) {
    _our_unpack_byte(c[i], s + 8*i);
  }
  s[8 * len] = '\0';
  ENSURES(s != NULL);
  return s;
}
/* End solution code */

// where to draw bits from
bit_t *bit_source;
symbol_t *byte_source;


size_t silly_hash(char *s) {
  size_t len = strlen(s);
  size_t n = 0;
  for (size_t i = 0; i < len; i++)
    n += (size_t)s[i];
  return n;
}

// Test n bits at a pseudorandom position in bit_source
bool test_pack_on_bits(size_t n, char *test) {
  bit_t *bits = xcalloc(n+1, sizeof(bit_t));
  strncpy(bits, bit_source + silly_hash(test), n);
  char *theirs = (char *)pack(bits);
  char *ours   = (char *)_our_pack(bits);
  bool outcome = (strncmp(ours, theirs, num_padded_bytes(strlen(bits))) == 0);
  free(bits);  free(theirs);  free(ours);
  return outcome;
}

// Tests bits from a binascii file
bool test_pack_on_file(char *fname) {
  size_t max;
  bit_t *bits = read_file_to_char_array(fname, &max);
  char *theirs = (char *)pack(bits);
  char *ours   = (char *)_our_pack(bits);
  bool outcome = (strncmp(ours, theirs, num_padded_bytes(strlen(bits))) == 0);
  free(bits);  free(theirs);  free(ours);
  return outcome;
}

// Test n bytes at a pseudorandom position in byte_source
bool test_unpack_on_bytes(size_t n, char *test) {
  symbol_t *bytes = xcalloc(n, sizeof(symbol_t));
  strncpy((char *)bytes, (char *)byte_source + silly_hash(test), n);
  char *theirs = (char *)unpack(bytes, n);
  char *ours   = (char *)_our_unpack(bytes, n);
  bool outcome = (strncmp(ours, theirs, 8*n) == 0);
  free(bytes);  free(theirs);  free(ours);
  return outcome;
}

// Tests bytes from a binascii file
bool test_unpack_on_file(char *fname) {
  size_t size;
  symbol_t *bytes = read_file_to_byte_array(fname, &size);
  char *theirs = (char *)unpack(bytes, size);
  char *ours   = (char *)_our_unpack(bytes, size);
  size_t len = strlen(theirs);
  bool outcome = (len == strlen(ours) &&
                  strncmp(ours, theirs, len) == 0);
  free(bytes);  free(theirs);  free(ours);
  return outcome;
}


int main (int argc, char **argv) {
  if (argc != 2) {
    printf("Need 1 argument to run, got %d", argc);
    exit(1);
  }

  // Where to draw bits from for pack
  size_t bit_max;
  char *bit_file = "data/binascii/sonnets.01";
  bit_source = read_file_to_char_array(bit_file, &bit_max);

  // Where to draw bytes from for unpack
  size_t byte_max;
  char *byte_file = "data/compressed/sonnets.txt.hip";
  byte_source = read_file_to_byte_array(byte_file, &byte_max);


  // pack

  if (strcmp(argv[1], "pack-0-bits") == 0) {
    assert(test_pack_on_bits(0, argv[1]));
    }
  else if (strcmp(argv[1], "pack-1-bit") == 0) {
    assert(test_pack_on_bits(1, argv[1]));
    }
  else if (strcmp(argv[1], "pack-4-bits") == 0) {
    assert(test_pack_on_bits(4, argv[1]));
    }
  else if (strcmp(argv[1], "pack-7-bits") == 0) {
    assert(test_pack_on_bits(7, argv[1]));
    }
  else if (strcmp(argv[1], "pack-8-bits") == 0) {
    assert(test_pack_on_bits(8, argv[1]));
    }
  else if (strcmp(argv[1], "pack-9-bits") == 0) {
    assert(test_pack_on_bits(9, argv[1]));
    }
  else if (strcmp(argv[1], "pack-many-bits") == 0) {
    for (size_t i = 0; i < 100000; i = 1 + i*i)
      assert(test_pack_on_bits(i, argv[1]));
    }

  else if (strcmp(argv[1], "pack-free-coffee") == 0) {
    assert(test_pack_on_file("data/binascii/free_coffee.01"));
  }
  else if (strcmp(argv[1], "pack-nobody") == 0) {
    assert(test_pack_on_file("data/binascii/nobody.01"));
  }
  else if (strcmp(argv[1], "pack-sonnets") == 0) {
    assert(test_pack_on_file("data/binascii/sonnets.01"));
    }

  // unpack
  else if (strcmp(argv[1], "unpack-0-bytes") == 0) {
    assert(test_unpack_on_bytes(0, argv[1]));
    }
  else if (strcmp(argv[1], "unpack-1-byte") == 0) {
    assert(test_unpack_on_bytes(1, argv[1]));
    }
  else if (strcmp(argv[1], "unpack-4-bytes") == 0) {
    assert(test_unpack_on_bytes(4, argv[1]));
    }
  else if (strcmp(argv[1], "unpack-7-bytes") == 0) {
    assert(test_unpack_on_bytes(7, argv[1]));
    }
  else if (strcmp(argv[1], "unpack-8-bytes") == 0) {
    assert(test_unpack_on_bytes(8, argv[1]));
    }
  else if (strcmp(argv[1], "unpack-9-bytes") == 0) {
    assert(test_unpack_on_bytes(9, argv[1]));
    }
  else if (strcmp(argv[1], "unpack-many-bytes") == 0) {
    for (size_t i = 0; i < 100000; i = 1 + i*i)
      assert(test_unpack_on_bytes(i, argv[1]));
    }

  else if (strcmp(argv[1], "unpack-free-coffee") == 0) {
    assert(test_unpack_on_file("data/compressed/free_coffee.txt.hip"));
  }
  else if (strcmp(argv[1], "unpack-nobody") == 0) {
    assert(test_unpack_on_file("data/source/nobody.jpg"));
  }
  else if (strcmp(argv[1], "unpack-sonnets") == 0) {
    assert(test_unpack_on_file("data/source/sonnets.txt"));
  }
  else if (strcmp(argv[1], "unpack-sonnets-bin") == 0) {
    assert(test_unpack_on_file("data/binascii/sonnets.01"));
  }
  else if (strcmp(argv[1], "unpack-shakespeare") == 0) {
    assert(test_unpack_on_file("data/freq/shakespeare.frq"));
  }


  else {
    printf("Unknown option %s", argv[1]);
    exit(1);
  }

  free(bit_source);
  free(byte_source);
}
