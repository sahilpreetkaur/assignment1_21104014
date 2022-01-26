#QUESTION 1 ---->
string1 = "Python is a case sensitive language"

#option a
print (len(string1)) #inbuilt function to find length

#option b
print (string1[::-1]) 

#option c
string2 = string1[10:27]
print (string2)

#option d
print (string1.replace("a case sensitive","object oriented"))

#option e
print (string1.find("a"))

#option f
print (string1.replace(" ",""))



#QUESTION 2 ---->
#storing our data
name = "Sahilpreet kaur"
SID = 21104014
dep_name = "Electrical"
CGPA = 9.8

print ("Hey,",name,"Here!\nMy SID is",SID ,"\nI am from",dep_name, "department and my CGPA is", CGPA)



#QUESTION 3 ---->
a = 56 
b = 10

#option a
print (a&b)

#option b
print (a|b)

#option c
print (a^b)

#option d
print (a<<2, b<<2)

#option e
print (a>>2, b>>4)



#QUESTION 4  ---->
#taking user input
a = float(input("enter 1st no."))
b = float(input("enter 2nd no."))
c = float(input("enter 3rd no."))

#conditions for a no. to be greatest
if (a>b and a>c):
    print (a)
elif (b>a and b>c):
    print (b)
else:
    print (c)
    
#alternatively:- this can also be done by max function
#print (max(a,b,c))


#QUESTION 5 ---->
str1= input("enter anything\n") 

if "name" in str1 :      #condition to check if name is in string
    print ("yes")
else:
    print("no")
    


#QUESTION 6 ---->
#taking user input
a = int(input("enter first side of triangle "))
b = int(input("enter second side of triangle "))
c = int(input("enter third side of triangle "))

if (a>=(b+c) or b>=(a+c) or c>=(a+b)):      #test 
    print ("No")
else:
    print ("Yes")