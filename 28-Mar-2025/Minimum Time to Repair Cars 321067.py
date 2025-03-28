# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def tot_cars(self, minimum, ranks):
        cnt = 0
        for rank in ranks:
            cnt += math.isqrt(minimum // rank)
        return cnt

    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, max(ranks) * cars * cars

        while low <= high:
            mid = (low + high) // 2
            if self.tot_cars(mid, ranks) >= cars:
                high = mid - 1
            else:
                low = mid + 1

        return low