#include "lib/boardutil.h"
#include "lib/bitarray.h"
#include "lib/xalloc.h"
#include "lib/contracts.h"
#include "lib/ht.h"
#include "lib/queues.h"

#include <stdio.h>

struct position {
  bitarray current_board;
  bitarray moves_made;
};

typedef struct position position;

ht_key elem_key(ht_elem e)
{
  REQUIRES(e != NULL);

  ht_key result = &(((struct position*)e)->current_board);

  ENSURES(result != NULL);
  return result;
}

bool key_equal(ht_key k1, ht_key k2)
{
  REQUIRES(k1 != NULL);
  REQUIRES(k2 != NULL);

  return *((bitarray*)(k1)) == *((bitarray*)(k2));
}

size_t key_hash(ht_key k)
{
  REQUIRES(k != NULL);

  bitarray current_board = *((bitarray*)(k));

  return (size_t)(current_board);
}

void elem_free(ht_elem e)
{
  if (e != NULL)
  {
    free(e);
  }
}

bool winning_bitarray(bitarray *board, uint8_t width, uint8_t height)
{
  for (int x = 0; x < width * height; x++)
  {
    if (bitarray_get(*board,x) == true) return false;
  }

  return true;
}

position *make_moves(ht *visited_boards, queue* move_queue,
                     uint8_t width, uint8_t height)
{
  while(!queue_empty(*move_queue))
  {
    position *current = (position*)(deq(*move_queue));

    ASSERT(current != NULL);

    for (int x = 0; x < width * height; x++)
    {
      position *next = xmalloc(sizeof(position));

      bitarray next_board = bitarray_flip(current->current_board, x);
      if (x / width - 1 >= 0)
        next_board = bitarray_flip(next_board, x - width);
      if (x % width - 1 >= 0)
        next_board = bitarray_flip(next_board, x - 1);
      if (x / width + 1 < height)
        next_board = bitarray_flip(next_board, x + width);
      if (x % width + 1 < width)
        next_board = bitarray_flip(next_board, x + 1);

      bitarray next_move = bitarray_flip(current->moves_made, x);

      next->current_board = next_board;
      next->moves_made = next_move;

      if (ht_lookup(*visited_boards, &next_board) == NULL)
      {
        ht_insert(*visited_boards, next);

        if (winning_bitarray(&next_board, width, height))
        {
          return next;
        }

        enq(*move_queue,next);

      } else {

        free(next);

      }
    }
  }

  return NULL;
}

int main(int argc, char **argv)
{
  if (argc != 2) {
    fprintf(stderr,"Usage: lightsout <board name>\n");
    return 1;
  }

  char *board_filename = argv[1];

  ht visited_boards = ht_new(
    256,
    &elem_key,
    &key_equal,
    &key_hash,
    &elem_free);
  queue move_queue = queue_new();
  bitarray current_board = 0;
  uint8_t width = 0;
  uint8_t height = 0;

  if (!file_read(board_filename, &current_board, &width, &height))
  {
    ht_free(visited_boards);
    queue_free(move_queue, NULL);
    return 1;
  }
  if (BITARRAY_LIMIT < width * height)
  {
    ht_free(visited_boards);
    queue_free(move_queue, NULL);
    return 1;
  }

  position* current = xmalloc(sizeof(position));
  current->current_board = current_board;
  current->moves_made = 0;

  enq(move_queue,current);
  position* result = make_moves(&visited_boards, &move_queue, width, height);

  if (result == NULL)
  {
    return 1;
  }

  for (int x = 0; x < width * height; x++)
  {
    if (bitarray_get(result->moves_made,x))
    {
      printf("%d", x / width);
      printf(":");
      printf("%d", x % width);
      printf("\n");
    }

  }

  ht_free(visited_boards);
  queue_free(move_queue, NULL);
  free(current);
  return 0;
}
