class Solution:
    # Time = O(m^2*n), n: len(cpdomains), m: avg. length of cpd
    # Space = O(m*n)
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp_map = defaultdict(int)
        
        # Process subdomains
        for cpd in cpdomains:
            tmp = cpd.split(" ")
            count = int(tmp[0])
            domain = tmp[1]
            subdomain = domain.split(".")
            m = len(subdomain)
            for i in range(m):
                cp_map[".".join(subdomain[i:m])] += count
        
        res = []
        # Build the results
        for sub, count in cp_map.items():
            cp = [str(count), sub]
            res.append(" ".join(cp))
        
        return res
        
            