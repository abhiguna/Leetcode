class Solution:
    # Time = O(NlogM), M: max subarray sum, N: len(nums)
    # Space = O(1)
    def splitArray(self, nums: List[int], m: int) -> int:
        N = len(nums)
        
        def get_num_partitions(sub_sum):
            partitions = 1
            curr_sum = 0
            for n in nums:
                curr_sum += n
                if curr_sum > sub_sum:
                    partitions += 1
                    curr_sum = n
            return partitions
        
        start = max(nums)
        end = sum(nums)
        while start <= end:
            mid = start + (end - start) // 2
            partitions_needed = get_num_partitions(mid)
            if partitions_needed > m:
                # Move to the right since actual min maximum subarray sum is greater than mid if 
                # only m partitions given
                start = mid + 1
            else:
                # Move left since we can use more partitions and bring down the min maximum subarray sum
                end = mid - 1
        # At the end of binary search, start is going to point to the minimum max subarray sum
        return start