class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for sign in s:
            if sign in "([{":
                stack.append(sign)
            elif stack and stack[-1] + sign in ["()","[]","{}"]:
                stack.pop()
            else:
                return False
        return not stack
#Time: O(n)
#Memory: O(n)
#Device: Phone