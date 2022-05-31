class Solution:
    # Approach 2: Merge Sort -> stable, NOT in-place
    
    # Time = O(NlogN) -> T(N) = 2T(N/2) + cn
    # Space = O(N)
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(start, mid, end):
            i, j = start, mid+1
            aux = []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    aux.append(nums[i])
                    i += 1
                else:
                    aux.append(nums[j])
                    j += 1
            
            while i <= mid:
                aux.append(nums[i])
                i += 1
            
            while j <= end:
                aux.append(nums[j])
                j += 1
            
            nums[start:end+1] = aux
            return
        
        def merge_sort(start, end):
            # Base case
            if start >= end:
                return
            
            mid = start + (end-start) // 2
            merge_sort(start, mid)
            merge_sort(mid+1, end)
            merge(start, mid, end)
            return
        
        
        merge_sort(0, len(nums)-1)
        return nums
        
        