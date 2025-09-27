import random
computer = random.choice([-1,0,1])
youstr = input("enter the string : ")
youdict = {"stone" : -1,"paper" : 0,"scissor" : 1}
reverseDict = {-1 : "stone", 0: "paper",1 : "sci"}

you = youdict[youstr]

print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer == you):
    print("it's draw")

elif(computer == -1 and you == 0 ):
    print("you win")

elif(computer == 1 and you == -1):
    print("you win")

elif(computer == 0 and you == 1):
    print("you win")

else:
    print("you lose")
