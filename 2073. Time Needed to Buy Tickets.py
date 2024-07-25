class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result =0
        temp = tickets[k]
        for i in range(len(tickets)):
            if i<k:
                result = result+tickets[i]
            else:
                x = tickets[i]
                if x== temp:
                    result+=x
                elif x<temp:
                    result+=tickets[i]
                else:
                    result+=x

        return result

x=Solution()
print(x.timeRequiredToBuy([5,1,1,1],0))

