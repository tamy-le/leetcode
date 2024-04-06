#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum_water = 0
        while left < right:
            if height[left] < height[right]:
                current_water_area = (right - left) * height[left]
                left += 1
            else:
                current_water_area = (right - left) * height[right]
                right -= 1
            maximum_water = max(maximum_water, current_water_area)
        return maximum_water


# Time: O(n)
# Memory: O(n)
# @lc code=end
