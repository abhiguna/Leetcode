class Vector2D:
    # Time = O(1)
    # Space = O(1)
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer = 0
        self.inner = 0

    # Time = O(v/n), v: max # of inner values in any list, n: # of outer lists
    # Space = O(1)
    def advance_to_next(self):
        while self.outer < len(self.vec) and \
                self.inner == len(self.vec[self.outer]):
            self.outer += 1
            self.inner = 0
    
    # Time = O(v/n), v: max # of inner values in any list, n: # of outer lists
    # Space = O(1)
    def next(self) -> int:
        # Advance to the next non-empty row
        self.advance_to_next()
        num = self.vec[self.outer][self.inner]
        self.inner += 1
        return num
    
    # Time = O(v/n), v: max # of inner values in any list, n: # of outer lists
    # Space = O(1)
    def hasNext(self) -> bool:
        # Skip all the empty rows in the vector
        self.advance_to_next()
        return self.outer < len(self.vec)
        
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()