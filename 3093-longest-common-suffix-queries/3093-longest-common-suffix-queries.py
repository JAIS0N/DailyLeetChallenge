class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        def better(new_idx, old_idx):
            if old_idx == -1:
                return True

            if len(wordsContainer[new_idx]) != len(wordsContainer[old_idx]):
                return len(wordsContainer[new_idx]) < len(wordsContainer[old_idx])

            return new_idx < old_idx

        def update(node, idx):
            if better(idx, node.best_index):
                node.best_index = idx

        for i, word in enumerate(wordsContainer):
            node = root
            update(node, i)

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                update(node, i)

        answer = []

        for query in wordsQuery:
            node = root

            for ch in reversed(query):
                if ch not in node.children:
                    break
                node = node.children[ch]

            answer.append(node.best_index)

        return answer