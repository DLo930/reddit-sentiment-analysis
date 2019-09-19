#ifndef _HUFFMAN_RENAME2_THEIRS_
#define _HUFFMAN_RENAME2_THEIRS_

// Functions we want to use the student's version
//#define is_htree _their_is_htree
//#define is_htree_leaf _their_is_htree_leaf
//#define is_htree_interior _their_is_htree_interior
//#define htree_higher_priority _our_htree_higher_priority
//#define build_htree _their_build_htree

// Functions we want to use our version
#define decode_src _their_decode_src
#define htree_to_codetable _their_htree_to_codetable
#define encode_src _their_encode_src
#define build_freqtable _their_build_freqtable
#define pack _their_pack
#define unpack _their_unpack

#endif
