class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        for i in sorted(strs):
            x = []
            y= [ (x.append(j)) for j in strs  if sorted(i) == sorted(j) ]
            if len(x) > 0:
                res.append(x)
                z = [strs.remove(z) for z in x]
        return res

obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(obj.groupAnagrams(strs))
