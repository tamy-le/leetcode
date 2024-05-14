#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_area = 0
        len_heights = len(heights)
        for i in range(len_heights):
            index = i
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                largest_area = max(largest_area, height * (i - index))
            stack.append([index, heights[i]])

        for index, height in stack:
            largest_area = max(largest_area, (len_heights - index) * height)
        return largest_area


# Time: O(n)
# Memory: O(n) if heights in acs order

# @lc code=end
