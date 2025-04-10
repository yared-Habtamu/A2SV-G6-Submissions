# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

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
        emp_map={emp.id:emp for emp in employees}
        stk=[emp_map[id]]
        tot=0
        while stk:
            e=stk.pop()
            tot+=e.importance
            for neigh in e.subordinates:
                stk.append(emp_map[neigh])
        return tot
        