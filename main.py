# SNAKE WATER GUN GAME
print('''welcome to snake water gun game''')
print("it's you vs computer")
import random
c=random.choice([0,1,2])
game = {"snake":0, "water": 1, "gun": 2}
reversegame={0:"snake",1:"water",2:"gun"}
y = input("enter your choice:")
y2 = y.lower()
you= game[y2]
if (you==c):
  print("draw")

else:
  print(f"you choose {reversegame[you]} and computer choose {reversegame[c]}")

if(you==0 and c==1):
  print("~you won")

elif(you==1 and c==0):
  print("~you lose")

elif(you==1 and c==2):
  print("~you won")

elif(you==2 and c==1):
  print("~you lose")

elif(you==2 and c==0):
  print("~you won")

elif(you==0 and c==2):
  print("~you lose")


# the end





  

