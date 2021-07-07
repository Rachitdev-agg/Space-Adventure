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
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

question1 = input("you are in a space shuttle, Go or wait? ")
ques1 = question1.lower()
if ques1 == "go":
  question2 = input("You are in space, Go out or stay in? ")
  ques2 = question2.lower()
  if ques2 == "stay in":
    question3 = input("You found 3 drawers, which of them should you open. Left, Middle or Right? ")
    ques3 = question3.lower()
    if ques3 == "middle":
      print("you found a teleporter and millions of dollars. Now you are be rich and be on earth. Congrats you won")
    elif ques3 == "left":
      print("You found an alien carnivore in there and you become his lunch.")
    else:
      print("You found diamonds!! but you cant go to earth, so you have to die here alone. Doesn't really matter because you were gonna die like that anyway")
  else:
    print("And Now you are a dead freezed body floating in space")
else:
  print("You got caught and went to jail. Real smart move buddy.")