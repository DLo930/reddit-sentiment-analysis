/* String Buffer Library
 *
 * 15-122 Principles of Imperative Computation
 */

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "lib/contracts.h"
#include "lib/xalloc.h"

#include "strbuf.h"
#include "_strbuf.h"

bool _is_strbuf(struct strbuf *sb) {
  if (sb == NULL) return false;
  if (!(sb->limit > 0)) return false;
  if (!(sb->len < sb->limit)) return false;
  // alloc == bytes allocated for s->buf cannot be checked
  if (!(sb->buf != NULL)) return false;
  if (!(strlen(sb->buf) == sb->len)) return false;
  /* last line implies sb->buf[sb->len] == '\0' */
  return true;
}

struct strbuf *_strbuf_new(size_t alloc_init) {
  REQUIRES(alloc_init > 0);
  struct strbuf *sb = xmalloc(sizeof(struct strbuf));
  sb->limit = alloc_init;
  sb->len = 0;
  char *buf = xmalloc(alloc_init * sizeof(char));
  buf[0] = '\0';
  for (size_t i=1; i<alloc_init; i++) {
	  buf[i] = 'a';
  }
  sb->buf = buf;
  ENSURES(_is_strbuf(sb));
  return sb;
}

char *_strbuf_dealloc(struct strbuf *sb) {
  REQUIRES(_is_strbuf(sb));
  char *buf = sb->buf;
  free(sb);
  return buf;
}

char *_strbuf_str(struct strbuf *sb) {
  REQUIRES(_is_strbuf(sb));
  char *str = xmalloc((sb->len+1) * sizeof(char));
  strncpy(str, sb->buf, sb->len+1); /* copy '\0' */
  ENSURES(strlen(str) == sb->len);
  return str;
}

void _resize(struct strbuf *sb, size_t bound) {
  REQUIRES(_is_strbuf(sb) && sb->limit <= bound);
  size_t new_alloc = (2*sb->limit >= bound ? 2*sb->limit : bound);
  char *new_buf = xmalloc(new_alloc * sizeof(char));
  strncpy(new_buf, sb->buf, sb->len + 1); /* copy '\0' */
  free(sb->buf);                          /* free old buffer */
  sb->limit = new_alloc;
  /* sb->len unchanged */
  sb->buf = new_buf;
  ENSURES(_is_strbuf(sb));
  return;
}

void _strbuf_add(struct strbuf *sb, char *str, size_t str_len) {
  REQUIRES(_is_strbuf(sb) && str != NULL && strlen(str) == str_len);
  size_t new_len = sb->len + str_len;
  if (new_len < sb->len) {
    fprintf(stderr, "Maximal array size exceeded\n");
    abort();
  } else if (!(new_len < sb->limit)) {
    /* need to resize */
    _resize(sb, new_len+1);
  }
  ASSERT(_is_strbuf(sb));
  ASSERT(new_len < sb->limit);
  strncpy(&sb->buf[sb->len], str, str_len);
  sb->buf[new_len] = '\0';
  sb->len = new_len;
  ENSURES(_is_strbuf(sb));
  return;
}

void _strbuf_addstr(struct strbuf *sb, char *str) {
  REQUIRES(_is_strbuf(sb) && str != NULL);
  _strbuf_add(sb, str, strlen(str));
  ENSURES(_is_strbuf(sb));
  return;
}
