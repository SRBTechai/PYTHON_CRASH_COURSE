# Dictionary is nothing but key value pairs
#dl = {}
#print(dl)

d2 = {"Sachin":"Biryani",
      "Kunal":"Sandwitch",
      "John":"Burger",
      "soham":{"A":"Book","B":"Pen","C":"Pencil"}}
print(type(d2))
print(d2)
# how to check the dictionary
print(d2["Sachin"]) # here sachin is a key and its value is Biryani
# how to add dictionary in to dictionary
print(d2["soham"]["C"]) # here the value of C in the key soham is Penci;

# how to add key and value in the dictionary

d2 ["Harshal"]= "Chicken Showrma"
print(d2)

# how to delete the key value from dictionary
del d2 ["Kunal"]
print(d2)

# how to make copy of the existing dictionary

d3 = d2.copy()

print(d3)
del d3["soham"]
print(d3)

# how to print all keys
print(d2.keys())

d3["nicola"]= "Capuchino"
print(d3)
print(d3.keys())
print(d3.items())


d4 = {"Water":"Paani","Tea":"Chaha","Breakfast":"Nasta","lunch":"Dupar cha jevan","Dinner":"Ratri cha jevan"}
print(d4)
print("Type the Word")
n1=input()
print("meaning of the", n1,"is", d4[n1])