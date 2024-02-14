import time


class Solution(object):
    def destCity(self, paths):
        dumy = []
        if len(paths) == 1:
            return paths[0][-1]
        else:
            x = paths[0][-1]
            paths.remove(paths[0])
            while len(paths)>0:
                for j in paths:
                    if j[0] == x:
                        x=j[-1]
                        dumy = j
                        paths.remove(j)
                        break
        return dumy[-1]
obj = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

result = obj.destCity(paths)
print(result)