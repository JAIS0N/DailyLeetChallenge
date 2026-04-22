class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result=[]
        for query in queries:
            found = False
            for word in dictionary:
                diff = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2:
                    found = True
                    break
            if found:
                result.append(query)
        
        return result