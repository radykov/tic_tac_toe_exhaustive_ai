from board import Board

board = Board()
visited_boards = {}
visited_boards[board.hash] = board
opposite_mode = True
HUMAN_PLAYER = Board.CROSS

def play_human():
    human_board = Board()
    while human_board.winner is None:
        human_board.print_readable()
        if human_board.curr_piece is not HUMAN_PLAYER:
            found_board = visited_boards[human_board.hash]
            human_board.move(found_board.next_move[0], found_board.next_move[1])
        else:
            human_moves = map(int, raw_input("Enter moves: ").split(" "))
            try:
                human_board.move(human_moves[0], human_moves[1])
            except Exception:
                print "That was an incorrect move, try again"
    human_board.print_readable()
    human_board.winner_readable()

def update_board_winner(board_to_update, x, y, winner):
    board_to_update.eventual_winner = winner
    board_to_update.next_move = [x,y]

def play_all(played_boards, board):
    if board.winner is not None:
        # Update the eventual winner for this board
        if opposite_mode:
            board.eventual_winner = Board.opposite_winner(board.winner)
        else:
            board.eventual_winner = board.winner
        return board.eventual_winner

    curr_best = None
    # i is the x value
    for i in range(3):
        # j is the y value
        for j in range(3):
            try:
                new_board = board.move_copy(i,j)
            except Exception as e:
                continue
            if new_board.hash not in played_boards:
                played_boards[new_board.hash] = new_board
                eventual_winner = play_all(played_boards, new_board)
            else:
                eventual_winner = played_boards[new_board.hash].eventual_winner

            # If a node placed by player results in them forcing a win, save this as the best move and
            # the function can be exited
            if eventual_winner == board.curr_piece:
                update_board_winner(board, i, j, eventual_winner)
                return eventual_winner

            # If no move has been placed, then any winner will be the best eventual winner and any next reacheable board
            # is the best reachable board
            if curr_best is None:
                update_board_winner(board, i, j, eventual_winner)
                curr_best = eventual_winner
            # If no winning move has been reached yet, the best we can get otherwise is a draw
            elif curr_best is not Board.DRAW and eventual_winner is Board.DRAW:
                update_board_winner(board, i, j, eventual_winner)
                curr_best = Board.DRAW

    return curr_best

print "Winner is " + Board.READABLE_CONVERSION[play_all(visited_boards, board)]
print str(len(visited_boards)) + " unique board iterated"
play_human()