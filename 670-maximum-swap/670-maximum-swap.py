from collections import defaultdict

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        pos_swap = 0
        max_idx = -1
        max_val = '0'
        swap_found = False
        
        i = 0
        while i < len(num_list) - 1:
            if num_list[i] > num_list[i+1]:
                pos_swap = i + 1
            elif num_list[i] < num_list[i+1]:
                break
            i += 1
            print(pos_swap)
            
        if i == len(num_list) - 1:
            return int(''.join(num_list))
        if num_list[pos_swap] > num_list[i]:
            pos_swap = i
        i += 1
        max_idx = i
        max_val = num_list[i]
        
        while i < len(num_list):
            if num_list[i] >= max_val:
                max_idx = i
                max_val = num_list[i]
            i += 1
            
        if max_val > num_list[0]:
            num_list[0], num_list[max_idx] = num_list[max_idx], num_list[0]
        else:
            num_list[pos_swap], num_list[max_idx] =num_list[max_idx], num_list[pos_swap]
        return int(''.join(num_list))    
        
#         for i in range(0,len(num_list)-1):
#             if not swap_found and num_list[i] < num_list[i+1]:
#                 pos_swap += 1
#                 swap_found = True
#             if not swap_found and num_list[i] == num_list[i+1]:
                
#             if swap_found and i != pos_swap:
#                 if num_list[i] >= max_val:
#                     max_val = num_list[i]
#                     max_idx = i
#         print(swap_found, pos_swap)
#         if swap_found and num_list[-1] >= max_val:
            
#             max_val = num_list[-1]
#             max_idx = -1
        
            
            