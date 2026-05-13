# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#basic idea is to use a helper function to compare if two trees are same 
#and return True or false

# and in main function 
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        if not subRoot:
            return True
        
        
        if self.helper_sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))


    
    def helper_sameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.helper_sameTree(p.left,q.left) and self.helper_sameTree(p.right,q.right)
            





