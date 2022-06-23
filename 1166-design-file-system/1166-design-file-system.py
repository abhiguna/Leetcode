class FileSystem:
    # Time = O(1)
    # Space = O(1)
    def __init__(self):
        self.paths_seen = {
            "": -1,
            "/": -1
        }
        
    # Time = O(1)
    # Space = O(1)
    def createPath(self, path: str, value: int) -> bool:
        split_path = path.split("/")
        n = len(split_path)
        parent_path = "/".join(split_path[0:n-1])
        
        if path == "" or path == "/" or (path in self.paths_seen) or (parent_path not in self.paths_seen):
            return False
        
        self.paths_seen[path] = value
        return True
        
    # Time = O(1)
    # Space = O(1)
    def get(self, path: str) -> int:
        if path in self.paths_seen:
            return self.paths_seen[path]
        return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)