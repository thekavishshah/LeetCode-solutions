# Last updated: 6/7/2025, 7:02:41 PM
#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def checkTree(self, root):
        return root.val == root.left.val + root.right.val
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        