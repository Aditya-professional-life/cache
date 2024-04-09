class Solution:
    def countStudents(self, students, sandwiches):
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                if sandwiches[0] not in students:
                    break
                else:
                    students.append(students.pop(0))
        return len(students)

sol = Solution()
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
result = sol.countStudents(students, sandwiches)
print(result)
