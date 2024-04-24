class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)-1):
            stack.append(i)
            if temperatures[i] < temperatures[i+1]:
                while stack and temperatures[i+1] > temperatures[stack[-1]]:
                    index = stack.pop()
                    result[index] = i + 1 - index
        return result
    
# Time: O(n) Worst case is all preceding numbers smaller than their next number
# Memory: O(n) if not count result