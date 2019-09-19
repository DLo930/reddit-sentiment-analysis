#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "lib/contracts.h"
#include "lib/xalloc.h"
#include "strbuf.h"
#include "assert.h"
/*
 * C Unit tests for string buf lab
 *
 */

 void testIsStrBuf()
 {
  assert(is_strbuf(NULL) == false);

  struct strbuf *sb = xmalloc(sizeof(struct strbuf));
  
  sb->limit = 3;
  sb->len = 0;
  sb->buf = xcalloc(3, sizeof(char));
  assert(is_strbuf(sb) == true);

  sb->len = 1;
  sb->buf[1] = '\0';
  assert(is_strbuf(sb) == false);

  sb->buf[0] = 'a';
  assert(is_strbuf(sb) == true);

  sb->buf[0] = 'a';
  assert(is_strbuf(sb) == true);

  sb->buf[1] = 'b';
  assert(is_strbuf(sb) == false);

  sb->buf[0] = '\0';
  assert(is_strbuf(sb) == false);
  
  sb->buf[0] = 'c';
  assert(is_strbuf(sb) == false);

  sb->len = 2;
  assert(is_strbuf(sb) == true);

  sb->buf[2] = 'c';
  assert(is_strbuf(sb) == false);

  sb->buf[2] = '\0';
  assert(is_strbuf(sb) == true);

  free(strbuf_dealloc(sb));

 }

 void testCreate()
 {
  struct strbuf *sb = strbuf_new(3);
  assert(sb->limit == 3);
  assert(sb->len == 0);
  assert(sb->buf[0] == '\0');
  assert(is_strbuf(sb));

  free(strbuf_dealloc(sb));
 }

void testStrBufStr()
{
  struct strbuf *sb = strbuf_new(3);
  char *c = xcalloc(2, sizeof(char));
  char *str1 = strbuf_str(sb);
  assert(strcmp(str1, c) == 0);
  assert(strlen(str1) == 0);
  assert(str1[sb->len] == '\0');
  free(str1);

  c[0] = 'a';
  c[1] = '\0';
  sb->buf[0] = 'a';
  sb->len = 1;

  char *str2 = strbuf_str(sb);
  assert(strcmp(str2, c) == 0);
  assert(strlen(str2) == 1);
  assert(str2[sb->len] == '\0');

  free(str2);
  free(c);
  free(strbuf_dealloc(sb));
}

void testAdd()
{
  struct strbuf *sb = strbuf_new(3);

  char *c = xcalloc(6, sizeof(char));
  strbuf_add(sb, c, 0);
  char *str1 = strbuf_str(sb);
  assert(strcmp(str1, c) == 0);
  assert(sb->buf[0] == '\0');
  assert(sb->len == 0);
  free(str1);

  c[0] = 'a';
  c[1] = '\0';
  strbuf_add(sb, c, 1);
  char *str2 = strbuf_str(sb);
  assert(strcmp(str2, c) == 0);
  assert(sb->buf[1] == '\0');
  assert(sb->len == 1);
  assert(sb->limit == 3);
  
  char *s = xcalloc(6, sizeof(char));
  s = strcpy(s, str2);
  free(str2);

  c[0] = 'b';
  c[1] = 'c';
  c[2] = '\0';
  strbuf_add(sb, c, 2);
  
  s = strcat(s, c);
  char *str3 = strbuf_str(sb);
  assert(strcmp(str3, s) == 0);
  free(str3);

  assert(sb->buf[3] == '\0');
  assert(sb->len == 3);
  assert(sb->limit == 6);

  free(c);
  free(s);
  free(strbuf_dealloc(sb));
}

void testAddStr()
{
  struct strbuf *sb = strbuf_new(3);

  char *c = xcalloc(6, sizeof(char));
  strbuf_addstr(sb, c);
  char *str1 = strbuf_str(sb);
  assert(strcmp(str1, c) == 0);
  assert(sb->buf[0] == '\0');
  assert(sb->len == 0);
  free(str1);

  c[0] = 'a';
  c[1] = '\0';
  strbuf_addstr(sb, c);
  char *str2 = strbuf_str(sb);
  assert(strcmp(str2, c) == 0);
  assert(sb->buf[1] == '\0');
  assert(sb->len == 1);
  assert(sb->limit == 3);
  

  char *s = xcalloc(6, sizeof(char));
  s = strcpy(s, str2);
  free(str2);

  c[0] = 'b';
  c[1] = 'c';
  c[2] = '\0';
  strbuf_addstr(sb, c);

  s = strcat(s, c);
  char *str3 = strbuf_str(sb);
  assert(strcmp(str3, s) == 0);
  free(str3);

  assert(sb->buf[3] == '\0');
  assert(sb->len == 3);
  assert(sb->limit == 6);

  free(c);
  free(s);
  free(strbuf_dealloc(sb));
}

int main() {

  /***************/
  /* string buf tests */
  /***************/
  printf("Testing is strbuf...\n");
  testIsStrBuf();
  printf("Testing create...\n");
  testCreate();
  printf("Testing string creation...\n");
  testStrBufStr();
  printf("Testing add...\n");
  testAdd();
  printf("Testing addstr...\n");
  testAddStr();
  printf("Done\n");
  return 0;
}