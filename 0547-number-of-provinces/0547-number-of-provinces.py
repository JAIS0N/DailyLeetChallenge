class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                parent[rootY] = rootX

        # Traverse adjacency matrix
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        # Count unique roots
        provinces = set()

        for i in range(n):
            provinces.add(find(i))

        return len(provinces)