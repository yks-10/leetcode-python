class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = n%2
        y = 2**x
        if y == n:
            return True
        else:
            return False

obj = Solution()
print(obj.isPowerOfTwo(1))