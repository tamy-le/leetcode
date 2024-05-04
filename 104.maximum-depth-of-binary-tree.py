#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(root, depth=0):
            if not root:
                return 0
            depth = (
                max(findDepth(root.left, depth + 1), findDepth(root.right, depth + 1))
                + 1
            )
            return depth

        return findDepth(root)


# @lc code=end
# Time: O(n)
# Memory: O(1)
