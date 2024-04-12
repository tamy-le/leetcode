#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def counter(numbs: List[int]) -> dict:
            dictionary = {}
            for numb in numbs:
                dictionary[numb] = dictionary.get(numb, 0) + 1
            return dictionary

        nums_counter = counter(nums)
        sorted_items = sorted(nums_counter.items(), key=lambda item: item[1])
        unique_count = len(sorted_items)
        return [key_value[0] for key_value in sorted_items[unique_count - k :]]


# @lc code=end
# Time: O(nlogn) Worst case is when nums has no duplicate numbers
# Memory: O(n)
