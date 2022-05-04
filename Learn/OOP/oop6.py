class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
       # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property.setter
    def gotmarks(self,sentence):
        # return self.name + ' obtained ' + self.marks + ' marks'
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks

st = Student("Jaki", "25")
st.name = "Anusha"
print(st.name)
print(st.gotmarks)