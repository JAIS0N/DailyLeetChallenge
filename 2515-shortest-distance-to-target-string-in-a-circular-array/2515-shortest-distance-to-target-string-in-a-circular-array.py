class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        smallest=float('inf')
        for i, word in enumerate(words):
            if word==target:
                direct=abs(i-startIndex)
                circle=n-direct
                smallest=min(smallest,direct,circle)
        if smallest == float('inf'):  # target not found
            return -1
        
        return smallest