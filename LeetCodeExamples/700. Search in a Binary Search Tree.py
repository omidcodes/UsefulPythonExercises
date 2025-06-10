# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return None
        
        ptr = root

        while True:
            
            if ptr.val == val:
                return ptr
            
            if ptr.right is None and ptr.left is None:
                return None # the end

            if ptr.left and ptr.left.val == val:
                return ptr.left

            if ptr.right and ptr.right.val == val:
                return ptr.right
            
            if ptr.right and ptr.left is None:
                ptr = ptr.right
                # We just have right
                continue
            
            if ptr.left and ptr.right is None:
                ptr = ptr.left
                # We just have left
                continue
            
            # Till here we are sure that we have both right and left
            if val > ptr.right.val:
                ptr = ptr.right
                continue

            if val < ptr.left.val:
                ptr = ptr.left
                continue

            if val > ptr.val:
                ptr = ptr.right
                continue

            if val < ptr.val:
                ptr = ptr.left
                continue

