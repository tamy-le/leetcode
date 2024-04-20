class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_size = 3
        board_size = 9

        def canAddToHash(variable, dictionary):
            return variable not in dictionary or variable == "."

        def containsDuplicate(nums: List[int]) -> bool:
            hash_dict = {}
            for i in range(len(nums)):
                if canAddToHash(nums[i], hash_dict):
                    hash_dict[nums[i]] = 1
                else:
                    return True
            return False

        def checkHorizontal(board: List[int]) -> bool:
            for i in range(board_size):
                if containsDuplicate(board[i]):
                    return False
            return True

        def checkVertical(board: List[int]) -> bool:
            for i in range(board_size):
                hash_dict = {}
                for j in range(board_size):
                    if canAddToHash(board[j][i], hash_dict):
                        hash_dict[board[j][i]] = 1
                    else:
                        return False
            return True

        def checkBox(board: List[int]) -> bool:
            for i in range(box_size):
                for j in range(box_size):
                    hash_dict = {}
                    for t in range(i * box_size, (i + 1) * box_size):
                        for k in range(j * box_size, (j + 1) * box_size):
                            if canAddToHash(board[t][k], hash_dict):
                                hash_dict[board[t][k]] = 1
                            else:
                                return False
            return True

        return checkHorizontal(board) and checkVertical(board) and checkBox(board)


# Time: O(1) -> because we know the actual number of operations
# Memory: O(1) -> same
