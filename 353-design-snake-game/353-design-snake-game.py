from collections import deque

# Date: 2/18/22
# 20m 3
class SnakeGame:

    # next_position --> (r, c) : local var
    # curr_position
    # body_positions --> queue()
    # body_loc --> set() easy lookup
    # food_queue --> queue()
    # score --> int
    # width --> check boundary
    # height --> check boundary
    
    # Time: O(1)
    # Space = O(1)
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0, 0)])
        self.snake_set = {(0,0) : 1}
        self.width = width
        self.height = height
        self.food = food
        self.food_idx = 0
        self.movement = {'U':[-1,0], 'L':[0,-1], 'R':[0,1], 'D':[1,0]}

    # Time = O(1)
    # Space = O(W*H + N), W = width, H = height, and N = len(food)
    def move(self, direction: str) -> int:
        newHead = (self.snake[0][0] + self.movement[direction][0],
                  self.snake[0][1] + self.movement[direction][1])
        
        crosses_boundary1 = newHead[0] < 0 or newHead[0] >= self.height
        crosses_boundary2 = newHead[1] < 0 or newHead[1] >= self.width
        bites_itself = newHead in self.snake_set and newHead != self.snake[-1]
        
        if crosses_boundary1 or crosses_boundary2 or bites_itself:
            return -1
        
        next_food_item = self.food[self.food_idx] if self.food_idx < len(self.food) else None
        if next_food_item and next_food_item[0] == newHead[0] and   next_food_item[1] == newHead[1]:
            self.food_idx += 1
        else:
            tail = self.snake.pop()
            del self.snake_set[tail]
        
        self.snake.appendleft(newHead)
        self.snake_set[newHead] = 1

        return len(self.snake) - 1
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)