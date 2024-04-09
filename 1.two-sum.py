#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        nums_len = len(nums)
        for i in range(nums_len):
            other_number = target - nums[i]
            if other_number in hash_table:
                return [hash_table[other_number], i]
            hash_table[nums[i]] = i
        return []


# @lc code=end
# Time: O(n)
# Memory: O(n)
