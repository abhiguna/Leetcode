class Solution:
    
    def intersection(self, A, B):
        M = len(A)
        N = len(B)
        i = 0
        j = 0
        res = []
        while i < M and j < N:
            if A[i] < B[j]:
                i += 1
            elif B[j] < A[i]:
                j += 1
            else:
                # intersection
                res.append(A[i])
                i += 1
                j += 1
        return res
    
    # Time = O(N + M + O): N, M, O: len(arr1), len(arr2), len(arr3)
    # Space = O(1)
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        first = self.intersection(arr1, arr2)
        res = self.intersection(first, arr3)
        return res