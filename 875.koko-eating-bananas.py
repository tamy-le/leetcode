from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        def can_finish_eating(piles, k, h):
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile/k)
            return total_hour <= h
        while l <= r:
            current_number = (l+r)//2
            if can_finish_eating(piles, current_number, h):
                res = current_number
                r = current_number-1
            else:
                l = current_number + 1
        return res
    
# Time: O(log(n)*log(m)) m = max(piles)
# Complexity: O(1)