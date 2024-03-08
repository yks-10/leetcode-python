class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        y = {i: arr.count(i) for i in arr}  # Count element occurrences efficiently
        values = sorted(y.values())  # Sort counts in descending order

        count = 0
        result = 0

        while count < k and values:
            current_count = values.pop(0)  # Remove and store the first value
            if count + current_count <= k:  # Check if count + current_count <= k
                count += current_count  # Update count
                result += 1  # Increment result
            else:
                break  # Break if count exceeds k
        return result

obj = Solution()
arr =[5,5,4]
k = 1
print(obj.findLeastNumOfUniqueInts(arr,k))
