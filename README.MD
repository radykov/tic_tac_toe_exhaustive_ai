This does a greedy-ish Depth First Search on all the possible permutations on Tic Tac Toe or Toe Tac Tic (tic tac toe where the goal is to make the other player win)

It stops searching as soon as a winning move has been found, also it ends up visiting less board for Toe Tac Tic than Tic Tac Toe, hinting that it's easier to lose at Toe Tac Tic than Tic Tac Toe, at least if you're iterating across the combinations in the same order as me.

Change opposite_mode between True and False to play normal Tic Tac Toe or to play Tic Tac Toe in order to lose

Change HUMAN_PLAYER to be Board.CROSS, Board.NAUGHT to change the human player, change it to -1 to see the AI play itself


Have fun
