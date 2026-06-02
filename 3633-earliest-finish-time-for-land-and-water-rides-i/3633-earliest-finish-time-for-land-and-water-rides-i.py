class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float("inf")

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_finish = landStartTime[i] + landDuration[i]
                finish_after_water = max(land_finish, waterStartTime[j]) + waterDuration[j]

                water_finish = waterStartTime[j] + waterDuration[j]
                finish_after_land = max(water_finish, landStartTime[i]) + landDuration[i]

                ans = min(ans, finish_after_water, finish_after_land)

        return ans
        