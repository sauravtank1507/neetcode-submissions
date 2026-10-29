# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            
            l_depth = depth(node.left)
            r_depth = depth(node.right)
            
            max_depth = max(l_depth, r_depth) + 1
            return max_depth

        return depth(root)
