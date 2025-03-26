# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def tot_days(cap):
            tot=0
            count=1
            for i in range(len(weights)):
                tot+=weights[i]
                if tot>cap:
                    count+=1
                    tot=weights[i]
                if count>days:
                    return False
            return True

        l=max(weights)-1
        r=sum(weights)
        while (l+1)<r:
            mid=(l+r)//2
            if not tot_days(mid):
                l=mid
            else:
                r=mid
        return r