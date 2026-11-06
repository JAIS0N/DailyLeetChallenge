class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        
        # Sort queries along with their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        
        l = 0
        r = 0
        m = len(logs)
        
        for original_idx, q in sorted_queries:
            window_start = q - x
            window_end = q
            
            # Expand right pointer to include logs up to window_end
            while r < m and logs[r][1] <= window_end:
                server_counts[logs[r][0]] += 1
                r += 1
                
            # Shrink left pointer to exclude logs before window_start
            while l < m and logs[l][1] < window_start:
                server_counts[logs[l][0]] -= 1
                if server_counts[logs[l][0]] == 0:
                    del server_counts[logs[l][0]]
                l += 1
                
            # Servers with zero requests = total servers (n) - servers that got requests
            ans[original_idx] = n - len(server_counts)
            
        return ans
        