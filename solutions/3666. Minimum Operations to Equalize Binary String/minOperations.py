import collections
"""
You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. 
If it is not possible, return -1.


"""

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z_count = s.count('0')
        if z_count == 0:
            return 0
        
        # DSU to skip visited nodes for even and odd indices
        # We need nodes up to n + 2 to avoid index out of bounds
        p = [list(range(0, n + 3)), list(range(0, n + 3))]
        
        def find(par, i):
            root = i
            par_p = p[par]
            while par_p[root] != root:
                root = par_p[root]
            curr = i
            while par_p[curr] != root:
                next_i = par_p[curr]
                par_p[curr] = root
                curr = next_i
            return root

        q = collections.deque([z_count])
        dist = [-1] * (n + 1)
        dist[z_count] = 0
        
        # Mark the initial z_count as visited in DSU
        par_init = z_count % 2
        p[par_init][z_count] = find(par_init, z_count + 2)
        
        while q:
            z = q.popleft()
            d = dist[z]
            
            l = abs(z - k)
            r = min(z + k, 2 * n - z - k)
            par = (z + k) % 2
            
            curr = find(par, l)
            while curr <= r:
                if dist[curr] == -1:
                    dist[curr] = d + 1
                    if curr == 0:
                        return d + 1
                    q.append(curr)
                
                # Mark as visited (remove from future find calls)
                p[par][curr] = find(par, curr + 2)
                curr = find(par, curr)
        
        return -1




# Test cases:
if __name__ == "__main__":
    solution = Solution()
    s1 = "110"
    k1 = 1
    print(solution.minOperations(s1, k1))  # Output: 1

    s2 = "0101"
    k2 = 3
    print(solution.minOperations(s2, k2))  # Output: 2

    s3 = "101"
    k3 = 2
    print(solution.minOperations(s3, k3))  # Output: -1