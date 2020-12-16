# Allows Navigation between the different algorithms
from graphics import *

# https://stackoverflow.com/questions/39867464/adding-button-to-python-graphics-py-window

def Navigation(screen):
  PAGES = ['Caesar Cipher', 'Vigenère Cipher'] # Number of Algorithms to view

  x = 100
  y = 25

  buttons = []

  for i, page in enumerate(PAGES):
    # Create Button
    button = Text(Point(x, y * 2 ), "Press " + str(i + 1) + ": " + page).draw(screen)
    button.setTextColor("black")
    
    buttons.append(button)
    # Update x for next button display
    x = x + 175
  return buttons
