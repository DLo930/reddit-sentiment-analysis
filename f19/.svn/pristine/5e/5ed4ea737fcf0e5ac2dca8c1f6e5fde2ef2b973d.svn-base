#ifndef __C0RUNTIME_H__
#define __C0RUNTIME_H__
#include <stddef.h>

#ifndef C0_HAVE_CONCRETE_RUNTIME
// Generic runtime definitions for compiling libraries
#include <stdbool.h>

typedef struct c0_string_impl* c0_string;
typedef char c0_char;
#endif

typedef struct c0_array c0_array;

// Initializes the runtime
void c0_runtime_init();

// Aborts execution and notifies the user of the reason
void c0_abort(const char *reason);

// Allocates from the GC heap
void *c0_alloc(size_t bytes);
// Allocate an array of elemsize elements of elemcount bytes per element
c0_array* c0_array_alloc(size_t elemsize, int elemcount);

// Returns a pointer to the element at the given index of the given array
// Runtimes may ignore the element size
void* c0_array_sub(c0_array *a, int idx, size_t elemsize);

#ifdef C0_HAVE_CONCRETE_RUNTIME
// Returns the length of the array. This is only permitted in certain C0
// programs since not all runtimes may support it.
int c0_array_length(c0_array *a);
#endif

// Returns the empty string
c0_string c0_string_empty();
// Returns the length of the given string
int c0_string_length(c0_string s);

// Returns the character at the given index of the string. If the index is out
// of range, aborts.
c0_char c0_string_charat(c0_string s, int i);

// Returns the substring composed of the characters of s beginning at index
// given by start and continuing up to but not including the index given by end
// If end <= start, the empty string is returned
// If end < 0 or end > the length of the string, it is treated as though it
//   were equal to the length of the string.
// If start < 0 the empty string is returned.
c0_string c0_string_sub(c0_string s, int a, int b);

// Returns a new string that is the result of concatenating b to a.
c0_string c0_string_join(c0_string a, c0_string b);

// Constructs a c0rt_string_t from a null-terminated string
c0_string c0_string_fromcstr(const char *s);

// Returns a null-terminated string from a c0_string. This string must be
// explicitly deallocated by calling c0_string_freecstr.
const char *c0_string_tocstr(c0_string s);

// Frees a string returned by c0_string_tocstr
void c0_string_freecstr(const char *s);

// Returns a c0_string from a string literal.
c0_string c0_string_fromliteral(const char *s);

bool c0_string_equal(c0_string a, c0_string b);
int c0_string_compare(c0_string a, c0_string b);
bool c0_char_equal(c0_char a, c0_char b);
int c0_char_compare(c0_char a, c0_char b);

#endif // __C0RUNTIME_H__
