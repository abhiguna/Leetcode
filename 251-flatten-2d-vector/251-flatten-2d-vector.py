# Time = O(n), n: # of elements in the vec
# Space = O(1)
class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = []
        for r in range(len(vec)):
            for c in range(len(vec[r])):
                self.vec.append(vec[r][c])
        self.pos = 0

    def next(self) -> int:
        num = self.vec[self.pos]
        self.pos += 1
        return num
        

    def hasNext(self) -> bool:
        return (self.pos + 1) <= len(self.vec)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()