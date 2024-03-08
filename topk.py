class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        x = {}
        for i in set(nums):
            if nums.count(i) in x:
                x[nums.count(i)].append(i)
            else:
                x[nums.count(i)] = [i]
        # res = list(x.values())
        # res = [item for sublist in res for item in sublist]
        arr = sorted(x, key=lambda y: x[y], reverse=True)
        return arr[:k]

x=Solution()
print(x.topKFrequent([1,2],2))