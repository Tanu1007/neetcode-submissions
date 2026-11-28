# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalancedA = True
        def dfs(node):
            if not node:
                return 0
            nonlocal isBalancedA
            lefth = dfs(node.left)
            righth = dfs(node.right)
            if abs(lefth-righth)>1:
                isBalancedA = False
            return 1+max(lefth,righth)
        dfs(root)
        return isBalancedA
        