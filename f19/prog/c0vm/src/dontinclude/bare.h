#ifndef _BARE_H_
#define _BARE_H_

/* C0 runtime types */
#include <stdbool.h>

struct c0_array {
  int count;
  int elt_size;
  char elems[];
};

typedef char c0_char;
typedef const char *c0_string;

#define C0_HAVE_CONCRETE_RUNTIME
#include "c0runtime.h"

#ifdef CC0
// For slight speed gain, inline:
#define c0_string_fromliteral(s) s

#endif /* CC0 */

#endif /* _BARE_H_ */
