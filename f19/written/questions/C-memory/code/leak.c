#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "lib/xalloc.h"
#include "lib/contracts.h"

typedef struct list_node list;
struct list_node {
  int data;
  list* next;
};

void free_list(list* L) {
  list* current = L;
  while (current != NULL) {
    list* next = current->next;
    free(current);
    current = next;
  }
  return;
}

void sum(list* L) {
  list* sum = xmalloc(sizeof(list));
  sum->data = 0;
  list* current = L;
  while (current != NULL) {
    sum->data += current->data;
    current = current->next;
  }
  L->data = sum->data;
  L->next = NULL;
  return;
}

void print_list(list* L) {
  while (L != NULL) {
    printf("%d ", L->data);
    L = L->next;
  }
  printf("\n");
}

int main() {
  list* current = NULL;
  for (int i=0 ; i<10 ; i++) {
    ASSERT(0 <= i);
    list* new = xmalloc(sizeof(list));
    new->data = i;
    new->next = current;
    current = new;
  }
  printf("Initial list: "); print_list(current);
  sum(current);
  printf("Summed list: "); print_list(current);
  return 0;
}
