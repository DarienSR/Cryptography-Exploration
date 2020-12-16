import string
import numpy as np
from graphics import *

def CaesarCipher():
  # ENCRYPTION SETUP
  ALPHABET = list(string.ascii_lowercase) # TO DO: MOVE TO A GENERAL FILE
  return ALPHABET

def Encrypt(ALPHABET, shiftBy, plainText):
  cipherText = ""
  shifted_alphabet = np.roll(ALPHABET, -shiftBy)
  for letter in plainText:
    if letter != " ":
      cipherText += shifted_alphabet[ALPHABET.index(letter)]
    else:
      cipherText += " "
  return cipherText, " ".join(shifted_alphabet)

