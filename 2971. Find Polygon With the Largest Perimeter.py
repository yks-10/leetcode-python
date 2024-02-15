class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        res = -1
        total = 0
        for i in nums:
            if total> i:
                res = total +i
            total+=i
        return  res

obj=Solution()
nums = [1,12,1,2,5,50,3]
print(obj.largestPerimeter(nums))