#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str not in result:
                result[sorted_str] = [word]
            else:
                result[sorted_str].append(word)
        return result.values()


# @lc code=end
# Time: O(n*m*logm)
# Memory: O(n*m)

# Note: return result.values() use more memory then return list:
# 1. Because dict used more space then list and return dictionary object view is still keep dict in memory
