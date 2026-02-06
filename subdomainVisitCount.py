class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hash_map = defaultdict(int)

        visited = [] 
        for domain in cpdomains:

            num, domain = domain.split(" ")

            hash_map[domain] += int(num)
            r = 0
            n = len(domain)
            while r < n:
                if domain[r] == '.': 
                    hash_map[domain[r+1:]] += int(num)
                    domain = domain[r+1:]
                    n = len(domain)
                    r = 0

                r += 1
            
            
        for key, val in hash_map.items():
            visited.append(str(val)+" "+key)


        return visited

