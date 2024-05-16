from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        counter_s1 = Counter(s1)
        counter_s2 = Counter(s2[:n1])
        
        for i in range(n1, n2):
            if counter_s1 == counter_s2:
                return True
            counter_s2[s2[i]] += 1
            counter_s2[s2[i - n1]] -= 1
            if counter_s2[s2[i - n1]] == 0:
                del counter_s2[s2[i - n1]]
        
        return counter_s1 == counter_s2

#Time: O(26n)
#Memory: O(26*2) -> O(1)
