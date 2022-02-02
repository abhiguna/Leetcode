# Date: 2/2/22
# 30m 2
class Solution:
    # Time = O(m + n)
    # Space = O(m + n)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        idx1 = 0
        idx2 = 0
        intersections = []
        while idx1<m and idx2<n:
            start = max(firstList[idx1][0], secondList[idx2][0])
            end = min(firstList[idx1][1], secondList[idx2][1])
            if start <= end:
                intersections.append([start, end])
            
            if firstList[idx1][1] <= secondList[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        return intersections
        
            
            
            