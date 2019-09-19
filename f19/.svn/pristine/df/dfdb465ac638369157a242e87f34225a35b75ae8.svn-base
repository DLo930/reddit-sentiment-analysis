#include <stdio.h>
#include "lib/bitarray.h"
#include "lib/ba-ht.h"
#include "lib/queues.h"
#include "lib/xalloc.h"
#include "lib/boardutil.h"
#include "lib/contracts.h"

typedef uint8_t uint;

bitarray press_button(bitarray board, uint row, uint col, uint width, uint height) {
	bitarray flipped = board;
	if (is_valid_pos(row, col, width, height)) 
	  flipped =  bitarray_flip(flipped, get_index(row, col, width, height));
	if (is_valid_pos(row + 1, col, width, height)) 
	  flipped =  bitarray_flip(flipped, get_index(row + 1, col, width, height));
	if (is_valid_pos(row - 1, col, width, height)) 
	  flipped =  bitarray_flip(flipped, get_index(row - 1, col, width, height));
	if (is_valid_pos(row, col + 1, width, height)) 
	  flipped =  bitarray_flip(flipped, get_index(row, col + 1, width, height));
	if (is_valid_pos(row, col - 1, width, height)) 
	  flipped =  bitarray_flip(flipped, get_index(row, col - 1, width, height));
		return flipped;

}

/*Recursively prints solution starting board start
  to board end. */
void print_solution(ht boards, 
                    bitarray start, 
                    bitarray end, 
                    uint row, 
                    uint col, 
                    uint width, 
                    uint height) {
  if (end == start) {
    //Already at start
	  return;
	} else {
		bitarray prev = press_button(end, row, col, width, height);
		ba_ht_elem B = ht_lookup(boards, &prev);
		ASSERT(B != NULL);
		uint prevrow = B->last_move/width;
		uint prevcol = B->last_move%width;
	  printf("%d:%d\n", (int)row, (int)col);
		print_solution(boards, start, prev, prevrow, prevcol, width, height);
	}
}

int board_lights (bitarray board, uint width, uint height) {
  int n = 0;
	for (uint r = 0; r < height; r++) {
	  for (uint c = 0; c < width; c++) {
		  if (bitarray_get(board, get_index(r, c, width, height))) {
			 n++;
			}
		}
	}
  return n;
}

int main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "Usage: lightsout <board name>\n");
    return 1;
  }
  char *board_filename = argv[1];
  uint width = 0;
  uint height = 0;
  bitarray b = bitarray_new();

  bool read = file_read(board_filename, &b, &width, &height);
  if (!read)
    return 1;

	if(!is_valid_boardsize(width, height))
    return 1;

  print_board(b, width, height);

	ba_ht_elem start = xmalloc(sizeof(struct ba_ht_elem_base));
  start->ba = b;
	queue move_queue = queue_new();
	enq(move_queue, (void *)start);
	ht boards = ba_ht_new(10000);
	ht_insert(boards, start);

	while (!queue_empty(move_queue)) {
	   ba_ht_elem B = (ba_ht_elem)deq(move_queue);
		 for (uint row = 0; row < height; row++) {
		   for (uint col = 0; col < width; col++) {
			   uint i =  get_index(row, col, width, height);
				 bitarray newboard = press_button(B->ba, row, col, width, height);
				 if (board_lights(newboard, width, height) == 0) {
           fprintf(stderr, "Solution found.\n");
				   print_solution(boards, b, newboard, row, col, width, height);
					 ba_ht_free(boards);
					 queue_free(move_queue, NULL);
					 return 0;
				 }
				 if (ht_lookup(boards, &newboard) == NULL) {
					 ba_ht_elem new = xmalloc(sizeof(struct ba_ht_elem_base));
					 new->last_move = i;
					 new->ba = newboard;
					 ba_ht_insert(boards, new);
					 enq(move_queue, (void *)new);
				 }
			 }
		 }
	}
	fprintf(stderr, "No solution found.\n");
	ba_ht_free(boards);
	queue_free(move_queue, NULL);
	return 1;
}
