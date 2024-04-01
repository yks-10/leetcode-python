class Decorator:

    def Riser(func):
        def rise(self, a):
            a=a*2
            return func(self, a)
        return rise

    @Riser
    def Add(self,a,b):
        return a+b

class Calculator(Decorator):
    def multi(a):
        x = Decorator.Riser(a)
        return x*a
x=Calculator
rise=x.Riser(5)
y=Calculator.multi(rise)
print(y)
