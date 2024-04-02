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
            previous_smaller_number = float('inf')
            while smaller_index < bigger_index:
                current_sum = numbers[smaller_index] + numbers[bigger_index]
                if current_sum == target:
                    if numbers[smaller_index]!=previous_smaller_number:
                        result.append([numbers[smaller_index], numbers[bigger_index]])
                        previous_smaller_number = numbers[smaller_index]
                    bigger_index -= 1
                    smaller_index += 1
                elif current_sum > target:
                    bigger_index -= 1
                else:
                    smaller_index += 1
            return result

        sorted_numbs = sorted(nums)
        final_result = []
        previous = float('inf')
        
        for i in range(len(sorted_numbs) -1, 1, -1):
            if previous == sorted_numbs[i]:
                continue
            previous = sorted_numbs[i]
            result  = twoSum(sorted_numbs[:i], -sorted_numbs[i])
            if result:
                result = [each + [sorted_numbs[i]] for each in result]
                final_result.extend(result)
        return final_result

#Lesson learn: append return none instead using non in place function such as addition

# @lc code=end

