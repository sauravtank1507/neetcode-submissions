# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def count(node, max_node):
            
            if not node:
                return 0
            if node.val >= max_node:
                res = 1
            else:
                res = 0
            max_node = max(max_node, node.val)
            
            res += count(node.left, max_node)
            res += count(node.right, max_node)

            return res

        return count(root, root.val)
            