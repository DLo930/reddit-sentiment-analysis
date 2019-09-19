/*
 * Reading words from a file using the C0 file library
 *
 * William Lovas <wlovas@cs.cmu.edu>
 * 15-122, Fall 2010
 */

#include "include/c0.h"
#include "include/string.h0"
// #include "file.h0"
#include "include/bare.h" /* for typedef c0_string */
#include "include/util.h" /* for freadline */

#include "lib/xalloc.h"
#include "lib/contracts.h"

#include "readfile.h"


/*
 * implementation follows
 */

/*** file readers -- for reading space-separated words out of a file ***/

// NB: more than just space, actually -- matches any "interword" character
bool is_space(char c) {
    return c == ' ' || c == '\t' || c == '\n' || c == '\r';
}

/* returns the word in sentence starting at i, and sets *newi to the
   beginning of the next word, or just past the end of the sentence if
   there is no next word */
string word(string sentence, int i, int *newi)
//@requires 0 <= i && i < string_length(sentence);
//@requires !is_space(string_charat(sentence, i));
//@requires newi != NULL;
//@ensures string_length(\result) > 0;
//@ensures *newi <= string_length(sentence);
{
    int j = i+1;
    int len = string_length(sentence);
    /* find next space */
    while (j < len && !is_space(string_charat(sentence, j)))
    //@loop_invariant 0 <= j && j <= len;
    {
        j++;
    }
    *newi = j;
    /* NB: allocates */
    return string_sub(sentence, i, j);
}

int skip_space(string sentence, int i)
//@requires 0 <= i && i <= string_length(sentence);
//@ensures \result == string_length(sentence) || !is_space(string_charat(sentence, \result));
{
    int j = i;
    int len = string_length(sentence);
    while (j < len && is_space(string_charat(sentence, j)))
    {
        j++;
    }
    return j;
}

struct reader {
    FILE *file;
    string current;
    int current_idx;
};

typedef struct reader *reader;

/* a reader is valid if its buffer pointer is either in bounds for its
   buffer or just past the end of its buffer.
   TODO: fit this into pre- and post-conditions of functions below... */
bool reader_valid(reader r) {
    return r == NULL
        || (0 <= r->current_idx && r->current_idx <= string_length(r->current));
}

bool at_space(reader r)
//@requires r != NULL;
{
    return r->current_idx < string_length(r->current)
        && is_space(string_charat(r->current, r->current_idx));
}

/* NB: allocates */
string truncating_file_readline(FILE *file) {
    REQUIRES(!feof(file));
    string s = (string) freadline(file);
    ASSERT(s != NULL);
    int len = string_length(s);
    /* ensure allocation happens -- string_sub will otherwise return "" */
    if (len > 0 && string_charat(s, 0) == '#') {
        free(s);
        // return c0_string_fromcstr("");
        // yecch: depends on string == char *:
        return xcalloc(1, sizeof(char)); // init'ed to "\0"
    }
    for (int i = 1; i < len; i++)
        //@loop_invariant 1 <= i && i <= len;
        if (string_charat(s, i) == '#') {
            string res = string_sub(s, 0, i);
            free(s);
            return res;
        }
    // ensures s is allocated
    return s;
}

reader get_reader(string fname)
//@ensures \result == NULL || !at_space(\result);
{
    /* simulate file_read from C0 file library */
    FILE *file = fopen(fname, "r");
    if (file == NULL) {
        c0_abort("Could not open file");
    }

    if (feof(file)) {
        fclose(file);
        return NULL;    /* special case: null reader is empty */
    } else {
        reader r = alloc(struct reader);
        r->file = file;
        r->current = truncating_file_readline(file);
        r->current_idx = skip_space(r->current, 0);
        return r;
    }
}

void close_reader(reader r) {
    if (r != NULL) {
        fclose(r->file);
        free(r->current);
        free(r);
    }
}

string read_word(reader r)
//@requires r == NULL || !at_space(r);
//@ensures r == NULL || !at_space(r);
{
    /* no strings available from the empty reader */
    if (r == NULL) return "";

    /* if we're at the end of a line, read lines until we get to a new word */
    while (r->current_idx == string_length(r->current) && !feof(r->file))
    //@loop_invariant !at_space(r);
    {
        /* XXX BUG: might not be allocated, if string_sub returned "" */
        free(r->current);
        r->current = truncating_file_readline(r->file);
        r->current_idx = skip_space(r->current, 0);
    }

    /* two cases: either we're at a word char or we've exhausted the file */
    /*@ assert (r->current_idx < string_length(r->current)
                && !is_space(string_charat(r->current, r->current_idx)))
            || (r->current_idx == string_length(r->current)
                && file_eof(r->file));
    @*/
    if (r->current_idx < string_length(r->current))
    //@assert !is_space(string_charat(r->current, r->current_idx));
    // (follows from !at_space(r))
    {
        int i;
        string w = word(r->current, r->current_idx, &i);
        r->current_idx = skip_space(r->current, i);
        return w;
    } else
    //@assert (r->current_idx == string_length(r->current));
    //@assert file_eof(r->file);
    {
        // no word, and current string exhausted
        return "";
    }
}


/*** linked lists containing strings ***/

struct string_list_cell {
    string head;
    struct string_list_cell *tail;
};

typedef struct string_list_cell *string_list;

size_t string_list_length(string_list l) {
    size_t count = 0;
    while (l != NULL) {
        count++;
        l = l->tail;
    }
    return count;
}

string_list string_list_empty() {
    return NULL;
}

string_list string_list_cons(string s, string_list l) {
    string_list res = alloc(struct string_list_cell);
    res->head = s;
    res->tail = l;
    return res;
}

void string_list_free(string_list l, void (*elem_free)(void *)) {
    while (l != NULL) {
        string_list tail = l->tail;
        if (elem_free != NULL) elem_free(l->head);
        free(l);
        l = tail;
    }
}

/* convert a string list to an array, reversing the elements */
string * rev_list_to_array(string_list l)
//@ensures \length(\result) == string_list_length(l);
{
    size_t len = string_list_length(l);
    string * res = alloc_array(string, len);
    size_t i;
    string_list ll = l;
    for (i = len; 0 < i--; ) {
        //@assert ll != NULL;
        res[i] = ll->head;
        ll = ll->tail;
    }
    return res;
}


/*** read words from a file ***/

struct string_bundle {
    string * array;
    size_t length;
};

string * string_bundle_array(string_bundle wl) { return wl->array; }
size_t string_bundle_length(string_bundle wl) { return wl->length; }

string_bundle read_words(string filename)
//@ensures \length(\result->array) == \result->length;
{
    reader r = get_reader(filename);
    string_list l = NULL;
    string w = read_word(r);
    string_bundle res = alloc(struct string_bundle);
    size_t count = 0;

    /* accumulate words in reverse order */
    while (!string_equal(w, "")) {
        l = string_list_cons(w, l);
        w = read_word(r);
        count++;
    }
    close_reader(r);

    /* reverse accumulated words and convert to array */
    /* PERF: could pass count into rev_list_to_array to avoid recomputing it */
    res->array = rev_list_to_array(l);
    res->length = count;
    string_list_free(l, NULL);
    return res;
}

void string_bundle_free(string_bundle wl, void (*string_free)(void *)) {
    for (size_t i = 0; i < wl->length; i++)
        if (string_free != NULL) string_free(wl->array[i]);
    free(wl->array);
    free(wl);
}
