# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortarr = []
        def inorder(node):
            nonlocal sortarr
            if not node:
                return
            if node.left:
                # sortarr.append(node.left.val)
                inorder(node.left)
            sortarr.append(node.val)
            if node.right:
                # sortarr.append(node.right.val)
                inorder(node.right)
        inorder(root)
        # print(sortarr)
        return sortarr[k-1]


        