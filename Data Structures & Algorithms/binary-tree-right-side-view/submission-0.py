# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#q = [4,5,6,7]  res = [1,3]
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        q = deque()
        res = []
        q.append(root)

        while q:
            n = q[-1]
            res.append(n.val)

            size = len(q)

            for i in range(size):

                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
    
        return res

