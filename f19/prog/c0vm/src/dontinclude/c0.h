#include <stdbool.h>
#include <stdlib.h>

#ifndef _C0_H_
#define _C0_H_

typedef char * string;

#define alloc(tp) ((tp *)calloc(1,sizeof(tp)))
#define alloc_array(tp,e) ((tp *)calloc(e,sizeof(tp)))

#endif /* _C0_H_ */
