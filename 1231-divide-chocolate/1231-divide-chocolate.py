class Solution:
    # Time = O(Nlog(S-M)), S: sum(sweetness), M: max(sweetness), N: len(sweetness)
    # Space = O(1)
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        N = len(sweetness)
        start = min(sweetness)
        end = sum(sweetness)
        
        def get_num_pieces(target_min_sweetness):
            num_pieces_needed = 0
            total_sweetness = 0
            for s in sweetness:
                total_sweetness += s
                if total_sweetness >= target_min_sweetness:
                    # Increment the total number of pieces created that achieve the target min sweetness
                    num_pieces_needed += 1
                    # Restart the sweetness level
                    total_sweetness = 0
            return num_pieces_needed
            
        while start <= end:
            mid = start + (end - start) // 2
            # We have to get the number of pieces such that each piece has a total sweetness of at least mid
            num_pieces_needed = get_num_pieces(mid)
            # Min sweetness is too high, each piece is longer than expected
            if num_pieces_needed < k + 1:
                end = mid - 1
            # Achieved target min sweetness, we have to now search if a higher min sweetness is achievable
            #.   with k + 1 pieces
            else:
                start = mid + 1
        
        # The end ptr points to the max minimum sweetness achievable with k + 1 pieces
        return end