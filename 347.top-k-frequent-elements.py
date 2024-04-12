#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        heap = []
        for number, count in counter.items():
            heapq.heappush(heap, (-count, number))
        return [heapq.heappop(heap)[1] for _ in range(k)]


# @lc code=end
# Time: O(nlogn) still the same but better because sort can reach n^2 but heap is stable
# Memory: O(n)
