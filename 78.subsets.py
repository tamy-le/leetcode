class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(nums, end, start=0, sub_res=[]):
            res.append(sub_res[:])
            for i in range(start, end):
                sub_res.append(nums[i])
                backTrack(nums, end, i+1)
                sub_res.pop()
        backTrack(nums, len(nums))
        return res

# Time: O(n*2^n)
# Memory: O(n)