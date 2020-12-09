from graphics import *
from CaesarCipher import *

appName = "Exploring Cryptography"
screenHeight = 600
screenWidth = 600

def main():
  screen = GraphWin(appName, screenHeight, screenWidth) # screen setup
  
  # Program Runs
  CaesarCipher(screen)

  # Program Ends

  # Pause to view result, otherwise the window will disappear
  screen.getMouse() 
  screen.close()

main()