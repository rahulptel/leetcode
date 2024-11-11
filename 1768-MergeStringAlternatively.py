class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1

        i = 0
        result = ""
        while i < len(word1) and i < len(word2):
            result += word1[i]
            result += word2[i]
            i += 1

        if i < len(word1):
            result += word1[i:]
        else:
            result += word2[i:]

        return result
