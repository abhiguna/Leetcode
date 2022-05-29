class Solution:
    # Time = O(N)
    # Space = O(N)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        min_sum = 0
        MOD = (10**9) + 7
        local_ans = [0] * N # Stores the min sum for subarrays upto idx i
        stack = deque() # (value, idx)
        
        for i in range(N):
            # Pop out all the elements that have a value greater or equal to curr element
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            
            # If the stack is not empty, the min sum ending at idx i is
            #   min sum ending at the previous smaller idx + (span * arr[i])
            if stack:
                span = i - stack[-1][1]
                local_ans[i] = local_ans[stack[-1][1]]
            else:
                span = i + 1
            
            local_ans[i] += span * arr[i]
            min_sum = (min_sum + local_ans[i]) % MOD
            
            # Add the current (value, idx) to the stack
            stack.append((arr[i], i))
        
        return min_sum