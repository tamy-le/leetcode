#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        h_len = len(height)
        if h_len < 3:
            return 0

        max_left, max_right = height[0], height[-1]
        l, r = 1, h_len - 2
        ans = 0
        while l <= r:
            if max_left < max_right:
                if max_left < height[l]:
                    max_left = height[l]
                else:
                    ans += max_left - height[l]
                l += 1
            else:
                if max_right < height[r]:
                    max_right = height[r]
                else:
                    ans += max_right - height[r]
                r -= 1
            print(l, r, max_left, max_right)
        return ans


# @lc code=end
# Time: O(n)
# Memory: O(1)
