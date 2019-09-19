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

bool is_strbuf(struct strbuf *sb) {
  if (sb == NULL) return false;
  if (!(sb->alloc > 0)) return false;
  if (!(sb->len < sb->alloc)) return false;
  // alloc == bytes allocated for s->buf cannot be checked
  if (!(sb->buf != NULL)) return false;
  if (!(strlen(sb->buf) == sb->len)) return false;
  /* last line implies sb->buf[sb->len] == '\0' */
  return true;
}

struct strbuf *strbuf_new(size_t alloc_init) {
  REQUIRES(alloc_init > 0);
  struct strbuf *sb = xmalloc(sizeof(struct strbuf));
  sb->alloc = alloc_init;
  sb->len = 0;
  char *buf = xmalloc(alloc_init * sizeof(char));
  buf[0] = '\0';
  sb->buf = buf;
  ENSURES(is_strbuf(sb));
  return sb;
}

char *strbuf_dealloc(struct strbuf *sb) {
  REQUIRES(is_strbuf(sb));
  char *buf = sb->buf;
  free(sb);
  return buf;
}

char *strbuf_str(struct strbuf *sb) {
  REQUIRES(is_strbuf(sb));
  char *str = xmalloc((sb->len+1) * sizeof(char));
  strncpy(str, sb->buf, sb->len+1); /* copy '\0' */
  ENSURES(strlen(str) == sb->len);
  return str;
}

void resize(struct strbuf *sb, size_t bound) {
  REQUIRES(is_strbuf(sb) && sb->alloc <= bound);
  // next line requires quadratic space
  // size_t new_alloc = bound;
  size_t new_alloc = (2*sb->alloc >= bound ? 2*sb->alloc : bound);
  char *new_buf = xmalloc(new_alloc * sizeof(char));
  strncpy(new_buf, sb->buf, sb->len+1); /* copy '\0' */
  // commenting out next line is memory leak
  free(sb->buf);			  /* free old buffer */
  sb->alloc = new_alloc;
  /* sb->len unchanged */
  sb->buf = new_buf;
  ENSURES(is_strbuf(sb));
  return;
}

void strbuf_add(struct strbuf *sb, char *str, size_t str_len) {
  REQUIRES(is_strbuf(sb) && str != NULL && strlen(str) == str_len);
  size_t new_len = sb->len + str_len;
  if (new_len < sb->len) {
    fprintf(stderr, "Maximal array size exceeded\n");
    abort();
  } else if (!(new_len < sb->alloc)) {
    // next line is memory error
    // resize(sb, new_len);
    resize(sb, new_len+1);
  }
  ASSERT(is_strbuf(sb));
  ASSERT(new_len < sb->alloc);
  // next line requires quadratic time
  // strncat(sb->buf, str, str_len);
  strncpy(&sb->buf[sb->len], str, str_len);
  sb->buf[new_len] = '\0';
  sb->len = new_len;
  ENSURES(is_strbuf(sb));
  return;
}

void strbuf_addstr(struct strbuf *sb, char *str) {
  REQUIRES(is_strbuf(sb) && str != NULL);
  strbuf_add(sb, str, strlen(str));
  ENSURES(is_strbuf(sb));
  return;
}
