#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(nums, permute=[]):
            if not nums:
                res.append(permute)
                return
            for i in range(len(nums)):
                backTrack(nums[:i] + nums[i + 1 :], permute + [nums[i]])

        backTrack(nums)
        return res


# @lc code=end
# Time: O(n*n!)
# Memory: O(n*n!)
