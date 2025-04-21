#lets check the datatype of diffrent values

a=5
print("type of a:" , type(a) )

b=2.5
print("type of b:" , type(b) )

c="coding"
print("type of c:" , type(c) )

d=True
print("type of d:" , type(d) )



#Assigning Diffrent Variables

name = "Penguin"
age = 15
is_student=True
weight=38.5





print("Name:", name)
print("Data type of a is", type(name))

print("age:", age)
print("Data type of Age is" , type(age))

print("is_student :", is_student)
print("Data type of is_student is" , type(is_student))

print("Weight :", weight)
print("Data type of weight is" , type(weight))

#Type casting to convert the datatype of variables
print("/n After Type casting")
age= str(age)
print(age)
print("Data type of Age is" , type(age))

weight= int(weight)
print(weight)
print("Data type of Weight is" , type(weight))


#input a word
text = str(input("Enter a string"))

#Reverse String
#using step value as -1 to iterate in reverse
revText= text[ ::-1]
text=revText

print("Reverse of Given string is:")
print(text)
