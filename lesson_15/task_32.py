
class Buffer:

    def __init__(self):
        self.list_of_marks = []

    def add(self, *a):
        self.list_of_marks.extend(a)
        while len(self.list_of_marks) - 5 >= 0:
            print(sum(self.list_of_marks[0:5]))
            self.list_of_marks = self.list_of_marks[5:]

    def get_current_part(self):
        return self.list_of_marks
