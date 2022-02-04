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
            print(idx, num, ms)
            if idx == ms:
                ms += 1
                continue
            else:
                break
        if len(heap) == 0:
            return int(''.join(num_list))
        else:
            while len(heap) != 0:
                
                item1 = heapq.heappop(heap)
                print(N - (-item1 % 10))
                print(ms, idx)
                print(item1)
                if (-item // 10) == (-item1 // 10):
                    idx = (N - (-item1 % 10))
                else:
                    break
            num_list[ms], num_list[idx] = num_list[idx], num_list[ms]
            print(int(''.join(num_list)))
            return int(''.join(num_list))
            
            