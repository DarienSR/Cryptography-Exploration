import numpy as np
import string

def shift(ALPHABET, amount):
  return np.roll(ALPHABET, -amount).tolist()

def TableSetup():
  table = []
  # Setting up our Vigenere Table with alphabets with differnt shift values.
  for x in range(0,27):
    table.append(shift(list(string.ascii_lowercase), x))
  return table

# Calculate cipherText
def Encrypt(table, plainText, keyWord):
  ALPHABET = list(string.ascii_lowercase)
  cipherText = ""

  print("======================")
  print(keyWord)
  print("======================")

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

def RepeatKeyword(plainTextClone, keyWord):
  keyWordClone = ""
  count = 0
  for x in range(1, len(plainTextClone) + 1):
    try:
      keyWordClone += keyWord[count]
    except IndexError:
      count = 0
      keyWordClone += keyWord[count]

    count = count + 1
  return keyWordClone


def GetVigenere(key = "lemon", plain = "attackatdawn"): 
  table = TableSetup()
  cipherText = Encrypt(table, plain, key)
  keyWordRepeated = RepeatKeyword(plain, key)

  return {
    "name": "Vigenere Cipher",
    "plain_text": plain,
    "keyword": key,
    "keyword_repeated": keyWordRepeated,
    "cipher_text": cipherText,
    "table": table,
  }
