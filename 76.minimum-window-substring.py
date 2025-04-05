#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = len(set(t)), 0
        window_s, count_t = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        res, res_len = [-1, -1], float("infinity")
        l = 0
        for i in range(len(s)):
            window_s[s[i]] = window_s.get(s[i], 0) + 1
            if s[i] in count_t and window_s[s[i]] == count_t[s[i]]:
                have += 1
            while need == have:
                if i - l + 1 < res_len:
                    res = [l, i]
                    res_len = i - l + 1
                window_s[s[l]] -= 1
                if s[l] in count_t and window_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1     
        return s[res[0]:res[1]+1] if res_len != float("infinity") else ""
        
# @lc code=end

# Time: O(n + m) worst case where t appear near the end of s, opposite best case will be when t at begining
# Memory: O(m + k) k is unique character in s
