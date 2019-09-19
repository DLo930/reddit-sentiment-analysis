/* Simple file reading code, translated from C0
 * 15-122 Principles of Imperative Computation, Spring 2011
 * William Lovas
 */

#ifndef _READFILE_H
#define _READFILE_H

/*
 * interface: given a filename, return a "string bundle",
 * which is an array of strings along with its length.
 */

struct string_bundle;
typedef struct string_bundle *string_bundle;

/* allocate and populate a string bundle by reading words from filename */
string_bundle read_words(string filename);
/* free a string bundle, calling string_free on all of its contained strings */
void string_bundle_free(string_bundle sb, void (*string_free)(void *));

string * string_bundle_array(string_bundle wl);
size_t string_bundle_length(string_bundle wl);

#endif /* _READFILE_H */
