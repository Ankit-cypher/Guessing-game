import random
guess = int(input("Try "))
jackpot = random.randint(1,100)
counter = 1 
while guess != jackpot:
  if guess<jackpot:
    print("Guess higher")
  
  else:
    print("Guess lower")
  guess = int(input("Try ")) 
  counter+=1

print("Correct")
print("You took",counter, "attempts" )

