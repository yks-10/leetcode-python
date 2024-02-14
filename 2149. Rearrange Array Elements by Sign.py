class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = [i for i in nums if i>=0]
        negative = [i for i in nums if i<0]
        result =[]
        result1 = [[result.append(positive[i]), result.append(negative[i])] for i in range(len(positive))]
        return result

obj = Solution()
nums = [3,1,-2,-5,2,-4]
result = obj.rearrangeArray(nums)
print(result)