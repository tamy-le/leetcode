#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(numbers, target):
            result = []
            smaller_index, bigger_index = 0, len(numbers) - 1
            while smaller_index < bigger_index:
                current_sum = numbers[smaller_index] + numbers[bigger_index]
                if current_sum == target:
                    result.append([numbers[smaller_index], numbers[bigger_index]])
                    bigger_index -= 1
                    smaller_index += 1
                    while bigger_index > smaller_index and numbers[bigger_index] == numbers[bigger_index+1]:
                        bigger_index -= 1
                    while bigger_index > smaller_index and numbers[smaller_index] == numbers[smaller_index-1]:
                        smaller_index += 1
                elif current_sum > target:
                    bigger_index -= 1
                else:
                    smaller_index += 1
            return result

        sorted_numbs = sorted(nums)
        final_result = []
        index = len(sorted_numbs) - 1
        while index > 1:
            result  = twoSum(sorted_numbs[:index], -sorted_numbs[index])
            if result:
                result = [each + [sorted_numbs[index]] for each in result]
                final_result.extend(result)
            index-=1
            while index > 0 and sorted_numbs[index] == sorted_numbs[index+1]:
                index-=1
        return final_result

#Lesson learn: 
#1. append return none instead using non in place function such as addition
#2. using while to remove duplicate instead of inf variable (just for practical reason)
# @lc code=end

