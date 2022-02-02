from collections import defaultdict

class Solution:
    # Time = O(n*klogk) n=length of array of strings, k=length of each string
    # Space = O(n*k) 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        for s in strs:
            key = "".join(sorted(list(s)))
            groupings[key].append(s)
        return [anagram for anagram in groupings.values()]
    