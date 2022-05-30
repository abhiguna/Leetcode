class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def find_largest_rectangle(heights):
            N = len(heights)
            # Find the left and right spans for each idx i
            stack = deque()
            left_span = [0]*N
            
            for i in range(N):
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                
                if stack:
                    left_span[i] = i - stack[-1][1]
                else:
                    left_span[i] = i + 1
                stack.append((heights[i], i))
            
            stack = deque()
            right_span = [0]*N
            
            for i in range(N-1,-1,-1):
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                
                if stack:
                    right_span[i] = stack[-1][1] - i
                else:
                    right_span[i] = N - i
                stack.append((heights[i], i))
            
            max_area = 0
            for i in range(N):
                curr_area = heights[i] * (left_span[i] + right_span[i] - 1)
                max_area = max(max_area, curr_area)
            
            return max_area
        
        # Get the dimensions of the matrix
        M, N = len(matrix), len(matrix[0])
        histogram = [0] * N
        largest_rectangle = 0
        # We treat each row as the ground floor and build a histogram from the current row
        #.  we then use that to find the largest. rectangle in that histogram
        for row in range(M):
            for col in range(N):
                if matrix[row][col] == "1":
                    histogram[col] += 1
                # If matrix[r][c] == 0, we set the height to 0 since curr row is the 
                #. ground floor
                else:
                    histogram[col] = 0
            curr_area = find_largest_rectangle(histogram)
            largest_rectangle = max(largest_rectangle, curr_area)
        
        return largest_rectangle
                