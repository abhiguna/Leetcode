from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while heap:
            freq_num = heapq.heappop(heap)
            result.append(freq_num[1])
        return result