# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def checker(house,x,heat):
            i=0
            k=0
            while i<len(house):
                if house[i]<heat[k]-x:
                    return False
                elif house[i]>heat[k]+x:
                    k+=1
                    if k==len(heat):
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
            if checker(houses,mid,heaters):
                r=mid-1
            else:
                l=mid+1
        return l

        