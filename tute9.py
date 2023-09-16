# list

#grocery = ['Deo','Soap','Detergent','Thooth Paste','Shampoo',56]
#print(grocery)
#print(grocery[0])
#print(grocery[5])

numbers = [2,7,9,11,3]
#numbers.sort() # it sort the list of numbers in ascencding order (this function change the orignal list )
#numbers.reverse() # it sort the list of numbers in descending order
#print (numbers)

# Slicing
#print(numbers[0:5]) # this function doesnt change the orignal list.
#print(numbers[::2]) # it skips every second value from the list.
#print(max(numbers))
#print(min(numbers))

numbers.append(7) # APPEND ADD THE NEW VALUE AT THE END OF THE LIST
print(numbers)

#blank=[] # empty list
#print(blank)
#blank.append(2)  # here we have added the values in the empty list
#blank.append(7)
#blank.append("sachin")
#blank.append('@@')
#print(blank)

#numbers.insert(1,555) # here we have added the value after the 1 index value
#numbers.remove(555) # here we have removed the 555 value from the list.
#numbers.pop() # it removes the last element from the list
#print(numbers)

# mutable = can change   (List is a Mutable, we can update it)
# immutable = cant change( Tuple is immutable , we cant update it)

#tp = (1,) # to create tuple we have to write it in paranthesis, or for justsingle item just ad one comma at ehe end
#print(tp)
#tp[1]= 9

a=8
b=10
 # how to make a = 10 and b= 8
a,b = b,a

print (a, b)

num1 =[1,3,4,5,6,85,3,4]
num1.copy()
print(num1)
num1.remove(85)
print(num1)
num1.clear() # it clear all element from the list
print(num1)
