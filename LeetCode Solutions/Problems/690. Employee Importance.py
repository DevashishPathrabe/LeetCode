"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        s = {}
        for employee in employees:
            s[employee.id] = employee
        queue = [id]
        value = 0
        while queue:
            employee_id = queue.pop()
            employee = s[employee_id]
            value += employee.importance
            queue.extend(employee.subordinates)
        return value