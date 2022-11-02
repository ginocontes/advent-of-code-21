
import itertools

def main():
    res = numbers_to_extract()


class BingoGame(object): 
    def __init__(self, boards, numbers):

        self._boards = boards
        self._numbers = numbers 
        self._numbers_extracted = set()

    def play(self, to_loose=False):
        winners = []
        for number_extracted in self._numbers:
            self._numbers_extracted.add(number_extracted)
            for board in self._boards:
                has_bingo, points = board.has_bingo(number_extracted, self._numbers_extracted)
                if has_bingo:
                    to_add = True
                    if len(winners) != 0:
                        for i in range(len(winners)):
                            if winners[i][0] == board:
                                to_add = False
                    if to_add:
                         winners += [ (board, True, number_extracted, points)]
        print(len(winners))
        print(winners[0][0]._not_extracted_numbers)
        if len(winners) > 0:
            return winners[0] if not to_loose else winners[-1]
        return None, False, None, None

    


class BingoBoard(object):
    def __init__(self, board):
        self._rows = 5
        self._cols = 5
        self._board: list  = board
        self._not_extracted_numbers = set(itertools.chain(*board))

    def get_columns(self):
        cols = []
        for i in range(5):
            col = []
            for j in range(5):
                col += [self._board[j][i]]
            cols.append(col)
        return cols

    def has_bingo(self, number_extracted, all_numbers_extracted):
        if number_extracted in self._not_extracted_numbers:
            self._not_extracted_numbers.remove(number_extracted)
        for row in self._board:
            if self.is_a_winner(row, all_numbers_extracted):
                print(row)
                return True, sum(self._not_extracted_numbers)

        for column in self.get_columns():
            # if number_extracted in column and number_extracted in self._not_extracted_numbers: # In case the number was removed during parsing of the row (I think it will always be the case)
            #     self._not_extracted_numbers.remove(number_extracted)

            if self.is_a_winner(column, all_numbers_extracted):
                return True, sum(self._not_extracted_numbers)

        return False, None

    def is_a_winner(self, row, numbers_extracted):
        return set(row).issubset(numbers_extracted) 



        

def parse_all_boards(boards):
    # bingo_boards = []
    # for i in range(len(boards)//5):
    #     final_board = []
    #     for j in range(5):
    #         final_board += [boards[i+j]]
    #     if(i != 0):
    #         break
    #     final_board = list(map(lambda l: l.rstrip(), final_board)) 
    #     board = parse_board(final_board)
    #     bingo_boards += [board]
    # print(boards)
    bingo_boards = []
    for i in range(0, len(boards), 6):
        current_board = boards[i:i+5]
        # print(current_board)
        current_board = list(map(lambda x: x.rstrip(), current_board))
        # print(current_board)
        # break
        bingo_board = parse_board(boards[i:i+5])
        print(bingo_board.get_columns())
        bingo_boards += [bingo_board]
        # print(bingo_board)
    # print(bingo_boards)
    return bingo_boards
    


def parse_board(board):
    real_board = [ list(map(lambda x: int(x), b.split())) for b in board]
    return BingoBoard(real_board)

def numbers_to_extract():
    with open("./input1.txt", "r")  as f:
        numbers = f.readline()
        numbers = list(map(lambda n: int(n), numbers.split(",")))
        # print(numbers) # list of numbers that will be extracted in a bingo game
        f.readline() # skip blankline
        boards = f.readlines()  # from now on this will be a 5*5 board separated by newlines
        # print(boards)
        bingo_boards = parse_all_boards(boards)
        game = BingoGame(bingo_boards, numbers)
        winner_board, has_winner, number_extracted, points = game.play(to_loose=True)
        if has_winner:
            print(winner_board, has_winner, number_extracted, points)
    return 


if __name__ == '__main__':
    main()