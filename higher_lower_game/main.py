# importing modules
import art
from game_data import data
import random

print(art.logo)


# setting score
answer = True
score =0

# looping until user makes a wrong answer
while answer:
    # taking two random numbers and corresponding item from the list
    number1 = random.randint(0,len(data)-1)      
    choice1 = data[number1]
    number2 = random.randint(0,len(data)-1)      
    choice2 = data[number2]

    # displaying the first choice
    print(f"Compare A {choice1['name']}, a {choice1['description']}, from {choice1['country']}")

    #displaying the seconnd choice
    print(f"Against B {choice2['name']}, a {choice2['description']}, from {choice2['country']}")

    # receiving user guess
    choice = input("Who Has more follower ? type 'A' or 'B': ")

    # comparing user guess and the higest value in those choices
    if int(choice1['follower_count']) > int(choice2['follower_count']):
        if choice == 'A':
            print("That is Correct")
            score +=1
        else:
            print("That is Wrong")
            answer = False
    elif int(choice1['follower_count']) < int(choice2['follower_count']):
        if choice == 'A':
            print("That is Wrong")
            answer = False
        else:
            print("That is Correct")
            score +=1
                    

print(f"Your Score is {score}")






