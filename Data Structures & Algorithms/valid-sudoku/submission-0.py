class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # for rule 1 and 2
    # look into a specific dimension, either x or y
    # for this to be valid, each row OR column must have different arrangements of 1 to 9
    # meaning the position of 1 has to be different in every column, so if 1 takes index 0 in the first row, 
    # there can NOT be a 1 in index 0 anymore, same for other numbers

    # for rule 3
        row = defaultdict(set)
        col = defaultdict(set)
        three_by_three = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                elif (board[i][j] in row[i]) or (board[i][j] in col[j]) or (board[i][j] in three_by_three[(i//3,j//3)]):
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                three_by_three[(i//3,j//3)].add(board[i][j])
        
        return True