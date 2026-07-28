class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            if any(s[i] != char for s in strs[1:]):
                return shortest[:i]

        return shortest