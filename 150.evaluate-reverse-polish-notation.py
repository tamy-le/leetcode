#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        result = 0
        for token in tokens:
            if token.strip("-").isdigit():
                number_stack.append(int(token))
            else:
                operand2 = number_stack.pop()
                operand1 = number_stack.pop()
                result = 0
                match token:
                    case "*":
                        result = operand1 * operand2
                    case "/":
                        result = operand1 / operand2
                    case "+":
                        result = operand1 + operand2
                    case "-":
                        result = operand1 - operand2
                number_stack.append(int(result))
        return number_stack[-1]


# @lc code=end
# Time: O(n)
# Memory: O(n)
