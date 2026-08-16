# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]

            left_depth, right_depth = dfs(root.left), dfs(root.right)

            balanced = left_depth[0] and right_depth[0] and abs(left_depth[1] - right_depth[1]) <= 1

            return [balanced, max(left_depth[1], right_depth[1]) + 1]
        
        return dfs(root)[0]