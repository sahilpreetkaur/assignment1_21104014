#Q1
#first we will take input by the user
a= float(input("enter 1st no."))
b= float(input("enter 2nd no."))
c= float(input("enter 3rd no."))
#program to find AVERAGE of the input no.s
avg = (a+b+c)/3
print("average of no. is",avg)

#Q2
#taking input of gross income and dependants from user
Inc = float(input("enter your gross income"))
dep = int(input("enter no. of dependants"))

rate= 0.2
std_ded= 10000 #standard deduction in dollars

taxable_income = Inc - std_ded - (dep*3000)

tax= taxable_income*rate
print("your tax is",tax)

#Q3
student = [21104014, "sahilpreet", 'F', "electrical engineering",8.2]
print(student)

#Q4
marks = [96,90,80,99,100]
marks.sort() #inbuilt function for sorting
print(marks)

#Q5a
colour = ["Red", "Green", "White","Black", "Pink", "Yellow"]

colour.pop(3)
print (colour)

#Q5b
colour = ["Red", "Green", "White", "Black", "Pink","Yellow"]

#replacing Black and Pink with Purple
colour[3:5] = ["Purple"]
print (colour)
