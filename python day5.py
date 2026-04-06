# Finding the area of a rectangle

#length=int(input("Enter the length of the rectangle :  "))
#width=int(input ("Enter the width of rectangle : "))

#using float is better than using int in this case

'''
length=(float(input("Enter the length of the rectangle in cm :  ")))
width=float(input ("Enter the width of rectangle in cm : "))

area= length*width

print(f"area of the rectangle is {area} cm²")

#cm² k liye numlock+alt+0178

'''

#making a shopping cart programe
#price , items ,quantity 
#day 6 ko continue

item=input("enter the name of the item : ")
price =float(input("Enter the price of the item : "))
quantity=int(input("Enter the number of items : "))

price_to_pay = price*quantity 

print(f"You need to pay {price_to_pay} $ for {quantity} {item}.")
