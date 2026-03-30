# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        rslt = []
        def traverse(node):
            if node is None:
                rslt.append('N')
                return
            
            rslt.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return ','.join(rslt)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(','))

        def traverse():
            v = next(vals)
            if v == 'N':
                return None
            
            node = TreeNode(int(v), None, None)
            node.left = traverse()
            node.right = traverse()
            return node

        return traverse()