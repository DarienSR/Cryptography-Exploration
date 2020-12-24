import numpy as np
import SetupCiphers as SP
from graphics import *

def shift(ALPHABET, amount):
  return np.roll(ALPHABET, -amount)

def TableSetup():
  table = []
  # Setting up our Vigenere Table with alphabets with differnt shift values.
  for x in range(0,27):
    table.append(shift(SP.GetDefaultAlphabet(), x))
  return table

# Calculate cipherText
def Encrypt(table, plainText, keyWord):
  ALPHABET = SP.GetDefaultAlphabet()
  cipherText = ""
  # Traverse the length of the plainText
  temp = 0
  for idx, letter in enumerate(plainText):
    # Keep on iterating through keyWord, if it reaches the end of the keyWord go to the start of keyWord.
    try:
      indexOfKeyLetter = ALPHABET.index(keyWord[temp])
    except IndexError:
      temp = 0
      indexOfKeyLetter = ALPHABET.index(keyWord[temp])

    # Get index of keyWord letter
    indexOfKeyLetter = ALPHABET.index(keyWord[temp])
    # Get index of keyWord letter
    indexOfPlainTextLetter = ALPHABET.index(letter)
    # Use the search table, looking up the two index values.
    cipherText += table[indexOfKeyLetter][indexOfPlainTextLetter]
    temp = temp + 1
  return cipherText