class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        value_to_indices = defaultdict(list)
        for i, value in enumerate(arr):
            value_to_indices[value].append(i)

        queue = deque([(0, 0)])  # index, steps
        visited = {0}

        while queue:
            index, steps = queue.popleft()

            neighbors = [index - 1, index + 1]

            # Same-value jumps
            neighbors.extend(value_to_indices[arr[index]])

            for nxt in neighbors:
                if nxt == n - 1:
                    return steps + 1

                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

            # Important: avoid revisiting same-value group again
            value_to_indices[arr[index]].clear()

        return -1
        