class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
                l += 1
            else:
                break
        result = nums[l] if nums[l] < nums[r] else nums[r]
        return result
        
# Time: O(log(n))
# Memory: O(1)