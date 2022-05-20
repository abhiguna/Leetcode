class Solution:
    # Time = O(logN)
    # Space = O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        
        # Special case: all elements are <= target
        return letters[start % len(letters)]