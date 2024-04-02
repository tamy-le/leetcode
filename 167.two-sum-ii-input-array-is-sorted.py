class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        smaller_index = 0
        bigger_index = len(numbers) - 1
        while smaller_index < bigger_index:
            current_sum = numbers[smaller_index] + numbers[bigger_index]
            if current_sum == target:
                return [smaller_index + 1, bigger_index + 1]
            elif current_sum > target:
                bigger_index -=1
            else:
                smaller_index +=1
        return -1

#Using iphone with safari browser