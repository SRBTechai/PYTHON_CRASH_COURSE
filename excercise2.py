# faulty calculator
# Operator
print("Wellcome to faulty calculator created By Sachin R B")
n1 = int(input("Enter First Number\n"))
n2 = int(input("Enter Second Number\n"))
operator = input("Select Operator Eg. *, +, / \n")

if n1==45 and n2==3 and operator =="*":
    print('Your Answer = 555')
elif n1==56 and n2==9 and operator =="+":
    print('Your Answer = 77')
elif n1==56 and n2==6 and operator =="/":
    print('Your Answer = 4')
elif operator =="*":
    n3 = n1*n2
    print(n3)
elif operator =="+":
    n4 = n1+n2
    print(n4)
elif operator =="/":
    n5 =n1/n2
    print(n5)
elif operator =="-":
    n6 =n1-n2
    print(n6)
elif operator =="%":
    n7 =n1%n2
    print(n7)
else:
    print("Error! Please check your input")
