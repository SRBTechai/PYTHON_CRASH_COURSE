# print("Hello how are you sachin")
# print("Hello how's are you sachin")
# print('\\Hello how are you sachin')
# print('Hello how are you sachin\nPlease update my channel dashboard')
# print('Hello how are you sachin\n\tPlease update my channel dashboard')
# print('\fHello how are you sachin Please update my channel dashboard')
# print('Hello how are you sachin\n\tPlease update my channel dashboard')

# variable is like a container in which we can store our data.

# var1 = "Hello how are you sachin Please update my channel dashboard"
# print(type(var1))
# var2= 333
# var3=3.33
# print(var2,var3)
# var2,var3 = var3,var2
# print(var2)

# Two Number addition Calculator

# print("Enter the first Value = ")
# n1 = int(input())
# print("Enter Second Value = ")
# n2 = int(input())
#
# print("Addition of your numbers is = ",int(n1+n2))

# Two Number Multiplication Calculator
# print("Wellcome to Multiplication Calculator\nPlease input first value =")
# n11 = int(input())
# print("Enter Second Value =")
# n12 = int(input())
#
# print("Result =",int(n11*n12))

# String
# mystr = "Hello how are you sachin. Please update my channel dashboard"
# print(mystr[:25])
# # print(mystr.find('sachin'))
# print(mystr.capitalize())
# mystr.upper()
# # print(mystr.upper())
# print(mystr.count("a"))
# print(mystr.isspace())
# print(mystr.endswith("sachin"))
# print(mystr.endswith("dashboard"))
# print(mystr.find('Please'))
# print(mystr[26:])
# print(mystr[25::2],"\n",mystr[:25])
# print(len(mystr))
# print(len(mystr[26:]))
# print(mystr.replace("dashboard","Report"))
# print(mystr)

# list = mutable (we can modify the list)

# veg = ["apple","banana","mango","orange","grapes","pineapple"]
# print(veg)
# print(len(veg))
# print(veg[0])
# print(veg[5])
# print(veg[2:])
# print(veg[:])
# print(veg)

# qty = [2,4,2,5,6,6]
# qty.sort()
# print(qty)
# qty.reverse()
# print(qty)
# print("Count of items = ",qty.count(6))
# print("Maximum value = ",max(qty))
# print("Minimum value = ",min(qty))
# qty.append(9) # it adds the value in the list at the end
# print(qty)

# empty = []
# print(empty)
# empty.append(2)
# empty.append(10)
# empty.append("sachin")
# empty.append("harshal")
# print(empty)
#
# empty.insert(3,555)
# empty.remove(555)
# empty.insert(4,"kunal")
# empty.pop()
# print(empty)

# Tuple = immutable (we cant modify tuple)

# tup1 = (1,)
# print(type(tup1))
# # tup1[1]
# print(tup1[0])
#
# a = 20
# b = 30
#
# print(a,b)
# # how to make a = 30 and b = 20
#
# a,b = b,a
# print(a,b)
#
# num = [1,3,4,5,6,7,8,3]
# num.copy()
# print(num)
# num.remove(3)
# print(num)
# num.clear()
# print(num)

# Dictionary : Dictionary is nothing but key value pairs
# d1 = {}
# print(d1)
#
# d2 = {"Honda":"City",
#       "Fiat":"Punto",
#       "Maruti":"Swift",
#       "VW":"Polo"}
# print(d2)
# print(type(d2))
# how to check dictionary

# d2["Honda"]
# print(d2["Honda"])
# print("Wellcome to the Car Dictionary\nPlease Enter Car Manufacture =")
# k1=str(input())
#
# print(k1,"Car name",d2[k1])
# d2["Tata"]="Safari"
# print(d2)
#
# del d2["Maruti"]
# print(d2)
#
# # lets make a copy of d2
# d3 = d2.copy()
# print(type(d3))
# print(d3)
#
# d3["Nissan"]= "Micra"
# print(d3.keys())
# print(d3.values())
#
# carm=[]
# carn=[]
#
# carm.append(d3.keys())
# carn.append(d3.values())
# print(carn,'\n',carm)

i = 0


# while (i<60):
#       print(i+1,end=" ")
#       i = i + 1

# while (i<20):
#       print("om namah shivay")
#       i = i+1

# while(True):
#       if i+1<5:
#             i=i+1
#             continue # continue will exicute while loop untill i<5
#       print(i+1,end=" ")
#       if (i == 50):
#             break # stops the loop
#       i = i+1
#
# print("Enter the input value = ")

while(True):
      i1 = int(input("Enter a Number\n"))
      if i1>100:
            print("Congrats you have Entered a Number Greater than 100")
            break
      else:
            print("Try again\n")
            continue

