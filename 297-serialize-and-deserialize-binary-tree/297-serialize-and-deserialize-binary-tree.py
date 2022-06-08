# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Edge case: empty tree
        if not root:
            return ""
        res = []
        
        # preorder traversal: N-L-R
        def dfs(node):
            # Base case: null node
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
            
        dfs(root)
        return ",".join(res)
    
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Edge case: empty tree
        if data == "":
            return None
        
        val_list = data.split(",")
        idx = [0]
        
        def dfs():
            # Base case: null node -> "N"
            if val_list[idx[0]] == "N":
                idx[0] += 1
                return None
            
            # Recursive case: preorder traversal
            node = TreeNode(int(val_list[idx[0]]))
            idx[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node
            
        root = dfs()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))