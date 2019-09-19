#include <stdbool.h>
#include "lib/contracts.h"
#include "board-ht.h"

static inline hdict_key my_entry_key(hdict_entry e) {
  REQUIRES(e != NULL);
  return &(((struct board_data*)e)->board);
}

bool my_elem_eq(hdict_key x, hdict_key y) {
  REQUIRES (x != NULL && y != NULL);
  return bitvector_equal((*(bitvector*)x),
                         (*(bitvector*)y));
}

size_t my_elem_hash(hdict_key x) {
  REQUIRES (x != NULL);
  bitvector B = (*(bitvector*)x);
  size_t h = 0;
  for (unsigned int i = 0; i < BITVECTOR_LIMIT; i++) {
    h = h << 1 | bitvector_get(B, i);
  }
  return h;
}

hdict_t ht_new(size_t capacity) {
  return hdict_new(capacity, &my_entry_key, &my_elem_eq, &my_elem_hash, &free);
}

void ht_insert(hdict_t H, struct board_data *DAT) {
  REQUIRES(H != NULL);
  REQUIRES(DAT != NULL);
  REQUIRES(hdict_lookup(H, &DAT->board) == NULL);

  hdict_insert(H, (void*)DAT);
}

struct board_data *ht_lookup(hdict_t H, bitvector B) {
  REQUIRES(H != NULL);

  return (struct board_data*) hdict_lookup(H, (void*)&B);
}
