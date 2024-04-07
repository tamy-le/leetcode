#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, typed_index, previous_i = 0, 0, 0
        name_len, typed_len = len(name), len(typed)
        if name == typed:
            return True
        if name_len > typed_len:
            return False
        while i < name_len and typed_index < typed_len:
            if name[i] == typed[typed_index]:
                i+=1
            elif name[previous_i] != typed[typed_index]:
                return False
            previous_i = i - 1
            typed_index += 1
        #Check if there is any wrong char not in name but in type
        if i == name_len:
            while typed_index < typed_len and typed[typed_index] == name[-1]:
                typed_index+=1
            if typed_index == typed_len:
                return True

        return False
# @lc code=end
#Time: O(n)
#Memory: O(n)
