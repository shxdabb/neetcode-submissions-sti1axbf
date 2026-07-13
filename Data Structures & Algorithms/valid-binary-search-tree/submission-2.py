# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lb = float("-inf")
        ub = float("inf")

        def dfs(node,lb,ub):
            if not node:
                return True
            # if not (node.val < ub and node.val > lb):
            #     return False

            if not node.val < ub or not node.val > lb:
                return False
            
            return (dfs(node.left,lb,node.val) and dfs(node.right,node.val,ub))

        return dfs(root,lb,ub)


