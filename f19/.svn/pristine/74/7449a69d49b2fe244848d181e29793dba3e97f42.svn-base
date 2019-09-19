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
  // No need to make the omission of the next line a bug.
  // Catching BUG1 and BUG2 imply this.
  if (!(sb->limit > 0)) return false;
#if (BUG == 1)

#else
  if (!(sb->len < sb->limit)) return false;
#endif
  // limit == bytes allocated for s->buf cannot be checked
  if (!(sb->buf != NULL)) return false;
#if (BUG == 2)

#else
  if (!(strlen(sb->buf) == sb->len)) return false;
#endif
  /* last line implies sb->buf[sb->len] == '\0' */
  return true;
}

struct strbuf *strbuf_new(size_t alloc_init) {
  REQUIRES(alloc_init > 0);

#if (BUG == 9)
  alloc_init = 13;
#else

#endif

  struct strbuf *sb = xmalloc(sizeof(struct strbuf));
  sb->limit = alloc_init;
  sb->len = 0;
  char *buf = xmalloc(alloc_init * sizeof(char));
#if (BUG == 3)
  buf[0] = 'A';  // To simulate just not setting buf[0] to NUL.
  buf[alloc_init - 1] = '\0';  // Ensure NUL is somewhere though!
#else
  buf[0] = '\0';
#endif
  sb->buf = buf;
  // ENSURES(is_strbuf(sb));
  return sb;
}

char *strbuf_dealloc(struct strbuf *sb) {
  REQUIRES(is_strbuf(sb));
#if (BUG == 4)
  char* buf = xmalloc(sb->len + 1);
  strcpy(buf, sb->buf);
  free(sb->buf);
#else
  char *buf = sb->buf;
#endif
  free(sb);
  return buf;
}

char *strbuf_str(struct strbuf *sb) {
  REQUIRES(is_strbuf(sb));
  char *str = xmalloc((sb->len+1) * sizeof(char));
#if (BUG == 5)
  (void)str;
  return(sb->buf);
#elif (BUG == 6)
  strncpy(str, sb->buf, sb->len);  // Oops, lost a byte.
  if (sb->len > 0) str[sb->len - 1] = '\0';
  return str;
#elif (BUG == 10)
  strncpy(str, sb->buf, sb->len+2); /* copy '\0' */
  str[sb->len] = '*';
  return str;  
#else
  strncpy(str, sb->buf, sb->len+1); /* copy '\0' */
  // ENSURES(strlen(str) == sb->len);
  return str;
#endif
}

void resize(struct strbuf *sb, size_t bound) {
  REQUIRES(is_strbuf(sb) && sb->limit <= bound);
  /* Next line is a quadratic implementation */
  // size_t new_alloc = bound;
  size_t new_alloc = (2*sb->limit >= bound ? 2*sb->limit : bound);
  char *new_buf = xmalloc(new_alloc * sizeof(char));
  strncpy(new_buf, sb->buf, sb->len + 1); /* copy '\0' */
  free(sb->buf);                          /* free old buffer */
  sb->limit = new_alloc;
  /* sb->len unchanged */
  sb->buf = new_buf;
  // ENSURES(is_strbuf(sb));
  return;
}

void strbuf_add(struct strbuf *sb, char *str, size_t str_len) {
  REQUIRES(is_strbuf(sb) && str != NULL && strlen(str) == str_len);
  size_t new_len = sb->len + str_len;
  if (new_len < sb->len) {
    fprintf(stderr, "Maximal array size exceeded\n");
    abort();
  } else if (!(new_len < sb->limit)) {
    /* need to resize */
#if (BUG == 7)

#else
    resize(sb, new_len+1);
#endif
  }
  // ASSERT(is_strbuf(sb));
  // ASSERT(new_len < sb->limit);
#if (BUG == 7)
  strncpy(&sb->buf[sb->len], str, (str_len >= sb->limit) ? str_len - sb->limit : str_len);
#elif (BUG == 8)
  strncpy(sb->buf, str, str_len);
  sb->buf[str_len] = '\0';
  sb->len = str_len;
#else
  strncpy(&sb->buf[sb->len], str, str_len);
  sb->buf[new_len] = '\0';
  sb->len = new_len;
  // ENSURES(is_strbuf(sb));
#endif
  return;
}

void strbuf_addstr(struct strbuf *sb, char *str) {
  REQUIRES(is_strbuf(sb) && str != NULL);
  strbuf_add(sb, str, strlen(str));
  // ENSURES(is_strbuf(sb));
  return;
}
