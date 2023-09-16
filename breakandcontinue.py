# break and continue statements
i= 0

# while(i<45):
#     print(i+1,end=" ")
#     i = i+1

# while (True):
#     if i+1<5:
#         i=i+1
#         continue  # continue will exicute while loop untill i<5
#     print(i+1 ,end=" ")
#     if (i == 44):
#         break    # stops the loop
#     i = i+1

# print("Enter the Input Value = ")
# i1 = int(input())

while (True):
    i1 = int(input("Enter a Number\n"))
    if i1>100:
        print("Congrats you have entered a number greater than 100")
        break
    else:
        print("Try again\n")
        continue
