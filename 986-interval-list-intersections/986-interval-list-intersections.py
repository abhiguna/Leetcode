class Solution:
    # Time = O(M+N)
    # Space = O(1)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        M, N = len(firstList), len(secondList)
        # Edge case: M == 0 or N == 0
        if M == 0 or N == 0:
            return []
        
        intersections = []
        i, j = 0, 0
        while i < M and j < N:
            # No Overlap
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            # Overlap
            else:
                intersections.append([max(firstList[i][0], secondList[j][0]), \
                                     min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1
        
        return intersections