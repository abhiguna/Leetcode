# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time = O(N)
# Space = O(1)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Edge case:
        if not root:
            return ""
        
        res = []
        
        def dfs(node):
            # Base case:
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        return ",".join(res)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Edge case: empty tree
        if data == "":
            return None
        
        data = data.split(",")
        idx = [0]
        
        def dfs():
            # Base case: out of bounds
            if data[idx[0]] == "N":
                idx[0] += 1
                return None
            
            root = TreeNode(int(data[idx[0]]))
            idx[0] += 1
            root.left = dfs()
            root.right = dfs()
            
            return root
        
        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))