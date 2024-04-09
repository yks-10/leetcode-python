class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result =0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                tickets[i]=tickets[i]-1
                if tickets[k]==0:
                    result=result+1
                    break
                result=result+1
        return result

x=Solution()
print(x.timeRequiredToBuy([2,3,2],2))

