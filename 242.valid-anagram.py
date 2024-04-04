class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        dict_s = Counter(s)
        dict_t = Counter(t)
        return dict_s == dict_t
        
#By phone
#Time: O(n+n)
#Memory: O(n+n)