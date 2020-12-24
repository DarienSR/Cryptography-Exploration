from graphics import *
from VigenereCipher import *
import SetupCiphers as SP

def DisplayVigenere(screen, nav):
  table = TableSetup() # Vigenere file
  display = []
  cipherDesc = "The Vigenere Cipher contains multiple Caesar Ciphers with different shift values."
  cipherName = "Vigenere Cipher"
  FIRST_HEADING_HEIGHT = 300

  # Undraw Navigation
  SP.UndrawDisplay(nav)

  # Undraw Navigation. 
  SP.UndrawDisplay(nav)

  # Display Press Esc to go Back, Heading, Description
  title = SP.DisplayInfo(screen, display, cipherName, cipherDesc)

  # Display Plain Input
  plainText = SP.CreateInput("Plain Text", 150, 275, 20, screen, display)

  plainText.setText("attackatdawn") # set default value

  # Display Key Word Input
  keyWord = SP.CreateInput("Key Word", 150, 350, 20, screen, display)

  keyWord.setText("lemon") # set default value

  # Display Cipher Text
  cipherText = Encrypt(table, plainText.getText().lower(), keyWord.getText().lower())

  cipherDisplayText = Text(Point(150, 415), "Cipher Text").draw(screen)

  display.append(cipherDisplayText)

  cipherDisplay = Text(Point(150, 435), cipherText).draw(screen)
  display.append(cipherDisplay)

  # Display Table onto screen. will also contain highlighting

  # Main Table
  y = 300
  for idx in range(0, 26):
    row = Text(Point(600, y), "  ".join(table[idx])).draw(screen)
    display.append(row)
    y = y + 20

  # X and Y Axis Alphabets - draw the default alphabet
  xAxis = Text(Point(600, 270), "  ".join(table[0])).draw(screen)
  xAxis.setTextColor("red")
  display.append(xAxis)

  # Draw Vertically (y axis)
  y = 300
  yAxis = [] # used to undraw later
  for idx in range(0, 26):
    letter = Text(Point(380, y), "  ".join(table[0][idx])).draw(screen) # draw vertically
    letter.setTextColor("red")
    yAxis.append(letter)
    y = y + 20

  # Get transformations
  plainTextClone = plainText
  cipherTextClone = cipherDisplay
  keyWordClone = RepeatKeyword(plainTextClone, keyWord)

  # Draw transformations
  plainClone = Text(Point(150, 500), plainTextClone.getText()).draw(screen)
  keyClone = Text(Point(150, 520), keyWordClone).draw(screen)
  cipherClone = Text(Point(150, 540), cipherTextClone.getText()).draw(screen)

  display.append(plainClone)
  display.append(keyClone)
  display.append(cipherClone)

  while screen.getKey() != "Escape":
    # Update Everything accoridng to new input
    plainTextText = plainText.getText().lower()
    plainText.setText(plainTextText)
    
    keyWordText = keyWord.getText().lower()
    keyWord.setText(keyWordText)

    updateCipherText = Encrypt(table, plainTextText, keyWordText)

    cipherDisplay.setText(updateCipherText)

    # Update transformations
    keyWordClone = RepeatKeyword(plainText, keyWord)
    keyClone.setText(keyWordClone)

    plainClone.setText(plainTextText)
    cipherClone.setText(updateCipherText)

  # Undraw Everything
  SP.UndrawDisplay(display)
  SP.UndrawDisplay(yAxis)

def RepeatKeyword(plainTextClone, keyWord):
  keyWordClone = ""
  count = 0
  for x in range(1, len(plainTextClone.getText()) + 1):
    try:
      keyWordClone += keyWord.getText()[count]
    except IndexError:
      count = 0
      keyWordClone += keyWord.getText()[count]

    count = count + 1
  return keyWordClone
