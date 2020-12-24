import string
from graphics import *
# Default Functions used across the ciphers for setup as well as their general display
# Divided into cipher logic and cipher display

# FUNCTIONS CIPHER LOGIC
def GetDefaultAlphabet():
  return list(string.ascii_lowercase)




# FUNCTIONS CIPHER DISPLAY

def UndrawDisplay(displayArr):
  for item in displayArr:
    item.undraw()

def DisplayHeading(screen, cipherName, pos, display, font_size = 20):
  heading = Text(Point(pos[0], pos[1]), cipherName).draw(screen)
  heading.setFace("helvetica")
  heading.setSize(font_size)
  heading.setStyle("bold")
  display.append(heading)
  return heading

def DisplayInfo(screen, display, cipherName, cipherDesc):
  # Esc to go back
  DisplayHeading(screen, "Press ESC to go back", (110, 100), display, 15)
  
  # Title
  title = DisplayHeading(screen, cipherName, (screen.getWidth() / 2, 150), display, 36)
  
  # Desc
  display.append(Text(Point(screen.getWidth() / 2, 190), cipherDesc).draw(screen))

  return title


def CreateInput(text, x, y, width, screen, display):
  display.append(Text(Point(x, y), text).draw(screen))
  inputText = Entry(Point(x, y + 30), width).draw(screen)
  display.append(inputText)
  return inputText