

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <setjmp.h>

#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "strbuf.h"

void strbuf_addbool(struct strbuf *sb, char *str, bool b) {
  if (b) {
    strbuf_add(sb, str, strlen(str));
  } else {
    strbuf_addstr(sb, str);
  }
}

bool task3(bool b) {
  struct strbuf *sb = xmalloc(sizeof(struct strbuf));
  sb->len = 0;
  sb->limit = 10;
  sb->buf = xcalloc(10, sizeof(char));
  strncpy(sb->buf + 1, "!@#$%^&*(", 9);
  
  strbuf_addbool(sb, "", b);
  if (!(sb->len == 0)) return false;
  if (!(sb->limit == 10)) return false;
  if (!(strcmp(sb->buf, "") == 0)) return false;

  strbuf_addbool(sb, "abc", b);
  if (!(sb->len == 3)) return false;
  if (!(sb->limit == 10)) return false;
  if (!(strcmp(sb->buf, "abc") == 0)) return false;
  
  char s5[10];
  strcpy(s5, "def");
  strbuf_addbool(sb, s5, b);
  if (!(sb->len == 6)) return false;
  if (!(sb->limit == 10)) return false;
  if (!(strcmp(sb->buf, "abcdef") == 0)) return false;

  // Resize not yet needed
  char s4[4];
  strcpy(s4, "ghi");
  strbuf_addbool(sb, s4, b);
  if (!(sb->len == 9)) return false;
  if (!(sb->limit == 10)) return false;
  if (!(strcmp(sb->buf, "abcdefghi") == 0)) return false;

  // Test resize on exact boundary
  strbuf_addbool(sb, "x", b);
  if (!(sb->limit > 10)) return false;
  if (!(sb->len == 10)) return false;
  if (!(strcmp(sb->buf, "abcdefghix") == 0)) return false;

  for (size_t i = sb->len+1; i < sb->limit; i++) sb->buf[i] = '?'; 

  // Presumabily this'll cause a resize
  char sB[] = "12345678912345678912345678912345678912345*";
  strbuf_addbool(sb, sB, b);
  if (!(sb->limit > 52)) return false;
  if (!(sb->len == 52)) return false;
  if (!(sb->buf[52] == '\0')) return false;
  if (!(sb->buf[51] == '*')) return false;

  // Now test resize when boundary strictly exceeded
  sb->len = 0;
  sb->limit = 1;
  sb->buf[0] = '\0';
  strbuf_addbool(sb, sB, b);
  if (!(sb->limit > 42)) return false;
  if (!(sb->len == 42)) return false;
  if (!(strcmp(sb->buf, sB) == 0)) return false;

  free(sb->buf);
  free(sb);

  return true;
}

int c0_main(int argc, char **argv) {

  if (argc < 2) {
    fprintf(stderr, "Must pass task number on command line\n");
    return 2;
  }

  char *cmd = argv[1];

  struct strbuf* sb = xmalloc(sizeof(struct strbuf));
  sb->limit = 4;
  sb->len = 0;
  sb->buf = xcalloc(5, sizeof(char));
    
  if (strcmp(cmd, "is_strbuf") == 0) {

    // Basic invariant checking
    if (is_strbuf(NULL)) return 1;

    // Correct string buffers of length 0-3 in a size "4" buffer
    for (size_t i = 0; i < 3; i++) {
      sb->buf[i] = 'x';
      sb->len = i+1;
      if (!is_strbuf(sb)) return 1;
    }

    // sb->buf[sb->len] must be '\0'
    strcpy(sb->buf, "abc");
    for (int i = 0; i < 3; i++) {
      sb->len = i;
      if (is_strbuf(sb)) return 1;  // len < strlen
    }
    sb->len = 3;
    if (!is_strbuf(sb)) return 1;
    sb->buf[2] = '\0';
    if (is_strbuf(sb)) return 1;    // len > strlen

  } else if (strcmp(cmd, "is_strbuf_contiguous") == 0) {
    
    // Is the cstring the correct length?
    sb->buf[0] = 'x';
    sb->buf[2] = 'x';
    sb->len = 3;
    if (is_strbuf(sb)) return 1;

  } else if (strcmp(cmd, "is_strbuf_tougher") == 0) {

    // len >= limit is invalid
    sb->len = 4;
    sb->limit = 4;
    sb->buf[0] = 'a';
    sb->buf[1] = 'b';
    sb->buf[2] = 'c';
    sb->buf[3] = 'd';
    if (is_strbuf(sb)) return 1;
    sb->len = 5;
    if (is_strbuf(sb)) return 1;
    sb->buf[3] = '\0';
    if (is_strbuf(sb)) return 1;
    sb->len = 3;
    if (!is_strbuf(sb)) return 1;

    // A string buffer that can only hold "" is valid
    sb->limit = 1;
    sb->len = 0;
    sb->buf[0] = '\0';
    if (!is_strbuf(sb)) return 1;

    // A string buffer of limit 0 is always invalid
    sb->limit = 0;
    for (size_t i = 0; i < 5; i++) {
      sb->len = i;
      if (is_strbuf(sb)) return 1;
    }

  } else if (strcmp(cmd, "is_strbuf_overly_strict") == 0) {
    
    // Allowing nonsense past the null terminator:
    //  '\0' 'x' 'x' 'x'
    //  '*' '\0' 'x' 'x'
    //  '*' '*' '\0' 'x'
    //  '*' '*' '*' '\0'
    strncpy(sb->buf, "xxxx", 4);
    for (size_t i = 0; i < 4; i++) {
      sb->buf[i] = '\0';
      sb->len = i;
      if (!is_strbuf(sb)) return 1;
      sb->buf[i] = '*';
    }

  } else if (strcmp(cmd, "is_strbuf_c_specific_bugs") == 0) {

    // Null buffers nooooooo
    free(sb->buf);
    sb->buf = NULL;
    if (is_strbuf(sb)) return 1;

  } else if (strcmp(cmd, "strbuf_new0") == 0) {

    strbuf_new(0);

  } else if (strcmp(cmd, "strbuf_new1") == 0) {
    free(sb->buf);
    free(sb);
    sb = strbuf_new(1);
    if (sb == NULL) return 1;
    if (sb->limit != 1) return 1;
    if (sb->len != 0) return 1;
    if (sb->buf == NULL) return 1;
    if (sb->buf[0] != '\0') return 1;
    sb->buf[0] = 'x';

  } else if (strcmp(cmd, "strbuf_new3") == 0) {
    free(sb->buf);
    free(sb);
    sb = strbuf_new(3);
    if (sb == NULL) return 1;
    if (sb->limit != 3) return 1;
    if (sb->len != 0) return 1;
    if (sb->buf == NULL) return 1;
    if (sb->buf[0] != '\0') return 1;
    sb->buf[2] = 'x';

  } else if (strcmp(cmd, "strbuf_str") == 0) {
    sb->buf[0] = '?';
    sb->buf[1] = '\0';
    sb->buf[2] = 'x';
    sb->buf[3] = 'y';
    sb->len = 1;

    char* s4 = sb->buf;
    char* s4a = strbuf_str(sb);
    char* s4b = strbuf_str(sb);

    if (s4 == s4a) return 1;
    if (s4 == s4b) return 1;
    if (s4a == s4b) return 1;

    if (sb->buf != s4) return 1;
    if (sb->buf[0] != '?') return 1;
    if (sb->buf[1] != '\0') return 1;
    if (strcmp(s4, s4a) != 0) return 1;
    if (strcmp(s4, s4b) != 0) return 1;
    free(s4a);
    free(s4b);

  } else if (strcmp(cmd, "strbuf_strnull") == 0) {
    strbuf_str(NULL);

  } else if (strcmp(cmd, "strbuf_add") == 0) {
    if (!task3(true)) return 1;

  } else if (strcmp(cmd, "strbuf_addstr") == 0) {
    if (!task3(false)) return 1;

  } else if (strcmp(cmd, "strbuf_add1") == 0) {
    strbuf_add(NULL, "abc", 3);

  } else if (strcmp(cmd, "strbuf_add2") == 0) {
    strbuf_add(sb, "abc", 0);

  } else if (strcmp(cmd, "strbuf_add3") == 0) {
    strbuf_add(sb, "abc", 5);

  } else if (strcmp(cmd, "strbuf_add4") == 0) {
    strbuf_add(sb, "abc", 4);

  } else if (strcmp(cmd, "strbuf_add5") == 0) {
    strbuf_add(sb, "abc", 2);

  } else if (strcmp(cmd, "strbuf_addstr1") == 0) {
    strbuf_addstr(NULL, "abc");

  } else if (strcmp(cmd, "strbuf_add1_c_specific") == 0) {
    strbuf_add(sb, NULL, 0);

  } else if (strcmp(cmd, "strbuf_add2_c_specific") == 0) {
    strbuf_add(sb, NULL, 1);

  } else if (strcmp(cmd, "strbuf_add3_c_specific") == 0) {
    strbuf_add(sb, NULL, 17);

  } else if (strcmp(cmd, "strbuf_addstr_c_specific") == 0) {
    strbuf_addstr(sb, NULL);

  } else if (strcmp(cmd, "strbuf_dealloc_bad") == 0) {
    strbuf_dealloc(NULL);

  } else if (strcmp(cmd, "strbuf_dealloc") == 0) {
    char *s1 = sb->buf;
    sb->buf[0] = 'x';
    sb->buf[1] = '\0';
    sb->len = 1;

    char *s2 = strbuf_dealloc(sb);
    if (s1 != s2) return 1;
    if (s2[0] != 'x') return 1;
    if (s2[1] != '\0') return 1;
    free(s2);
    return 0; // AVOID DOUBLE-FREE!

  } else {
    printf("bad argument!");
    exit(1);
  }

  free(sb->buf);
  free(sb);
  return 0;
           
}
