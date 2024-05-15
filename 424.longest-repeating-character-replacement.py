from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result, max_frequent = 0, 0
        counter = Counter()
        for i in range(len(s)):
            result += 1
            counter[s[i]] += 1
            max_frequent = max(max_frequent, counter[s[i]])
            if result - max_frequent > k:
                counter[s[i - result + 1]] -= 1
                result -= 1
        return result
    
#Time: O(n)
#Memory: O(len(s))
