class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in range(len(strs)):
            output += str(len(strs[i])) + "#" + strs[i]
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        list_of_nums = ""
        i = 0

        while i != len(s):
            while s[i] != "#":
                list_of_nums += str(s[i])
                i += 1
                print(i)
            output.append(s[i+1:i+1+int(list_of_nums)])
            i += 1+int(list_of_nums)
            list_of_nums = ""
                    
        return output
