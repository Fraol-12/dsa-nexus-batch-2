class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # Check columns
        for j in range(9):
            s = set()
            for i in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        item = board[box_row + i][box_col + j]
                        if item in s:
                            return False
                        elif item != '.':
                            s.add(item)

        return True
