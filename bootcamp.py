class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+= val
        print('hi: ', self.name, 'your avg score is: ', sum/3)

S=Student("M Umar",[94,89,85])
print(S.name)
print(S.marks)
S.get_avg()

S.name = 'M Umar Bhettani'
S.get_avg()
