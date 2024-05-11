class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_streak = 0
        for num in set_nums:
            if num + 1 not in set_nums:
                current_streak = 1
                lower = num - 1
                while lower in set_nums:
                    current_streak += 1
                    lower -= 1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak

#Memory: O(m) m uniqued numbes
#Time: O(n) 
