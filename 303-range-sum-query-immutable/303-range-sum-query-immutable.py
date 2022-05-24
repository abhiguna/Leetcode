class NumArray:
    # Time = O(1)
    # Space = O(1)
    def __init__(self, nums: List[int]):
        # Build the prefix sums array
        self.size = len(nums)
        self.prefix_sums = [0] * self.size
        self.prefix_sums[0] = nums[0]
        for i in range(1, self.size):
            self.prefix_sums[i] = nums[i] + self.prefix_sums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        # Edge case: if left == 0, return self.prefix_sums[right]
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)