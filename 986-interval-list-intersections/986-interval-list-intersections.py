class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        M = len(firstList)
        N = len(secondList)
        i = 0
        j = 0
        intersections = []
        
        while i < M and j < N:
            i_overlaps_j = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            j_overlaps_i = secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]
            
            # Check overlap
            if i_overlaps_j or j_overlaps_i:
                intersections.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            
            # Look at next interval
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return intersections