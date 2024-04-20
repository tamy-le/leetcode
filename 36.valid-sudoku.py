from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        output = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    output += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(output) == len(set(output))


# Time: O(1) -> Optimize time better, less code
# Memory: O(1)
