class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):
            # Add positions that can now jump to i
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1

            # Remove positions that are too far away to jump to i
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1

            dp[i] = s[i] == '0' and reachable > 0

        return dp[-1]