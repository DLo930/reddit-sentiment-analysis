
/* 
 * Hash tables interface
 *
 * 15-122 Principles of Imperative Computation */

#include "lib/ba-ht.h"
#include "lib/ht.h"
#include "lib/contracts.h"


ht_key elem_key(ht_elem e) {
  REQUIRES(e != NULL);
  ba_ht_elem E = (ba_ht_elem)e;
  return &E->ba;
}

bool key_equal(ht_key k1, ht_key k2) {
  REQUIRES(k1 != NULL && k2 != NULL);
  return *((ba_ht_key)k1) == *((ba_ht_key)k2);
}

size_t key_hash (ht_key k) {
  REQUIRES(k != NULL);
  return 12312311* (size_t)(*(ba_ht_key)k) + 3423525;
}

/*
size_t elem_free(ht_elem e) {
  free(e);
}*/




ht ba_ht_new(size_t capacity) {
  return ht_new(capacity, &elem_key, &key_equal, &key_hash, &free);
}


ba_ht_elem ba_ht_insert(ht H, ba_ht_elem e) {
  REQUIRES(e != NULL);
  return ht_insert(H, (ht_elem)e);
}

ba_ht_elem ba_ht_lookup(ht H, ba_ht_key k) {
  return ht_lookup(H, (ht_key)k);
}

void ba_ht_free(ht H) {
  ht_free(H);
}
