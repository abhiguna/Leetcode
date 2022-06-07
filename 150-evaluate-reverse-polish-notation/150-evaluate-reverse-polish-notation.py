class Solution:
    # Time = O(N)
    # Space = O(N)
    def evalRPN(self, tokens: List[str]) -> int:
        N = len(tokens)
        stack = []
        
        for t in tokens:
            # Operator
            if t in ["+", "-", "*", "/"]:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '+':
                    stack.append(op1 + op2)
                elif t == '-':
                    stack.append(op1 - op2)
                elif t == '*':
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))
            # Operand
            else:
                stack.append(int(t))
                
        return stack[-1]
        