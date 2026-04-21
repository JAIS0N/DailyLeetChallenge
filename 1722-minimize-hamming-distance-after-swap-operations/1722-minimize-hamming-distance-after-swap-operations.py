class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for a, b in allowedSwaps:
            union(a, b)

        # Build source counters grouped by root — ONE TIME
        src_groups = defaultdict(Counter)
        for i in range(n):
            src_groups[find(i)][source[i]] += 1

        # Single pass to count mismatches
        hamming = 0
        for i in range(n):
            root = find(i)
            t = target[i]
            if src_groups[root][t] > 0:
                src_groups[root][t] -= 1  # consume match
            else:
                hamming += 1              # group can't satisfy target[i]

        return hamming