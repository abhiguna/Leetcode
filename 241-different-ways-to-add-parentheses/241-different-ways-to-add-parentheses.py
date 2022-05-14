class Solution:
    # Approach: Memoization
    
    # Time = O(Nth catalan number)
    # Space = O(Nth catalan number)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        N = len(expression)
        
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            
            # Base case -> no operators present, we only have numbers
            if expression[start:end+1].isdigit():
                return [int(expression[start:end+1])]
            
            # Recursive case -> compute the list of values if the string in range [start, end] is solved
            res = []
            for idx in range(start, end+1):
                # Operator found
                if not expression[idx].isdigit():
                    Lresults = helper(start, idx-1)
                    Rresults = helper(idx+1, end)
                    for lval in Lresults:
                        for rval in Rresults:
                            # Evaluate current expression
                            if expression[idx] == "+":
                                res.append(lval + rval)
                            elif expression[idx] == "-":
                                res.append(lval - rval)
                            else:
                                res.append(lval * rval)
            
            memo[(start, end)] = res
            return res
        
        return helper(0, N-1)
        