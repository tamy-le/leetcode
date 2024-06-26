#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        for token in tokens:
            result = token
            if not token.strip("-").isdigit():
                operand2 = number_stack.pop()
                operand1 = number_stack.pop()
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
        return number_stack.pop()


# @lc code=end
# Time: O(n)
# Memory: O(n)
