#coding: utf-8

def Maths(b, a, c ):
    print("The equation of the quadratic root is given by ((b^2 +- 4ac)/2a)")
    print("X1 = ", format((b*b + 4*a*c)/2*a))
    print("X2 = ", format((b*b - 4*a*c)/2*a))
Maths(b=2, a=5, c=3)


calculus = lambda OTPrice: OTPrice + (OTPrice * 30/100)

print(calculus(2500),"$")