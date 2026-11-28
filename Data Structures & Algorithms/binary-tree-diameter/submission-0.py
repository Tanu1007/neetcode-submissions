# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal diameter
            leftD = dfs(node.left)
            rightD = dfs(node.right)
            diameter = max(diameter,leftD+rightD)
            return 1+max(leftD,rightD)
        dfs(root)
        return diameter
        