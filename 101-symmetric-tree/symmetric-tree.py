# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([root])
        
        while q:
            qlen = len(q)
            left, right = [], []
            
            for _ in range(qlen):
                node = q.popleft()
                
                if node:
                    if node.left:
                        left.append(node.left.val)
                        q.append(node.left)
                    else:
                        left.append(None)
                    
                    if node.right:
                        right.append(node.right.val)
                        q.append(node.right)
                    else:
                        right.append(None)
                else:
                    left.append(None)
                    right.append(None)
            
            if left != right[::-1]:
                return False
        
        return True
        