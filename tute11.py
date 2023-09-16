# set
s= set()
#print(type(s))
#s_from_list= set([1,2,3,4,5,6,7,8,9])
#print(s_from_list)
#print(type(s_from_list))

# how to add elements in the set
s.add(1)
print(s)
s.add(2)
print(s) # Set stores only unique values

s1= s.union({1,2,3})
print(s,s1)
s1 = s.intersection({1,2,3})
print(len(s1))
s1.remove(2)
print(s1)