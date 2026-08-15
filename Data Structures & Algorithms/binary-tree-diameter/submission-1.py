# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]
        def diameter(root):
            if not root:
                return 0
            left_diameter = diameter(root.left)
            right_diameter = diameter(root.right)

            max_diameter[0] = max(max_diameter[0], left_diameter + right_diameter) 

            return max(left_diameter, right_diameter) + 1
        
        diameter(root)
        return max_diameter[0]