print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print('Your mission is to find the treasure called "One Piece".\n') 

#Write your code below this line 👇

print("One night, you've killed a pirate guy that have a bounty for him dead or alive")
step_1 = input('type "1" to give him to marine or type "2" to just leave him?\n')

if step_1 == "1":
  print("\nMarine not giving you the money and try to arrest you too.")
  step_2 = input('Type "1" to fight all of them and run away or type "2" to try to negotiate with the boss or type "3" to just run away from them.\n')
  if step_2 == "2":
    print("\nThey will give you the money after sent you to jail for 7 days without foods")
  elif step_2 == "3":
    print('\nYou\'re reputation drop.\nGAME OVER.')
  else:
    print('\nYou still got caught by them.\nGAME OVER.')
else:
  print('\nYou are still become an ordinary pirate hunter and never gonna find "One Piece".\nGAME OVER.')