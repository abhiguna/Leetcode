class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {
            ')':'(', 
            ']':'[', 
            '}':'{'
        }
        for paren in s:
            if paren not in paren_dict: # Open paren
                stack.append(paren)
            else: # Close paren
                if not stack: # Empty stack
                    return False
                open_paren = stack.pop()
                if open_paren != paren_dict[paren]: # No match
                    return False
        return len(stack) == 0