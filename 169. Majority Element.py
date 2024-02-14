class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        major = 0
        c = 0
        y=set(nums)
        for i in y:
            if nums.count(i) > c:
                major= i
                c=nums.count(i)
        return major