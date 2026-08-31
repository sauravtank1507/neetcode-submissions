# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]

            left_pair = dfs(root.left)
            right_pair = dfs(root.right)

            withRoot = root.val + left_pair[1] + right_pair[1]
            withoutRoot = max(left_pair) + max(right_pair)

            return [withRoot, withoutRoot]

        return max(dfs(root))