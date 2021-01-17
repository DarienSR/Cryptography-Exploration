"""
Encrypt (Function) - takes in default ALPHABET, shift, and plainText. Generates shifted alphabet and returns it.
GetCaesarCipher (Function) - default shift value and text value. Calls Encrypt function and setups object
                            containing information for cipher.
"""

import string
import numpy as np

def Encrypt(ALPHABET, shiftBy, plainText):
  cipherText = "" # predefine text so we can append to it.
  shifted_alphabet = np.roll(ALPHABET, -shiftBy) # take the default alphabet and shift it to the left by shiftBy value
  
  for letter in plainText:
    if letter != " ":
      cipherText += shifted_alphabet[ALPHABET.index(letter)]
    else:
      cipherText += " "
  return cipherText, " ".join(shifted_alphabet)

def GetCaesarCipher(shiftBy = 1, text = "attackatdawn"):
  ALPHABET = list(string.ascii_lowercase)
  shift = shiftBy
  plain = text
  cipherText, shiftedAlphabet = Encrypt(ALPHABET, shift, plain)

  return {
    "name": "Caesar Cipher",
    "default_alphabet": " ".join(ALPHABET),
    "plain_text": plain,
    "shiftBy": shift,
    "shifted_alphabet": shiftedAlphabet,
    "cipher_text": cipherText
  }