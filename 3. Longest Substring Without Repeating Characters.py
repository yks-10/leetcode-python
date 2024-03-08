class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result=""
        sample = strs[0]
        initial = 0
        b=False
        while initial<len(sample):
            for i in strs:
                if i[initial]==sample[initial]:
                    continue
                else:
                    b=True
                    break
            initial+=1
            if b:
                break
            else:
                result += sample[initial]
                initial+=1
        return result

x = Solution()
print(x.longestCommonPrefix(["flower","flow","flight"]))