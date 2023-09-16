# n = 19
# no_of_guess = 1
# print("No of Guesses is limited to only 9 times")
#
# while(no_of_guess<=9):
#     inp = int(input("Enter the Number\n"))
#     if inp <19:
#         print("You Entered less number please enter greater number\n")
#     elif inp >19:
#         print("You Entered greater number please enter lesser number\n")
#     else:
#         print("Congrats You Won\n")
#         print(no_of_guess,"No of guesses you took to finish.")
#         break
#     print(9-no_of_guess,"No. of Guess left")
#     no_of_guess = no_of_guess+1
# if(no_of_guess>9):
#     print("Game Over")


cname = "josh"
noa = 1
print('no. of attempt limited to only 4')

while (noa<=4):
    ii = str(input("Enter Customer Name:\n"))
    if ii !="josh":
        print("You entered incorrect answer")
        print(noa,"attempts you take")
        print(4-noa,"attemps remains")
        noa = noa+1
        continue

    else:
        print("congratulation")
        print(noa,"no of guesses you taken")
        break

    print(4-noa,"No of guesses remain")
    noa = noa + 1
if noa>4:
    print("game over")
