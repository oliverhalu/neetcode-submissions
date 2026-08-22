class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create an array of length 9 to count digits
        counts_h = [0] * 9
        counts_v = [0] * 9
        counts = [0] * 9
        # 1. Check validity of horizontal lines
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    counts_h[int(board[i][j]) - 1] += 1
                if board[j][i] != ".":
                    counts_v[int(board[j][i]) - 1] += 1
            # if any element of counts if larger then 1 it means it contians the same digit twice making it invalid
            if any(v > 1 for v in counts_h): return False
            counts_h = [0] * 9
            if any(v > 1 for v in counts_v): return False
            counts_v = [0] * 9


        # 2. check validity of vertical lines
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[j][i] != ".":
                    counts[int(board[j][i]) - 1] += 1
            if any(v > 1 for v in counts): return False
            counts = [0] * 9


        # 3. check validiy of 3x3 squares
        row = 1
        column = 1
        counter = 1
        while row < len(board) + 1 and column < len(board[row - 1]) + 1:
            print("check ",row,column)
            if board[row - 1][column - 1] != ".":
                counts[int(board[row - 1][column - 1]) - 1] += 1
           
            # we reached last column of 3x3 so increase row and jump back in column
            if column % 3 == 0:
                if row % 3 == 0:
                    if any(v > 1 for v in counts) == True: return False
                    counts = [0] * 9
                if row == len(board):
                    row = 1
                    column += 1
                else:     
                    row += 1
                    column -= 2
            else:
                column += 1
            counter += 1
            
        return True

        