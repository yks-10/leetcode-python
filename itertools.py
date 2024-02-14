from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        perm = permutations(nums)
        for i in list(perm):
            result = result+[list(i)]
        return result

obj=Solution()
nums = [1,2,3]
print(obj.permute(nums))