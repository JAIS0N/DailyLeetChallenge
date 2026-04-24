class MedianFinder:
    def __init__(self):
            self.small = []  # max-heap (inverted min-heap): lower half
            self.large = []  # min-heap: upper half    


    def addNum(self, num: int) -> None:
            # Push to max-heap (negate since Python only has min-heap)
            heapq.heappush(self.small, -1 * num)

            # Balance: ensure every num in small is <= every num in large
            if (self.small and self.large and
                    (-1 * self.small[0]) > self.large[0]):
                val = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, val)

            # Balance sizes: small can have at most 1 extra element
            if len(self.small) > len(self.large) + 1:
                val = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            if len(self.large) > len(self.small) + 1:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
            # Odd total: left heap has extra — its top is the median
            if len(self.small) > len(self.large):
                return -1 * self.small[0]
            # Odd total: right heap has extra — its top is the median
            if len(self.large) > len(self.small):
                return self.large[0]

            # Even total: median is average of both heap tops
            return (-1 * self.small[0] + self.large[0]) / 2

