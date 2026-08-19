# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        lis = []

        def solve(node):
            if node is None:
                return

            lis.append(node.val)
            solve(node.left)
            solve(node.right)

        solve(root)

        return lis

        