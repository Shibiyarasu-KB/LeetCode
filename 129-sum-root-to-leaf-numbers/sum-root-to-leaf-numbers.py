# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(current,sum):
            if not current:
                return 0
            sum=sum*10+current.val
            if not current.left and not current.right:
                return sum
            return dfs(current.left,sum) + dfs(current.right,sum)
        return dfs(root,0)