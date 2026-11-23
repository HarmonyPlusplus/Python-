# a = 20 
# b = 50

# if a < b:
#     print("A is less than b")

# if a > b:
#     print("A is not greater than B")    
# else:
#     print("B is greater than A")    


# jamb_score = 179

# if jamb_score >= 100:
#     print("Admitted")
# elif jamb_score == 99:
#     print("Youre Almost there") 
# else:
#     print("Not admitted")   

# # Nested if
# age = 19
# score = 200

# if age >= 18:
#     if score >= 100:
#         print("Youve been Admitted")
# else: 
#     print("Later Nau")  


# fruits = ["Orange", "Mango", "Coco"]


# for fruit in fruits:
#     print(fruit)

# for i in range(1, 10):
#     print(i)

# for i in range(10):
#     print(i)


# num = 1

# while num < 10:
#     print("Harmony")
#     num += 1

# count = 100

# while count > 0:
#     print(count)
#     count -= 1

# Loop Control Statement
# for i in range(5):
#     if i==3:
#         break
#     print(i)

# for i in range(5):
#     if i==3:
#         continue
#     print(i)    

# for i in range(5):
#     if i==3:
#         pass
#     print(i)   


# Randomness and Accumulator pattern
# import random

# roll = random.randint(1, 20)
# print(roll)


# import random

# heads = 0  

# for i in range(10):
#     coin = random.randint(0, 1)
#     print(coin)
#     if coin == 1:
#         heads += 1 

# print("Total heads:", heads)


# bag = 0

# for i in range(100):
#     bag += 100
#     print(bag)

# import random 

# rolls = 0

# for i in range(5):
#     dice = random.randint(1,6)
#     rolls += dice
# print(rolls)

# import random 

# total = 0

# for i in range(3):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     totaldice = dice1+dice2
#     total += totaldice
# print(total)

import random


balance = 50
timebroke = 0
timeswon = 0 

while balance > 0 and balance < 100:
    game = random.randint(0,1)
    if game == 1:
        balance += 1
        timeswon += 1
        print(f"you won {balance}")
    else:
        balance -= 1
        timebroke += 1
        print(f"You failed {balance}")  

print("Game over! Final balance:", balance)
print("You won", timeswon)
print("you went broke", timebroke)      

