class Solution:
    # Time = O(k*C(N, k))
    # Space = O(k)
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def helper(curr_element, num_chosen, slate):
            # Base case: exhausted all the elements
            if num_chosen == k:
                res.append(slate[:])
            # Backtracking case
            elif curr_element > n:
                return
            else:
                # Exclude the curr element
                helper(curr_element + 1, num_chosen, slate)
                
                # Include the curr element
                slate.append(curr_element)
                helper(curr_element + 1, num_chosen + 1, slate)
                slate.pop()
            return
        
        # Root manager
        helper(1, 0, [])
        return res
        