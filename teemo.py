# Teemo Poision Leetcode Problem
from typing import List 
import pudb; pu.db
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        til = -1
        if duration == 0:
            return 0
        elif duration == 1:
            return len(timeSeries)
        for hit in timeSeries:
            if hit > til:  # Fresh hit
                count += duration
                til = hit + duration - 1
            elif hit + duration - 1 > til:
                count += (hit + duration-1) - til
                til = hit + duration - 1
        return count



testseries = [[0], [0,200], [1,2,3,4,5], [2,4,8,16], 
        [2,3,5,7,11,13,17], [x for x in range(10**4)]]
testdurations = [i for i in range(3,5)]
testdurations.append(10**7)
soln = Solution()

for series in testseries:
    for duration in testdurations:
        total = soln.findPoisonedDuration(series, duration)
        print("Series {} duration {} total time {}".format(None,duration,total))
        
