# Last updated: 4/10/2025, 1:06:24 AM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for i, char in enumerate(word1):
            merged.append(char)
            if (i < len(word2)):
                merged.append(word2[i])

        if len(word2) > len(word1):
            i = len(word1)
            while i < len(word2):
                merged.append(word2[i])
                i += 1
        
        return "".join(merged)
            