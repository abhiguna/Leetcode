# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Time = O(m/n), m: total # of lists and n: total # of integers in nestedList
# Space = O(m + n)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        # Iterative dfs
        def flatten_list(nestedList):
            res = []
            
            stack = []
            for n in nestedList[::-1]:
                stack.append(n)
            
            while stack:
                top = stack.pop()
                
                if top.isInteger():
                    res.append(top.getInteger())
                else:
                    for n in reversed(top.getList()):
                        stack.append(n)
            return res
        
        self.flat_list = deque()
        self.flat_list.extend(flatten_list(nestedList))
    
    def next(self) -> int:
        return self.flat_list.popleft()
    
    def hasNext(self) -> bool:
        return len(self.flat_list) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())