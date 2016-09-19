import copy

class Board:
    NAUGHT = 1
    CROSS = 4
    DRAW = 5
    MAX_MOVES = 9

    READABLE_CONVERSION = {0: "0", 1: "Y", 4: "X", 5: "DRAW"}
    HASH_CONVERSION = {0: 0, 1: 1, 4: 2}

    @staticmethod
    def next_piece(curr_piece):
        return Board.NAUGHT if curr_piece is Board.CROSS else Board.CROSS

    @staticmethod
    def opposite_winner(winning_piece):
        if winning_piece is Board.DRAW:
            return winning_piece
        return Board.CROSS if winning_piece is Board.NAUGHT else Board.NAUGHT


    def __init__(self):
        self.matrix = [[0,0,0] for i in range (3)]
        self.curr_piece = Board.CROSS
        self.horiz_won_track = [0]*3
        self.vert_won_track = [0]*3
        self.r_cross_won_track = 0
        self.l_cross_won_track = 0
        self.winner = None
        self.moves = 0
        self.hash = 0

    def move(self, x, y):
        if self.matrix[y][x] is not 0 or self.winner is not None:
            raise Exception
        self.matrix[y][x] = self.curr_piece
        self.moves += 1
        self.__update_hash__(x, y, self.curr_piece)
        self.__change_piece__()
        self.__check_win__(x, y)


    def move_copy(self, x, y):
        '''
        :param x: x co-ordinate
        :param y: y co-ordinate
        :return: A copy of the board after the move at x, y has been made
        '''
        board_copy = copy.deepcopy(self)
        board_copy.move(x, y)
        return board_copy

    def __update_hash__(self,x, y, piece):
        self.hash += Board.HASH_CONVERSION[piece] * 3**(y*3+x)


    def __change_piece__(self):
        self.curr_piece = Board.next_piece(self.curr_piece)

    def __check_win__(self, x, y):
        win_val = self.__check_won_for_move__(x, y)
        if win_val is not None:
            self.winner = win_val

    def __check_won_for_move__(self, x, y):
        self.horiz_won_track[y] += self.matrix[y][x]
        if self.horiz_won_track[y] is 3 or self.horiz_won_track[y] is 12:
            return self.matrix[y][x]

        self.vert_won_track[x] += self.matrix[y][x]
        if self.vert_won_track[x] is 3 or self.vert_won_track[x] is 12:
            return self.matrix[y][x]

        if x == y:
            self.r_cross_won_track += self.matrix[y][x]
            if self.r_cross_won_track is 3 or self.r_cross_won_track is 12:
                return self.matrix[y][x]
        if x + y == 2:
            self.l_cross_won_track += self.matrix[y][x]
            if self.l_cross_won_track is 3 or self.l_cross_won_track is 12:
                return self.matrix[y][x]

        if self.moves == Board.MAX_MOVES:
            return Board.DRAW
        return None

    def has_won(self):
        if self.winner is None: return None
        return Board.READABLE_CONVERSION[self.winner]

    def winner_readable(self):
        return Board.READABLE_CONVERSION[self.winner]

    def print_readable(self):
        out_str = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                out_str += Board.READABLE_CONVERSION[self.matrix[i][j]] + " "
            out_str += "\n"
        print out_str


    def __eq__(self, other):
        return self.hash == other.hash

    def __hash__(self):
        return self.hash