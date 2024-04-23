#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                return result.append(s)
            if left < n:
                dfs(left + 1, right, s + "(")
            if right < left:
                dfs(left, right + 1, s + ")")

        result = []
        dfs(0, 0, "")
        return result


# @lc code=end
# Time: O(Cn) -> 4^n/n^(3/2) ->  Stirling's approximation, for smaller number catalan number work better with binomial coefficients
# Memory: O(2n*Cn) Catalan number
# Note: Catalan number is coming from Dysk Paths -> number of full binary tree alternatives with 2n+1 nodes
