#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        longest_char = 0
        l = 0
        for r, char in enumerate(s):
            if char in dictionary and dictionary[char] >= l:
                l = dictionary[char] + 1
            dictionary[char] = r
            longest_char = max(r - l + 1, longest_char)
        return longest_char


# @lc code=end
# Time: O(n)
# Memory: O(n)
