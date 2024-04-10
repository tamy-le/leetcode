#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = list(map(lambda x: "".join(sorted(x)), strs))
        result = {}
        for i in range(len(sorted_strs)):
            if sorted_strs[i] not in result:
                result[sorted_strs[i]] = [strs[i]]
            else:
                result[sorted_strs[i]].append(strs[i])
        return result.values()


# @lc code=end
# Time: O(n)
# Memory: O(n)
