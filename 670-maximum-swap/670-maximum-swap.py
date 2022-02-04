import heapq

class Solution:
    def maximumSwap(self, num: int) -> int:
        heap = []
        heapq.heapify(heap)
        num_list = list(str(num))
        ms = 0
        N = len(num_list)
        
        for idx,num in enumerate(num_list):
            heapq.heappush(heap, -1*(int(num)*10 + N - idx))
        
        while len(heap) > 0:
            item = heapq.heappop(heap)
            idx,num = N - (-item % 10), (-item // 10)
            if idx == ms:
                ms += 1
                continue
            else:
                break
                
        if len(heap) == 0:
            return int(''.join(num_list))
        else:
            # Special case: dups allowed --> update idx
            while len(heap) != 0:
                item1 = heapq.heappop(heap)
                if (-item // 10) == (-item1 // 10):
                    idx = (N - (-item1 % 10))
                else:
                    break
            # swap
            num_list[ms], num_list[idx] = num_list[idx], num_list[ms]
            return int(''.join(num_list))
            
            