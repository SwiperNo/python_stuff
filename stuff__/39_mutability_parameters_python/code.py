from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

