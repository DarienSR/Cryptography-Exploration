from graphics import *
from DisplayCaesarCipher import DisplayCaesar
from Navigation import *
from DisplayVigenere import *
# DEFAULT APPLICATION SETUP
appName = "Exploring Cryptography"
screenHeight = 900
screenWidth = 1200

def main():
  nav = None
  screen = GraphWin(appName, screenWidth, screenHeight) # screen setup
  # program loop and navigation condition
  keyString = ""

  # Navigation Initial Display
  while keyString != "Escape":
    if keyString == "1":
      DisplayCaesar(screen, nav)
      nav = Navigation(screen) # Redisplay nav
    elif keyString == "2":
      DisplayVigenere(screen, nav)
      nav = Navigation(screen) # Redisplay nav
    else:
      nav = Navigation(screen)

    # Pause until input
    keyString = screen.getKey() 
    
  screen.close()  

main()