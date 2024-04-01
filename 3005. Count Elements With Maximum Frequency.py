class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        res = {i: [] for i in range(1,len(nums)+1)}
        for i in nums:
            c = nums.count(i)
            res[c].append(i)
        result = []
        for i in list(res.values())[::-1]:
            if len(i)>0:
                result+=i
                break
        return len(result)

x=Solution()
print(x.maxFrequencyElements([1,1,1,1]))