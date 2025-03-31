# Last updated: 3/31/2025, 3:50:21 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, char in enumerate(strs[0]):
            for word in range(1, len(strs)):
                if i >= len(strs[word]):
                    return strs[0][0:i]
                if strs[word][i] != char:
                    return strs[0][0:i]
    
        return strs[0]
        