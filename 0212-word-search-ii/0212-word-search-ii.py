class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores complete word at end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word  # mark end of word

        res = []

        def dfs(r, c, node):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            ch = board[r][c]
            if ch not in node.children:  # prune: no word starts with this path
                return

            next_node = node.children[ch]

            if next_node.word:           # found a complete word
                res.append(next_node.word)
                next_node.word = None    # avoid duplicates

            board[r][c] = '#'            # mark visited (in-place, no path set)

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = ch             # restore (backtrack)

            # Prune empty Trie nodes (optimization)
            if not next_node.children:
                del node.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res