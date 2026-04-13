# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # make a recursive dfs function that calc the height
        # and returns it then we calculate the diameter by adding both the heights returned by 
        # left dfs and right dfs and only update a global variable when we find bigger diameter
        # diameter will be max height of left subtree and max height of right subtree
        # and this needs to be found at every level  

        #lets define a global variable 
        self.res = 0 #res is diameter

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res,left+right)#updating dia by checking left height and right 
                                          #height at every level

            #dfs need to return height 
            return 1 + max(left,right) #this will return height of node at every level
            #and above result will be updated bu adding left and right height
        dfs(root)
        return self.res

        