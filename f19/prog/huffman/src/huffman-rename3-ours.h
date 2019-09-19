#ifndef _HUFFMAN_RENAME3_OURS_
#define _HUFFMAN_RENAME3_OURS_


// Helper functions in our file
#define error(x) (_our_error(x))
#define build_leaf(x,y) (_our_build_leaf(x,y))
#define build_interior(x,y) (_our_build_interior(x,y))
#define htree_higher_priority _our_htree_higher_priority
#define codetable_insert(x,y,z,u) (_our_codetable_insert(x,y,z,u))
#define encoded_size(x,y,z) (_our_encoded_size(x,y,z))
#define pack_byte(x,y) (_our_pack_byte(x,y))
#define unpack_byte(x,y) (_our_unpack_byte(x,y))


// Functions we want to use the student's version
#define is_htree(x) (_our_is_htree(x))
#define is_htree_leaf(x) (_our_is_htree_leaf(x))
#define is_htree_interior(x) (_our_is_htree_interior(x))
#define build_htree(x) (_our_build_htree(x))
#define htree_to_codetable(x) (_our_htree_to_codetable(x))

// Functions we want to use our version
//#define decode_src(x,y,z) (_our_decode_src(x,y,z))
//#define encode_src(x,y,z) (_our_encode_src(x,y,z))
//#define build_freqtable(x) (_our_build_freqtable(x))
//#define pack(x) (_our_pack(x))
//#define unpack(x,y) (_our_unpack(x,y))

#endif
