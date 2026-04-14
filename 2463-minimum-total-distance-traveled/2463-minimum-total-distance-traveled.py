class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort both to ensure the contiguous assignment property
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        # dp[i][j] is the min distance for first i robots using first j factories
        # Initialize with a very large value
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: 0 robots fixed takes 0 distance
        for j in range(m + 1):
            dp[0][j] = 0
            
        for j in range(1, m + 1): # For each factory
            f_pos, f_limit = factory[j-1]
            for i in range(n + 1): # For each number of robots handled so far
                # Option 1: Don't use this factory for any new robots
                dp[i][j] = dp[i][j-1]
                
                # Option 2: Use this factory to fix 'k' robots
                dist_sum = 0
                for k in range(1, min(i, f_limit) + 1):
                    # Robot being added is at index i-k
                    dist_sum += abs(robot[i-k] - f_pos)
                    
                    if dp[i-k][j-1] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i-k][j-1] + dist_sum)
                        
        return dp[n][m]