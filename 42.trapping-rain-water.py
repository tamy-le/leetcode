#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        h_len = len(height)
        l = 0
        while l < h_len and height[l] == 0:
            l += 1
        r = l + 1
        previous_max_index = r
        rain_water = 0
        while l < r < h_len:
            while r < h_len - 1 and height[r] <= height[l]:
                r += 1
                if height[r] >= height[previous_max_index]:
                    previous_max_index = r

            rain_water += ((previous_max_index - l) - 1) * min(
                height[previous_max_index], height[l]
            ) - sum(height[l + 1 : previous_max_index])
            l = previous_max_index
            r = l + 1
            previous_max_index = r
        return rain_water


# @lc code=end
# Time: O(n^2)
# Memory: O(n)
