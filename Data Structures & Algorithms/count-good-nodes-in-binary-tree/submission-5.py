# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # res = []
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         res.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # count=1
        # print(res)
        # for r in range(1,len(res)):
        #     if res[r]>=res[0]:
        #         count+=1
        # return count
        max_node = 0
        count=0
        def dfs(node,max_node):
            if node is None:
                return
            nonlocal count
            if max_node<=node.val:
                count+=1
            max_node = max(max_node,node.val)
            # if max_node==node.val:
            #     print(node.val)
            #     count+=1
            dfs(node.left,max_node)
            dfs(node.right,max_node)
            return
        dfs(root,root.val)
        return count
            

        