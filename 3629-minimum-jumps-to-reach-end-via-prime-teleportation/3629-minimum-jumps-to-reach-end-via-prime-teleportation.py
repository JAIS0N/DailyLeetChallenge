class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # Sieve to find smallest prime factor
        MAX_VAL = max(nums) + 1
        spf = list(range(MAX_VAL))  # smallest prime factor
        for i in range(2, int(MAX_VAL**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i*i, MAX_VAL, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # Group indices by prime factors of nums[j]
        prime_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            if val < 2:
                continue
            # Get unique prime factors of val
            seen = set()
            v = val
            while v > 1:
                p = spf[v]
                if p not in seen:
                    seen.add(p)
                    prime_to_indices[p].append(idx)
                while v % p == 0:
                    v //= p
        
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                
                # Adjacent moves
                for ni in [i - 1, i + 1]:
                    if 0 <= ni < n and not visited[ni]:
                        if ni == n - 1:
                            return steps
                        visited[ni] = True
                        queue.append(ni)
                
                # Prime teleportation: nums[i] must be prime
                val = nums[i]
                if val >= 2 and spf[val] == val:  # val is prime
                    p = val
                    if p in prime_to_indices:
                        targets = prime_to_indices.pop(p)  # consume the group
                        for j in targets:
                            if not visited[j]:
                                if j == n - 1:
                                    return steps
                                visited[j] = True
                                queue.append(j)
        
        return steps
        