class Solution:
    # Time = O(1)
    # Space = O(1)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        all_numbers = [num for num in range(1, 2001)]
        all_num_set = set(all_numbers)
        arr_set = set(arr)
        missing_set = all_num_set - arr_set
        return list(missing_set)[k-1]
                