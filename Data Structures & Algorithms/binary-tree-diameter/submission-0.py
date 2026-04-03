# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if node is None:
                return [0,0]

            leftSide = solve(node.left)
            rightSide = solve(node.right)

            curMax = max(leftSide[0], rightSide[0], leftSide[1]+rightSide[1]+1)
            longestWalk = max(leftSide[1]+1, rightSide[1]+1)

            return [curMax, longestWalk]

        rslt = solve(root)
        return rslt[0]-1
        
