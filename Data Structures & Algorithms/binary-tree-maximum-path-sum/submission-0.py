# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def DFS(root):
            if not root:
                return 0
            
            leftMax = DFS(root.left)
            rightMax = DFS(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(root.val + leftMax + rightMax, res[0])

            return root.val + max(leftMax, rightMax)

        DFS(root)

        return res[0]