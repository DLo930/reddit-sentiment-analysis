#include <stdlib.h>
#include <stdio.h>
#include "xalloc.h"

//Note that the solution to this exercise is very close to the solution to queue_free in the queues programming hw


typedef void* data;
typedef void data_free_fn(data e);

typedef struct list_node *list; 
struct list_node{ 
    struct list_node *next; 
    data d; 
}; 

list list_add(list L, data d){
  list n = xmalloc(sizeof(struct list_node));
  n->next = L;
  n->d = d;
  return n;
}

void list_free(list L, data_free_fn *Fr){ 
    struct list_node *p = L; 
    while(p != NULL){ 
      struct list_node *temp = p; 
      if (Fr != NULL) (*Fr)(temp->d); 
        
      p = p->next; 
      free(temp); 
    } 
    return; 
} 

int main(){
  list L = NULL;
  char * A[5] = {"hi", "hello", ":)", "blah","blahblah"};
  for(int i=0; i<5; i++){
    L = list_add(L,A[i]);
  } 
  list_free(L,NULL);
  L = NULL;
  for(int i=0; i<10; i++){
    int *d = xmalloc(sizeof(int));
    *d = i;
    L = list_add(L,(void*)d);
  } 
  list_free(L,&free);
  
  //Another test worth adding might be to try inserting other data structures with more overhead

  printf("All Tests Passed!\n");
  return 0;
}


