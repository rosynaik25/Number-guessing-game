import random

name=input("Enter your name:")
print("welcome!",name)

while True:
 Secret_number =random.randint(1, 1000)
 print ("Enter the numbers between 1to 1000")
 while True:
   guess=int(input("Enter the number you are guesssing:"))
 

   if guess<Secret_number:
    print("higher")
   elif guess>Secret_number:
    print("lower")
   else:
    print("Correct",Secret_number ,"you win")
    break


 choice =input("Do you want to play again?(yes/No)")
 if choice.lower() !="yes":
   print("Thanks for playing")
   break
