# in this we will try to find out the hypotenuse of the right angled triangle
# to find it we will use the formula : h=sqrt(a^2+b^2)

'''
import math

base=float(input("enter the base of the triangel(one of the sides that has a right angled triangle : )"))

prependicular=float(input("enter the prependicular of the triangel(the other side that has the right angle triangle on one of its edge : )"))

g=base**2+prependicular**2

h=math.sqrt(g)

print(f"The hypotenuse of the triangle is {h}")

'''

import math

a=int(input("enter side a : "))

b=int(input("enter side b : "))

h=math.sqrt(pow(a,2)+pow(b,2))

print(h)