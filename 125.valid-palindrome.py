#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_string = "".join(filter(lambda x: x.isalnum(), s)).lower()
        for i in range(len(alphanum_string) // 2):
            if alphanum_string[i] != alphanum_string[-(i + 1)]:
                return False
        return True


# @lc code=end
