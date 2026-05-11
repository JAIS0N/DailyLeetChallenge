class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        visiting = set()  # currently in DFS path
        visited  = set()  # fully processed, confirmed safe

        def dfs(node):
            if node in visiting:  # cycle detected
                return False
            if node in visited:   # already confirmed safe
                return True

            visiting.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        return all(dfs(i) for i in range(numCourses))