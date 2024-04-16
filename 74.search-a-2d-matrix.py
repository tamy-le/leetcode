class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        row_candidate = None
        l, r = 0, num_rows - 1
        while l <= r:
            mid = (r-l)//2 + l
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                l = mid + 1
            else:
                r = mid - 1

        row_candidate = l if matrix[r][0] > target else r
        l, r = 0, num_cols - 1
        if row_candidate != None:
            while l <= r:
                mid = (r-l)//2 + l
                if target == matrix[row_candidate][mid]:
                    return True
                elif target > matrix[row_candidate][mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
        
# Device: Phone
# Time: O(log(m*n))
# Memory: O(1)