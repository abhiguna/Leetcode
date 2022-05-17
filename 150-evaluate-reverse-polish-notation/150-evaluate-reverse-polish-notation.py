# Time = O(N)
# Space = O(N)
class Solution:
    def evaluate(self, op1, op2, operator):
        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        else:
            # Integer division
            return int(op1/op2)

        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = set(["+", "-", "*", "/"])
        
        for token in tokens:
            if token not in ops:
                # Operand
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                operator = token
                stack.append(self.evaluate(op1, op2, operator))
        
        # Result will be in the top of the stack
        return stack.pop()