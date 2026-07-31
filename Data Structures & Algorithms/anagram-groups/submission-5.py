from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for i in range(len(strs)):
            sor = "".join(sorted(strs[i]))
            output[sor].append(strs[i])
        return list(output.values())