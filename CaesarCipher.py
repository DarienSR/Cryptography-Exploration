import string
import numpy as np
from graphics import *

plainText = "attack at dawn".lower().replace(" ", "")
#input("Enter plain text: ").lower().replace(" ", "")
shiftBy = 5
#int(input("Enter shift: "))
ALPHABET = list(string.ascii_lowercase)
shifted_alphabet = np.roll(ALPHABET, -shiftBy)

cipherText = ""
for letter in plainText:
  cipherText += shifted_alphabet[ALPHABET.index(letter)]


def CaesarCipher(screen):
  # Point - x, y

  # Heading
  cipherName = "Caesar Cipher"
  heading = Text(Point(150, 40), cipherName + " shifted by: " + str(shiftBy))
  heading.draw(screen)

  # Actual Implementation

  alphabet = Text(Point(150, 100), ALPHABET) 
  alphabet.draw(screen)

  newAlphabet = Text(Point(150, 120), " ".join(shifted_alphabet))
  newAlphabet.draw(screen)

  plain = Text(Point(100, 140), "Plain Text: " + plainText)
  plain.draw(screen)

  cipher = Text(Point(100, 160), "Cipher Text: " + cipherText)
  cipher.draw(screen)


