class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        try:
            while sandwiches[0] in students:
                temp = students[0]
                if temp == sandwiches[0]:
                    students.remove(temp)
                    sandwiches.remove(sandwiches[0])
                else:
                    students.remove(students[0])
                    students=students+[temp]
        except:
            return len(students)
        return len(students)



x= Solution()
print(x.countStudents([1,1,0,0],[0,1,0,1]))