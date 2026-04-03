# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node is None:
                return [0, True]
            
            left = solve(node.left)
            right = solve(node.right)

            return [max(left[0]+1, right[0]+1), abs(left[0]-right[0]) <= 1 and left[1] and right[1]]
        
        return solve(root)[1]