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
        nodes = data.split(',')
        curNode = 0

        def traverse(node):
            nonlocal curNode
            curNode += 1
            if nodes[curNode] == 'N':
                node.left = None
            else:
                left = TreeNode(int(nodes[curNode]), None, None)
                node.left = left
                traverse(left)
            
            curNode += 1
            if nodes[curNode] == 'N':
                node.right = None
            else:
                right = TreeNode(int(nodes[curNode]), None, None)
                node.right = right
                traverse(right)

        if nodes[curNode] == 'N':
            return None
        
        root = TreeNode(int(nodes[curNode]), None, None)
        traverse(root)

        return root