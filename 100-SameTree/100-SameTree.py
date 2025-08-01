# Last updated: 7/31/2025, 6:14:06 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self,p, q):
        #if both p and q are null, if they are return true
        # if one of them is null, return false
        #if both are not null, check if the node values are equal


        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        if p.val!=q.val:
            return False
        
        #check the root if they are equal
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        