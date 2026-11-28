# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lvl_order = []
        queue = deque()
        queue.append(root)
        while queue:
            lvl_size = len(queue)
            curr_lvl = []
            for _ in range(lvl_size):
                node = queue.popleft()
                # print(queue)
                curr_lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl_order.append(curr_lvl)
        
        res=[]
        for lst in lvl_order:
            res.append(lst[-1])

        return res