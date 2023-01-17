class Students:
    def setName(self,name):
        self.__name = name
        return
    def getName(self):
        return self.__name
    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber
        return
    def getRollNumber(self):
        return self.__rollNumber
c = Students()
c.setName(input("Enter a name "))
c.setRollNumber(int(input("Enter the roll number ")))
print(c.getName())
print(c.getRollNumber())