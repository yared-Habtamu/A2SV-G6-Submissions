# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        count=0
        arr=0
        for i in range(len(points)):
            if count==0 or points[i][0]>arr:
                count+=1
                arr=points[i][1]
        return count

            
        """
        :type points: List[List[int]]
        :rtype: int
        """
        