class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(string)}*{string}" for string in strs])

    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index < len(s):
            current_len = ""
            while s[index] != "*":
                current_len += s[index]
                index += 1
            current_len = int(current_len)
            start_word = index + 1
            end_word = start_word + current_len
            res.append(s[start_word:end_word])
            index = end_word
        return res


# Time: O(n)
# Memory: O(1) result list not counted
