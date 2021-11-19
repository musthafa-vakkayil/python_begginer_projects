rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 
import random

choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if choice == 0:
  print(f"Your choice is \n{rock}")
elif choice ==1:
  print(f"\nYour choice is \n{paper}")
elif choice==2:
  print(f"\nYour choice is \n{scissors}")


com_choice = random.randint(0,2)

if com_choice == 0:
  print(f"\ncomputer choice is \n{rock}")
elif com_choice ==1:
  print(f"\ncomputer choice is \n{paper}")
elif com_choice==2:
  print(f"\ncomputer choice is \n{scissors}")


if choice==0 and com_choice==0:
  print("\ndraw")
elif choice==1 and com_choice==1:
  print("\ndraw")
elif choice==2 and com_choice==2:
  print("\ndraw")
else:
  if choice == 2 and com_choice==1:
    print("\nYou Win")
  elif choice ==1 and com_choice ==2:
    print("\nComputer Win")
  elif choice ==1 and com_choice ==0:
    print("\nYou Win")
  elif choice ==0 and com_choice ==1:
    print("\nComputer Win")
  elif choice ==0 and com_choice ==2:
    print("\nYou Win")
  elif choice ==2 and com_choice ==0:
    print("\nComputer Win")