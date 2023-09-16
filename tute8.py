# string
mystr = "Sachin is a data scientist"
print(mystr[0:3])

# string slicing
# S a c h i n
# 0 1 2 3 4 5 6
#

# if we want to slicethe first 3 letters of the word then we will
# write like this :
# print (mystr[0:3])

print(len(mystr))
print(mystr[-26])

print(mystr[0:6:2])

print(mystr[:6])
slc = 'My name is sachin Rajendera bagul lives in pune maharashtra'

print(slc)
print(len(slc))
print(slc[0:11])
print(len(slc[1:]))

print(slc[0::2])

ss = 'hello sachin good morning how are you'


print(ss)
print("the total length of the string is", len(ss))
print(ss[0:10])
print(ss[0::2])
print(ss[0::1])

print(ss[-1:])
print(ss[:-10])

print(ss.endswith('you')) # it give the bool value if the string endes with the "you". if not it will give result False.
print(ss.count("o")) # it gives you the count "o" character how much time it is repeated in the string.
print(ss.capitalize()) # it capitalze the string.
print(ss.replace("hello","Shri")) # it replace the value in the string.
print(ss.upper()) # it make string upppercase.
print(ss.rfind("good")) # it show the location of that word in the string.
print(ss.isspace())
print(ss.find('sachin'))