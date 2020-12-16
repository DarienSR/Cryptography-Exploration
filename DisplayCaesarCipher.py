from graphics import *
from CaesarCipher import *
import SetupCiphers as SP

def DisplayCaesar(screen, nav):
  # Undraw Navigation
  for x in nav:
    x.undraw()

  ALPHABET = CaesarCipher()


  # DISPLAY SETUP
  display = [] # We will push everything drawn onto screen in here.
  SP.DisplayHeading(screen, "Press ESC to go back", (110, 100), display, 15)
  cipherDesc = "One of the simplest and most popular ciphers. This substitution cipher works by replacing letters in the plaintext by a letter in a fixed position down the alphabet."
  cipherName = "Caesar Cipher"
  FIRST_HEADING_HEIGHT = 300

  # Title Setup
  title = SP.DisplayHeading(screen, cipherName, (screen.getWidth() / 2, 150), display, 36)

  # Cipher Desc
  display.append(Text(Point(screen.getWidth() / 2, 190), cipherDesc).draw(screen))

  # HOW IT WORKS SECTION
  heading = SP.DisplayHeading(screen, "How It Works", (110, FIRST_HEADING_HEIGHT), display)
  shiftByInput, shiftBy, displayShiftText = DisplayShiftInput(screen, FIRST_HEADING_HEIGHT, display) # Get and Display Shift Value
  plainTextInput, plainText, inputText = DisplayPlainText(screen, FIRST_HEADING_HEIGHT, display) # Get and Display PLain Text
  cipherText, shifted_alphabet = Encrypt(ALPHABET, shiftBy, plainText)  # Implementation of Caesar Cipher 

  # Draw Normal alphabet to screen - don't need to save as var, never redrawing
  display.append(Text(Point(150, FIRST_HEADING_HEIGHT + 50), ALPHABET).draw(screen))

  # Draw shifted alphabet to screen
  newAlphabet = Text(Point(150, FIRST_HEADING_HEIGHT + 70), shifted_alphabet).draw(screen)
  display.append(newAlphabet)

  # Add Text to input box
  cipher = Text(Point(100, FIRST_HEADING_HEIGHT + 120), "Cipher Text: " + cipherText).draw(screen)
  display.append(cipher)

  while screen.getKey() != "Escape":
    if(shiftBy == ""):
      shiftBy = 1
    else:
      try:
        shiftBy = int(shiftByInput.getText())
      except ValueError:
        shiftBy = 0

    # Update values based on user input
    plainText = plainTextInput.getText().lower()
    plainTextInput.setText(plainText)

    cipherText, shifted_alphabet = Encrypt(ALPHABET, shiftBy, plainText)
    newAlphabet.setText(shifted_alphabet)
    cipher.setText("Cipher Text: " + cipherText)
    
  # undraw everything
  SP.UndrawNavigation(display)

def DisplayShiftInput(screen, FIRST_HEADING_HEIGHT, display):
  shiftByInput = Entry(Point(150, FIRST_HEADING_HEIGHT + 30), 10).draw(screen)
  shiftBy = 1 # default shift
  shiftByInput.setText(shiftBy)
  displayShiftText = Text(Point(70, FIRST_HEADING_HEIGHT + 30), "Shift By").draw(screen)
  display.append(shiftByInput)
  display.append(displayShiftText)
  return shiftByInput, shiftBy, displayShiftText

def DisplayPlainText(screen, FIRST_HEADING_HEIGHT, display):
  plainTextInput = Entry(Point(200, FIRST_HEADING_HEIGHT + 100), 20).draw(screen)
  plainTextInput.setText("attack at dawn") # default example
  inputText = Text(Point(50, FIRST_HEADING_HEIGHT + 100), "Plain Text: ").draw(screen)
  plainText = plainTextInput.getText().lower()
  display.append(plainTextInput)
  display.append(inputText)
  return plainTextInput, plainText, inputText


