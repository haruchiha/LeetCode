# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            leftD = self.maxDepth(root.left)
            rightD = self.maxDepth(root.right)

            if leftD > rightD:
                return leftD + 1
            else:
                return rightD + 1

