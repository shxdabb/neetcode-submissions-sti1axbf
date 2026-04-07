# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Node = root
        if Node is None:
            return
        Node.left,Node.right = Node.right,Node.left
        self.invertTree(Node.left)
        self.invertTree(Node.right)

        return root