# 1582. Special Positions in a Binary Matrix
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/submissions/1118731298?envType=daily-question&envId=2023-12-13

class Solution(object):
    def numsSpecial(self, mat):
        count = 0
        for i in mat:
            if i.count(1)>1:
                continue
            else:
                count1 = 0
                if 1 in i:
                    ind = i.index(1)
                else:
                    continue
                for j in mat:
                    if j[ind]==1:
                        count1=count1+1
                    if count1>1:
                        break
            if count1==1:
                count= count+1
        return count

# Create an instance of the Solution class
sol = Solution()

# Call the numSpecial method on the instance
mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
result = sol.numsSpecial(mat)

# Print the result
print(result)