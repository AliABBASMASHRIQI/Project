# import random
# print("Hello World")

# x=2.0
# y=int(x)
# a='Ali'

# print(x,y)

# myList = [1.2,3,4,5,"Streintg"]
# print(myList)

# print (random.choice(myList))

# b=list(a)
# print(b,"My new List")

# c=b[0:1]
# print(c,"mutated List",b,"original")

# c.append("lI")

# b.extend(c)
# print(b)

# b.remove("lI")
# print(b)

# print(len(b))


# def sleep_in(weekday, vacation):
#  if weekday == False or vacation == True :
#   return True
#  else:
#   return False
 
 
# for i in range(len(b)):
#   print(b[i])


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# def okay(**kids):
#    print( "okay " + kids["kids1"])



# okay(kids1="Ali",kids2="Ali")


# def monkey_trouble(a_smile, b_smile):
#   if a_smile==True and b_smile == True or a_smile==False and b_smile == False:
#     return True
#   else:
#     return False


# def experimenatl_func(a,b):
#   print(a+b,"The print")

# experimenatl_func(True,False)

# def string_times(str, n):
#   result_string=""
#   for x in str:
#     result_string=result_string+x
  
#   return result_string



# def first_Input():
#     abc = input("Enter your name\n")
#     print(abc)

# first_Input()

#f=open('taskFile.txt')
#print(f.read())

import re

text = "My name is Ali Abbas and my phone Number is (94141-58857) or it is 6376332312 whatever you decide Ali Abbas okay"
patern = re.search("Ali Abbas",text)
patern2 = re.split("Ali Abbas",text)
patern3 = re.findall("Ali Abbas",text)
print(patern.span(),"Span")
print(patern.group(),"get the value ")
print(patern2)
print(patern3)
print(type(patern))