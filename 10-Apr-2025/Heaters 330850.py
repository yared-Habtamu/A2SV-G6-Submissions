# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def checker(x):
            i=0
            k=0
            while i<len(houses):
                if houses[i]<heaters[k]-x:
                    return False
                elif houses[i]>heaters[k]+x:
                    k+=1
                    if k==len(heaters):
                        return False
                else:
                    i+=1
            return True
        houses.sort()
        heaters.sort()
        l=0
        r=1000000000
        while l<=r:
            mid=(l+r)//2
            if checker(mid):
                r=mid-1
            else:
                l=mid+1
        return l

        