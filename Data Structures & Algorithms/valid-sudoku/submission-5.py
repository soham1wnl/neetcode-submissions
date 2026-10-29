class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxs=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                s=board[r][c]

                if s=='.': continue
                if s in rows[r] or s in cols[c] or s in boxs[r//3,c//3]: return False
                
                rows[r].add(s)
                cols[c].add(s)
                boxs[r//3,c//3].add(s)

        return True