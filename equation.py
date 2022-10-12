'''a = int(input("a: "))

b = int(input("b: "))

c = int(input("c: "))
x = (-b)
xx = (b**2 - 4*a*c)
xxx = (xx)**0.5
xxxx= (2*a)

x1 = (x + xxx)/xxxx
x2 = (x - xxx)/xxxx
print('x1:', x1 ,'\n', 'x2:', x2)
#print((a)+(a))'''


class passe():
    passwor =[]
    mypas = input('write password:')
    def __init__(self,**kwargs):
        super.__init__(**kwargs)
        self.passs()
        print(1)
        if len(self.passwor) != 1:
            self.retrive()
    def passs(self):
        self.passwor.append(self.mypas)
    def retrive(self):
        for i in self.passwor:
            print(i)



