class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if sandwiches:
                if sandwiches[0] == students[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                else:
                    if sandwiches[0] not in students:
                        return len(students)
                        break
                    else:
                        students.append(students.pop(0))
            else:
                return len(students)
                break
        return 0