class StockSpanner:

    def __init__(self):
        self.stack = deque() # Each element in stack is (price_of_stack, day)
        self.day = 0 # Will keep incrementing self.day for every call in next

    def next(self, price: int) -> int:
        # Remove all the elements that have a price <= current price
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        if self.stack:
            span = self.day - self.stack[-1][1]
        else:
            span = self.day + 1
        
        self.stack.append((price, self.day))
        self.day += 1
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)