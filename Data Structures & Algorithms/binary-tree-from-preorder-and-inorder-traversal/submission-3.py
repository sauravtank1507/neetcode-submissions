# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {val: ind for ind, val in enumerate(inorder)}

        self.preInd = 0

        def DFS(l, r):
            if  l > r:
                return None
            
            rootVal = preorder[self.preInd]
            self.preInd += 1
            root = TreeNode(rootVal)
            mid = hashMap[rootVal]
            root.left = DFS(l, mid  - 1)
            root.right = DFS(mid + 1, r)

            return root

        return DFS(0, len(inorder) - 1)