/* C0VM abnormal termination 
 * 15-122 Principles of Imperative Computation
 * Rob Simmons 
 */

#include "lib/c0vm_abort.h"
#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
#include <string.h>

void c0_user_error(char *err) {
  int i = 0;
  fprintf(stderr, "User error signaled in C0VM");

  if (err != NULL) {
    fprintf(stderr, ": %s\n", err);
    i += strlen(err);
  }

  exit(32 + i);
}

void c0_assertion_failure(char *err) {
  fprintf(stderr, "Assertion failure detected in C0VM");
  if (err != NULL) fprintf(stderr, ": %s\n", err);
  exit(26);
}

void c0_memory_error(char *err) {
  fprintf(stderr, "Memory error detected in C0VM: %s\n", err);
  if (err != NULL) fprintf(stderr, ": %s\n", err);
  exit(28);
}

void c0_arith_error(char *err) {
  fprintf(stderr, "Division error detected in C0VM");
  if (err != NULL) fprintf(stderr, ": %s\n", err);
  exit(31);
}
