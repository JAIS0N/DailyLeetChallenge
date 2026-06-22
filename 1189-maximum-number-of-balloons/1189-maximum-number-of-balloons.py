class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for char in text:
            count[char] = count.get(char, 0) + 1

        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )
        