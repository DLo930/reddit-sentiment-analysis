#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "lib/xalloc.h"
#include "lib/bitvector.h"
#include "board-ht.h"

int c0_main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "Wrong number of args\n");
    exit(1);
  }

  char *cmd = argv[1];

  bitvector bitvector_full = bitvector_new();
  for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) 
    bitvector_full = bitvector_flip(bitvector_full, i);

  if (strcmp(cmd, "createdestroy") == 0) {
    hdict_t H = ht_new(1);
    hdict_free(H);
    H = ht_new(1000);
    hdict_free(H);

  } else if (strcmp(cmd, "lookup_empty") == 0) {
    hdict_t H = ht_new(10);

    if (NULL != ht_lookup(H, bitvector_new())) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      if (NULL != ht_lookup(H, bitvector_flip(bitvector_new(), i))) return 1;
    }
    if (NULL != ht_lookup(H, bitvector_full)) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      if (NULL != ht_lookup(H, bitvector_flip(bitvector_full, i))) return 1;
    }

    hdict_free(H);

  } else if (strcmp(cmd, "add_one_lookup") == 0) {
    hdict_t H = ht_new(10);
    struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
    DAT->board = bitvector_new();
    DAT->test = 12;
    ht_insert(H, DAT);

    if (DAT != ht_lookup(H, DAT->board)) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      if (NULL != ht_lookup(H, bitvector_flip(bitvector_new(), i))) return 1;
    }
    if (NULL != ht_lookup(H, bitvector_full)) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      if (NULL != ht_lookup(H, bitvector_flip(bitvector_full, i))) return 1;
    }

    hdict_free(H);

  } else if (strcmp(cmd, "add_two_lookup") == 0) {
    hdict_t H = ht_new(10);

    struct board_data *DAT1 = xcalloc(1,sizeof(struct board_data));
    DAT1->board = bitvector_new();
    DAT1->test = 12;

    struct board_data *DAT2 = xcalloc(1,sizeof(struct board_data));
    DAT2->board = bitvector_full;
    DAT2->test = 4;

    ht_insert(H, DAT1);
    ht_insert(H, DAT2);

    if (DAT1 != ht_lookup(H, bitvector_new())) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      if (NULL != ht_lookup(H, bitvector_flip(bitvector_new(), i))) return 1;
    }
    if (DAT2 != ht_lookup(H, bitvector_full)) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      if (NULL != ht_lookup(H, bitvector_flip(bitvector_full, i))) return 1;
    }

    hdict_free(H);
    
  } else if (strcmp(cmd, "add_many") == 0) {
    hdict_t H = ht_new(10);

    struct board_data *DAT1 = xcalloc(1,sizeof(struct board_data));
    DAT1->board = bitvector_new();
    DAT1->test = 101;
    ht_insert(H, DAT1);

    struct board_data *DAT2 = xcalloc(1,sizeof(struct board_data));
    DAT2->board = bitvector_full;
    DAT2->test = 104;
    ht_insert(H, DAT2);

    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
      DAT->board = bitvector_flip(bitvector_new(), i);
      DAT->test = i;
      ht_insert(H, DAT);
    }

    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
      DAT->board = bitvector_flip(bitvector_full, i);
      DAT->test = 200 - i;
      ht_insert(H, DAT);
    }

    if (DAT1 != ht_lookup(H, bitvector_new())) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = ht_lookup(H, bitvector_flip(bitvector_new(), i));
      if (DAT == NULL) return 1;
      if (DAT->test != i) return 1;
    }
    if (DAT2 != ht_lookup(H, bitvector_full)) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = ht_lookup(H, bitvector_flip(bitvector_full, i));
      if (DAT == NULL) return 1;
      if (DAT->test != 200 - i) return 1;
    }

    hdict_free(H);

    
  } else if (strcmp(cmd, "add_many_change_test") == 0) {
    hdict_t H = ht_new(10);

    struct board_data *DAT1 = xcalloc(1,sizeof(struct board_data));
    DAT1->board = bitvector_new();
    DAT1->test = 101;
    ht_insert(H, DAT1);
    DAT1->test = 202;

    struct board_data *DAT2 = xcalloc(1,sizeof(struct board_data));
    DAT2->board = bitvector_full;
    DAT2->test = 104;
    ht_insert(H, DAT2);
    DAT2->test = 211;

    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
      DAT->board = bitvector_flip(bitvector_new(), i);
      DAT->test = i;
      ht_insert(H, DAT);
      (DAT->test)++;
    }

    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
      DAT->board = bitvector_flip(bitvector_full, i);
      DAT->test = 200 - i;
      ht_insert(H, DAT);
      (DAT->test)--;
    }

    if (DAT1 != ht_lookup(H, bitvector_new())) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = ht_lookup(H, bitvector_flip(bitvector_new(), i));
      if (DAT == NULL) return 1;
      if (DAT->test != i + 1) return 1;
    }
    if (DAT2 != ht_lookup(H, bitvector_full)) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = ht_lookup(H, bitvector_flip(bitvector_full, i));
      if (DAT == NULL) return 1;
      if (DAT->test != 199 - i) return 1;
    }

    hdict_free(H);
    
  } else if (strcmp(cmd, "add_many_same_test") == 0) {
    hdict_t H = ht_new(10);

    struct board_data *DAT1 = xcalloc(1,sizeof(struct board_data));
    DAT1->board = bitvector_new();
    DAT1->test = 5;
    ht_insert(H, DAT1);

    struct board_data *DAT2 = xcalloc(1,sizeof(struct board_data));
    DAT2->board = bitvector_full;
    DAT2->test = 5;
    ht_insert(H, DAT2);

    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
      DAT->board = bitvector_flip(bitvector_new(), i);
      DAT->test = 5;
      ht_insert(H, DAT);
    }

    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
      DAT->board = bitvector_flip(bitvector_full, i);
      DAT->test = 5;
      ht_insert(H, DAT);
    }

    if (DAT1 != ht_lookup(H, bitvector_new())) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = ht_lookup(H, bitvector_flip(bitvector_new(), i));
      if (DAT == NULL) return 1;
      if (DAT->test != 5) return 1;
    }
    if (DAT2 != ht_lookup(H, bitvector_full)) return 1;
    for (uint8_t i = 0; i < BITVECTOR_LIMIT; i++) {
      struct board_data *DAT = ht_lookup(H, bitvector_flip(bitvector_full, i));
      if (DAT == NULL) return 1;
      if (DAT->test != 5) return 1;
    }

    hdict_free(H);

  } else if (strcmp(cmd, "add_repeated1") == 0) {
    hdict_t H = ht_new(10);
    struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
    DAT->board = bitvector_new();
    DAT->test = 12;
    ht_insert(H, DAT);
    ht_insert(H, DAT);

  } else if (strcmp(cmd, "add_repeated2") == 0) {
    hdict_t H = ht_new(10);
    struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
    DAT->board = bitvector_new();
    DAT->test = 12;
    ht_insert(H, DAT);

    DAT = xcalloc(1,sizeof(struct board_data));
    DAT->board = bitvector_new();
    DAT->test = 12;
    ht_insert(H, DAT);

  } else if (strcmp(cmd, "add_repeated3") == 0) {
    hdict_t H = ht_new(10);
    struct board_data *DAT = xcalloc(1,sizeof(struct board_data));
    DAT->board = bitvector_new();
    DAT->test = 12;
    ht_insert(H, DAT);

    DAT = xcalloc(1,sizeof(struct board_data));
    DAT->board = bitvector_new();
    DAT->test = 16;
    ht_insert(H, DAT);

  } else { exit(1); }

  return 0;
}
