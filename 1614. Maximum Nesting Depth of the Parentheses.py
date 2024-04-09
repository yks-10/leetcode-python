class Solution:
    def maxDepth(self, s: str) -> int:
        o ="("
        c = ")"
        result = []
        start =0
        end=0
        for i in s:
            if i==o:
                start+=1
            elif i==c:
                result.append(start)
                start-=1
        return max(result)


x=Solution()
print(x.maxDepth("(1)+((2))+(((3)))"))