class Empolyee:
    count=0
    def __init__(self,empId,name):
        self.id=empId
        self.name=name
        Empolyee.count+=1
    @staticmethod
    def check(id):
        digit=0
        word=0
        for i in range(len(id)):
            if(id[i].isdigit()):
                digit+=1
            else:
                word+=1 
        return(digit>0 and word>0)
    def getEmployeecount(self):
        return Empolyee.count
e=Empolyee("khik","ganesh")
print(Empolyee.check(e.id))