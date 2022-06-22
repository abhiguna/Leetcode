from collections import *
import math

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        adj_list = defaultdict(list)
        
        def build_graph():
            for r in regions:
                for i in range(1, len(r)):
                    adj_list[r[0]].append(r[i])
        
        build_graph()
        smallest_region = [None]
        min_size = [math.inf]
        
        def dfs(src):
            (r1, r2) = (src == region1, src == region2)
            size[0] += 1
            
            # Base case: leaf node
            if len(adj_list[src]) == 0:
                return (r1, r2)
            
            # General case: internal node
            for nei in adj_list[src]:
                (r1_nei, r2_nei) = dfs(nei)
                r1 = r1 or r1_nei
                r2 = r2 or r2_nei
            
            if (r1, r2) == (True, True) and size[0] < min_size[0]:
                smallest_region[0] = src
                min_size[0] = size[0]
            
            return (r1, r2)
        
        for v in list(adj_list.keys()):
            size = [0]
            dfs(v)
            
        return smallest_region[0]