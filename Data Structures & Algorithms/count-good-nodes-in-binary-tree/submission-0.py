# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        path = []
        max_val = 0
        path.append(root.val)
        res = 0

        def dfs(curr):
            nonlocal max_val,res
            if not curr:
                return 
            path.append(curr.val)

            max_val = path[0]
            for i in path:

                if i >= max_val:
                    max_val = i

            if curr.val >= max_val:
                max_val = curr.val
                res+=1
                
                
        #max value is not getting changed after popped
            dfs(curr.left)
            dfs(curr.right)

            return path.pop()
        
        dfs(root)
        return res