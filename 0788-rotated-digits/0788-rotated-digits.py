class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotate = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6'}
        count = 0
        
        for x in range(1, n + 1):
            s = str(x)
            if all(d in rotate for d in s) and any(rotate[d] != d for d in s):
                count += 1
        
        return count