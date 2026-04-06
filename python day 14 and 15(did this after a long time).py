# in this we will try to find out the hypotenuse of the right angled triangle
# to find it we will use the formula : h=sqrt(a^2+b^2)

'''
import math

a=float(input("enter side a : "))

b=float(input("enter side b : "))

h=math.sqrt(pow(a,2)+pow(b,2))

print(h)

'''

#now we are studying about if conditions 
#i was out in camp for ncc army attachment camp after coming home i had to handel many things 
# at ones and it overwemlmed me a so i slipped a bit but this splipping is also a part of my
# growth i think i am going to pick up speed soon . and am seem to be returning on track 
# slowly.

a=float(input("enter your weight in kg : "))
b=float(input("enter your height in meters : "))
bmi=a/(pow(b,2))
print(f"The bmi is {round(bmi,2)}")

if bmi<16:
    print("Severe Thinness")
elif bmi>=16 and bmi<=17:
    print("Moderate Thinness	")
elif bmi>=17 and bmi<=18.5:
    print("Mild Thinness")
elif bmi>=18.5 and bmi<=25:
    print("Normal")
elif bmi>=25 and bmi<=30:
    print("overwieght")
elif bmi>=30 and bmi<=35:
    print("ob-1")
elif bmi>=35 and bmi<=40:
    print("ob-2")
elif bmi>40:
    print("ob-3")
else :
    print("unfamilier case")
