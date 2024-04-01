class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res =[]
        val = 1
        for i in range(len(nums)):
            print(nums[:i])
            print(",".join(nums[i:]))

x=Solution()
print(x.productExceptSelf([1,2,3,4]))


