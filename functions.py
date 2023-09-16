# # There are two types of functions
# 1) Built in functions
# 2) User Defined functions


# a = 9
# b = 8
# c = sum((a,b)) # Built in Function
# print(c)


# user defined function
# a = str(input("Enter the name\n"))
# def function1(a):
#     print("Hello" ,a," you are in Function1",)
#
# print(function1(a))

# def function1(a,b):
#     print("hello you are in function1 ", a+b)
#
# function1(5,7)

def function2(a,b):
    """ This is the fuction which calculate average of a and b value """
    avg = (a+b)/2
    return avg

v= function2(5,9)
print(v)
print(function2.__doc__)   # this fuction print he doc string line which is present in the function.