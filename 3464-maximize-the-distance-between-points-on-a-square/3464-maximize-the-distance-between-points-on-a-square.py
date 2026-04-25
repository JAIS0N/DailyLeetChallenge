import bisect
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def to_arc(x, y):
            if y == 0:     return x
            if x == side:  return side + y
            if y == side:  return 2 * side + (side - x)
            return         3 * side + (side - y)

        arc = sorted(to_arc(x, y) for x, y in points)
        n = len(arc)
        total = 4 * side

        def can_place(d):
            for start in range(n):
                count = 1
                cur = arc[start]
                first = cur
                wrapped = False
                i = start

                for _ in range(k - 1):
                    target = cur + d
                    if not wrapped:
                        pos = bisect.bisect_left(arc, target, i + 1, n)
                        if pos < n:
                            cur = arc[pos]
                            i = pos
                        else:
                            # wrap
                            wt = target - total
                            pos = bisect.bisect_left(arc, wt, 0, start)
                            if pos >= start:
                                break
                            cur = arc[pos]
                            i = pos
                            wrapped = True
                    else:
                        pos = bisect.bisect_left(arc, target, i + 1, start)
                        if pos >= start:
                            break
                        cur = arc[pos]
                        i = pos
                    count += 1

                if count == k:
                    # Check gap from last back to first
                    gap = (first - cur) % total
                    if gap >= d:
                        return True
            return False

        lo, hi, ans = 1, 2 * side, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans