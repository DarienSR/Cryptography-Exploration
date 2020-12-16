import string
from graphics import *
# Default Functions used across the ciphers for setup as well as their general display
# Divided into cipher logic and cipher display

# FUNCTIONS CIPHER LOGIC
def GetDefaultAlphabet():
  return list(string.ascii_lowercase)


# FUNCTIONS CIPHER DISPLAY

def UndrawNavigation(displayArr):
  for item in displayArr:
    item.undraw()

def DisplayHeading(screen, cipherName, pos, display, font_size = 20):
  heading = Text(Point(pos[0], pos[1]), cipherName).draw(screen)
  heading.setFace("helvetica")
  heading.setSize(font_size)
  heading.setStyle("bold")
  display.append(heading)
  return heading