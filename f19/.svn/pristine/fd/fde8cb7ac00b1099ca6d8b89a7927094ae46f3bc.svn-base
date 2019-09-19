/* String Buffer Library
 *
 * 15-122 Principles of Imperative Computation
 */

/* not yet a solution to test the string buffer */

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <setjmp.h>

#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "strbuf.h"
/* interface for reference implementation */
#include "_strbuf.h"

/* Task 1: is_strbuf */
bool task1() {
  if (!(is_strbuf(NULL) == false)) return false;

  char *s4 = xmalloc(4*sizeof(char));
  s4[0] = '\0';
  // This initializiation prevents a really picky issue: is_strbuf
  // reading from unitialized memory. Because this only happens in
  // badly incorrect implementations I'm not deeply worried about it.
  // It's an interesting test case, but 
  s4[1] = '?';
  s4[2] = '*';
  s4[3] = '!';

  struct strbuf *sb = xmalloc(sizeof(struct strbuf));
  sb->limit = 0;
  sb->len = 0;
  sb->buf = s4;
  if (!(is_strbuf(sb) == false)) return false; /* !(alloc > 0) */

  sb->limit = 4;                /* alloc > 0 */
  sb->len = 4;                  /* !(len < alloc) */
  if (!(is_strbuf(sb) == false)) return false;

  sb->len = 2;                  /* len < alloc */
  sb->buf = NULL;               /* !(buf != NULL) */
  if (!(is_strbuf(sb) == false)) return false;

  sb->buf = s4;
  sb->buf[0] = 'a';
  sb->buf[1] = '\0';            /* strlen(buf) < len */
  /* reading sb->buf[sb->len] here will read unitialized memory */
  /* Not anymore, see note above - rjs */
  if (!(is_strbuf(sb) == false)) return false;

  sb->buf[1] = 'b';
  sb->buf[2] = '\0';            /* strlen(buf) == len */
  if (!(is_strbuf(sb) == true)) return false;

  sb->buf[2] = 'c';
  sb->buf[3] = '\0';            /* strlen(buf) > len */
  if (!(is_strbuf(sb) == false)) return false;

  char *s1 = xmalloc(sizeof(char));
  s1[0] = '\0';
  sb->limit = 1;
  sb->len = 0;
  sb->buf = s1;
  if (!(is_strbuf(sb) == true)) return false;

  free(s4);
  free(s1);
  free(sb);

  return true;
}

/* Task 2: strbuf_new, strbuf_dealloc, strbuf_str */
bool task2() {

  struct strbuf *sb = strbuf_new(3);
  if (!(sb->limit == 3)) return false;
  if (!(sb->len == 0)) return false;
  if (!(sb->buf[0] == '\0')) return false;
  if (!_is_strbuf(sb)) exit(1); /* oops! */

  free(sb->buf);                /* overwrite below */

  char *s3 = xmalloc(3*sizeof(char));
  s3[0] = '?';
  s3[1] = '\0';
  sb->limit = 3;
  sb->len = 1;
  sb->buf = s3;
  if (!_is_strbuf(sb)) exit(1); /* oops! */

  char *t3a = strbuf_str(sb);   /* first copy */
  char *t3b = strbuf_str(sb);   /* second copy */
  if (!(strcmp(t3a, s3) == 0)) return false;
  if (!(strcmp(t3b, s3) == 0)) return false;
  if (!(t3a != s3)) return false;            /* require copy */
  if (!(t3b != s3)) return false;
  if (!(t3a != t3b)) return false;
  free(t3a);
  free(t3b);

  t3a = strbuf_dealloc(sb);
  /* sb is free'd here */
  if (!(t3a == s3)) return false;  /* pointer equality, s3 still defined */

  free(s3);
  return true;
}

/* Task 3: strbuf_add and strbuf_addstr */

bool task3a() {
  struct strbuf *sb = _strbuf_new(10);
  strbuf_addstr(sb, "");
  if (!(sb->len == 0)) return false;
  if (!(strcmp(sb->buf, "") == 0)) return false;

  strbuf_addstr(sb, "abc");
  if (!(sb->len == 3)) return false;
  if (!(strcmp(sb->buf, "abc") == 0)) return false;

  char *s5 = xmalloc(5*sizeof(char));
  strcpy(s5, "def");
  strbuf_addstr(sb, s5);
  if (!(sb->len == 6)) return false;
  if (!(strcmp(sb->buf, "abcdef") == 0)) return false;
  free(s5);

  /* test resize not yet needed */
  char *s4 = xmalloc(4*sizeof(char));
  strcpy(s4, "ghi");
  strbuf_addstr(sb, s4);
  if (!(sb->len == 9)) return false;
  if (!(strcmp(sb->buf, "abcdefghi") == 0)) return false;
  free(s4);

  /* now test resize on exact boundary */
  strbuf_addstr(sb, "j");
  if (!(sb->limit > 10)) return false;
  if (!(sb->len == 10)) return false;
  if (!(strcmp(sb->buf, "abcdefghij") == 0)) return false;
  /* cannot test if buffer is really new, because
   * original buffer has been free'd */

  free(_strbuf_dealloc(sb));

  /* now test resize when boundary strictly exceeded */
  sb = _strbuf_new(1);
  strbuf_addstr(sb, "[{(<>)}]\n"); /* length 9 */
  if (!(sb->limit >= 10)) return false;
  if (!(sb->len == 9)) return false;
  if (!(strcmp(sb->buf, "[{(<>)}]\n") == 0)) return false;

  free(_strbuf_dealloc(sb));
  return true;
}

bool task3b() {
  struct strbuf *sb = _strbuf_new(10);
  strbuf_add(sb, "", 0);
  if (!(sb->len == 0)) return false;
  if (!(strcmp(sb->buf, "") == 0)) return false;

  strbuf_add(sb, "abc", 3);
  if (!(sb->len == 3)) return false;
  if (!(strcmp(sb->buf, "abc") == 0)) return false;

  char *s5 = xmalloc(5*sizeof(char));
  strcpy(s5, "def");
  strbuf_add(sb, s5, 3);
  if (!(sb->len == 6)) return false;
  if (!(strcmp(sb->buf, "abcdef") == 0)) return false;
  free(s5);

  char *s4 = xmalloc(4*sizeof(char));
  strcpy(s4, "ghi");
  strbuf_add(sb, s4, 3);
  if (!(sb->len == 9)) return false;
  if (!(strcmp(sb->buf, "abcdefghi") == 0)) return false;
  free(s4);

  /* now test resize on exact boundary */
  strbuf_add(sb, "j", 1);
  if (!(sb->limit > 10)) return false;
  if (!(sb->len == 10)) return false;
  if (!(strcmp(sb->buf, "abcdefghij") == 0)) return false;
  /* cannot test if buffer is really new, because
   * original buffer has been free'd */

  free(_strbuf_dealloc(sb));

  /* now test resize when boundary strictly exceeded */
  sb = _strbuf_new(1);
  strbuf_add(sb, "[{(<>)}]\n", 9); /* length 9 */
  if (!(sb->limit >= 10)) return false;
  if (!(sb->len == 9)) return false;
  if (!(strcmp(sb->buf, "[{(<>)}]\n") == 0)) return false;

  free(_strbuf_dealloc(sb));
  return true;
}

bool task3() {
  bool b1 = task3a();
  bool b2 = task3b();
  return b1 && b2;
}

#ifdef DEBUG_FAIL

/* Checking REQUIRES contracts for all tasks */
bool check_contracts() {

  /* Task 1 */
  FAILURES_RESET();
  FAIL(strbuf_new(0));
  if (!(FAILURES == 1)) return false;

  /* Task 2 */
  FAILURES_RESET();
  FAIL(strbuf_dealloc(NULL));
  FAIL(strbuf_str(NULL));
  if (!(FAILURES == 2)) return false;

  /* Task 3 */
  FAILURES_RESET();
  struct strbuf *sb = _strbuf_new(27);
  FAIL(strbuf_add(NULL, "abc", 3));
  FAIL(strbuf_add(sb, NULL, 0));
  FAIL(strbuf_add(sb, "abc", 2));
  FAIL(strbuf_addstr(NULL, "abc"));
  FAIL(strbuf_addstr(sb, NULL));
  free(_strbuf_dealloc(sb));
  if (!(FAILURES == 5)) return false;

  FAILURES_RESET();
  return true;
}

#endif

bool stress(int num_adds) {

  /* initialize random number generator */
  srand(0xbadf00d);

  /* allocate a max length string */
  char *tmp = xmalloc(1024 * sizeof(char));
  for (size_t i = 0; i < 1024; i++) {
    tmp[i] = (rand() % 127) + 1; /* range 1..127 */
  }

  /* allocate a relatively small string buffer */
  struct strbuf *sb = _strbuf_new(153);
  size_t total = 0;
  for (int k = 0; k < num_adds; k++) {
    size_t len = rand() % 1024; /* random length of next string */
    char prev = tmp[len];
    tmp[len] = '\0';            /* trim random string */
    strbuf_addstr(sb, tmp);
    tmp[len] = prev;            /* restore random string */
    total = total + len;        /* keep track of length */
  }
  if (!(sb->len == total)) return false;     /* check at least size */
  free(strbuf_dealloc(sb));     /* free sb */
  free(tmp);                    /* free tmp string */

  return true;
}

int c0_main(int argc, char **argv) {

  if (argc < 2) {
    fprintf(stderr, "Must pass task number on command line\n");
    fprintf(stderr, "One of task1, task2, task2, stress <n>, contracts\n");
    return 2;
  }

  char* cmd = argv[1];

#ifndef DEBUG_FAIL

  if (strcmp(cmd, "is_strbuf") == 0) {
    if (is_strbuf(NULL)) return 1;
    for (int i = 0; i < 3; i++) {
      struct strbuf* sb = xmalloc(struct strbuf);
      
    }

  } else if (strcmp(cmd, "task1") == 0) {
    if (!task1()) return 1;
  } else if (strcmp(cmd, "task2") == 0) {
    if (!task2()) return 1;
  } else if (strcmp(cmd, "task3") == 0) {
    if (!task3()) return 1;
  } else if (strcmp(cmd, "stress") == 0) {
    if (argc != 3 ) {
      fprintf(stderr, "Must provide parameter for stress test, e.g., 4000, 8000, ...\n");
      return 2;
    }
    int n = (int)strtol(argv[2], NULL, 0); /* allow hex */
    /* 4K, 8K, 16K, 32K okay with valgrind, up to 1.8 secs */
    /* if you make the buffer just big enough, it will start to create
     * serious issues at 400 (40 MB allocated) and 800 (160 MB allocated)
     */
    if (!(0 < n && n < (1<<30))) {
      fprintf(stderr, "Stress parameter out of range");
      return 2;
    }
    if (!stress(n)) return 1;
  } else if (strcmp(cmd, "contracts") == 0) {
    fprintf(stderr, "Must compile with -DDEBUG_FAIL to run contracts test\n");
    exit(1);
  } else {
    fprintf(stderr, "Task not recognized\n");
    exit(1);
  }

#else

  /* Check contracts in all tasks */
  if (strcmp(cmd, "contracts") == 0) {
    if (!check_contracts()) return 1;
  } else {
    fprintf(stderr, "Check only contracts when compiled with -DDEBUG_FAIL\n");
    exit(1);
  }

#endif

  return 0;
}
