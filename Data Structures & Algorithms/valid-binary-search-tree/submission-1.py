# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node,minv,maxv):         
            if not node:
                return True
            # print(node.val,minv,maxv)
            if node.val>=maxv or node.val<=minv:
                return False
            left = isValid(node.left,minv,node.val)
            right = isValid(node.right,node.val,maxv)
            return left and right
        return isValid(root,float('-inf'),float('inf'))
        