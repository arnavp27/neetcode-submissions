class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_list = sorted(strs, key=len)
        prefix = ""
        for i in range(len(sorted_list[0])):
            for j in range(1, len(sorted_list)):
                if sorted_list[0][i] != sorted_list[j][i]:
                    return prefix
            prefix+=sorted_list[0][i]
        return prefix