class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create an array of length 9 to count digits
        counts_h = [0] * 9
        counts_v = [0] * 9
        counts_b = [0] * 9
        # 1. Check validity of horizontal lines
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    counts_h[int(board[row][col]) - 1] += 1
                if board[col][row] != ".":
                    counts_v[int(board[col][row]) - 1] += 1
            # if any element of counts if larger then 1 it means it contians the same digit twice making it invalid
            if any(v > 1 for v in counts_h): return False
            counts_h = [0] * 9
            if any(v > 1 for v in counts_v): return False
            counts_v = [0] * 9

        for box in range(9):
            box_row = (box // 3) * 3
            box_col = (box % 3) * 3

            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if board[r][c] != ".":
                        counts_b[int(board[r][c ]) - 1] += 1 
            
            if any(v > 1 for v in counts_b): return False
            counts_b = [0] * 9
            
        return True

        