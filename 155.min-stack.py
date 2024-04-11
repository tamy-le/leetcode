#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = None

    def push(self, val: int) -> None:
        current_value = val
        if self.stack:
            if val < self.min_value:
                current_value = 2 * val - self.min_value
                self.min_value = val
        else:
            self.min_value = val
        self.stack.append(current_value)

    def pop(self) -> None:
        current_pop_value = self.stack.pop()
        if current_pop_value < self.min_value:
            self.min_value = 2 * self.min_value - current_pop_value

    def top(self) -> int:
        x = self.stack[-1]
        if x < self.min_value:
            return self.min_value
        return x

    def getMin(self) -> int:
        return self.min_value if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
# Time: O(1)
# Memory: O(1)

# Note: set is unordered data structure
# Note: can use simple math to keep previous value
