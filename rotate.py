class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= 0:
            k=k%len(nums)
            nums[:] = nums[-k:] + nums[:-k]



obj = Solution()

nums = [1,2,3,4,5,6,7]
k = 3

obj.rotate(nums, k)