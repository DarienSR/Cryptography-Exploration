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

def View(plain, shift, cipher, default_alphabet, shifted_alphabet):
  return f"""
  <div class="inline">
    <div id="left">
      <form action="./caesar" method="POST">
        <div>
          <p class="bold">Plain Text: </p>
          <input value="{ plain }" name="text" />
          
          <p class="bold">Shift By: </p>
          <input type="number" value="{ shift }" min=0 value=0 name="shift" />
        </div>
        
        <div id="button-container">
          <button type='submit'>Update</button>
        </div>
      </form>
    </div>

    <div id="right">
      <div>

          <p><span class="bold">Default Alphabet:</span> { default_alphabet }</p>

          <p><span class="bold">Shifted Alphabet:</span> { shifted_alphabet }</p>
    
        <div>
          <p><span class="bold">Plain Text:</span> { plain }</p>
          <p><span class="bold">Cipher Text:</span> { cipher }</p>
        </div>
      </div>
    </div>
  </div>
  """

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
    "cipher_text": cipherText,
    "view": View(plain, shift, cipherText, " ".join(ALPHABET), shiftedAlphabet)
  }

