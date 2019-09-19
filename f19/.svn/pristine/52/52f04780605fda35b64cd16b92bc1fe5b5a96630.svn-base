/* String Buffer Library
 *
 * 15-122 Principles of Imperative Computation
 * This version exposes the externals, requires
 * discipline from client!
 */

#include <stdbool.h>
#include <stdlib.h>

#include "strbuf.h"

#ifndef __STRBUF_H_
#define __STRBUF_H_

/* defined in strbuf.h */
/*
struct strbuf {
  size_t alloc;
  size_t len;
  char *buf;
};
*/
bool _is_strbuf(struct strbuf *sb);

struct strbuf *_strbuf_new(size_t alloc_init);
char *_strbuf_dealloc(struct strbuf *sb);
char *_strbuf_str(struct strbuf *sb);

void _strbuf_add(struct strbuf *sb, char *str, size_t len);
void _strbuf_addstr(struct strbuf *sb, char *str);

#endif
