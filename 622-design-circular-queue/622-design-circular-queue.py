
class MyCircularQueue:
    # Time = O(1) amortized time for enqueue and dequeue
    # Space = O(N), N: the final capacity of the queue
    def __init__(self, k: int):
        # Initialize an empty array of size k
        self.array = [-1] * k
        self.capacity = k
        self.size = 0
        self.head = -1
        self.tail = -1
        
    # Resize the queue when the queue becomes full
    
    def enQueue(self, value: int) -> bool:
        # Queue is empty
        if self.size == 0:
            self.array[0] = value
            self.head = 0
            self.tail = 0
            self.size += 1
            return True
        else:
            # Queue is full
            if self.size == self.capacity:
                return False
            # If queue is not full, move the tail pointer to the right and set the new value where the tail now points
            self.tail = (self.tail + 1) % self.capacity
            self.array[self.tail] = value
            self.size += 1
            return True
        
    def deQueue(self) -> bool:
        # Queue is empty
        if self.size == 0:
            return False
        else:
            # Queue is of size == 1
            if self.size == 1:
                self.array[self.head] = [-1]
                self.head = -1
                self.tail = -1
                self.size = 0
            else:
                # Set the array[head] = -1 and increment the head ptr
                self.array[self.head] = -1
                self.head = (self.head + 1) % self.capacity 
                self.size -= 1
        return True
    
        

    def Front(self) -> int:
        # Queue is empty
        if self.size == 0:
            return -1
        return self.array[self.head]
        

    def Rear(self) -> int:
        # Queue is empty
        if self.size == 0:
            return -1
        return self.array[self.tail]
        

    def isEmpty(self) -> bool:
        return (self.size == 0)
        

    def isFull(self) -> bool:
        return (self.size == self.capacity)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()