class Expression:
    def __init__(self,num1,num2,num3,ans):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.ans = num1 + num2 + num3
        print("The Sum of the three numbers is:",self.ans)
        
obj = Expression(4,5,9,4+5+9)