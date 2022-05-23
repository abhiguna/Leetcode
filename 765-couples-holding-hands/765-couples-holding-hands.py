class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        h_map = {}
        # Initialize h_map<id_of_person, idx_location>
        for idx in range(N):
            h_map[row[idx]] = idx
            
        
        # Consider each sofa, keeping the left person in each sofa anchored and finding the corresponding
        #. right person based on the id of the left person in the current sofa
        num_swaps = 0
        for sofa in range(N//2):
            p_left = row[2*sofa]
            p_right = row[2*sofa + 1]
            p_right_expected = -1
            # If the id of the person on the left is even, then the person on the right must have an id one greater
            if p_left % 2 == 0:
                p_right_expected = p_left + 1
            else:
                p_right_expected = p_left - 1
            
            # If the person to the right of the current person is not the expected partner, we have to swap it
            #.  with the actual partner using the idx indicated by the hMap
            if p_right != p_right_expected:
                num_swaps += 1
                partner_loc = h_map[p_right_expected]
                # Swap
                row[2*sofa+1], row[partner_loc] = row[partner_loc], row[2*sofa+1]
                # Update h_map indices
                h_map[row[2*sofa+1]] = 2*sofa+1
                h_map[row[partner_loc]] = partner_loc
        
        return num_swaps
            
            
            
            