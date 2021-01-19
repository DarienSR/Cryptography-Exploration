from flask import Flask, render_template, request, jsonify
from CaesarCipher import *
from VigenereCipher import *
app = Flask(__name__)

# HOME
@app.route('/')
def home():
  app.route('/')
  return render_template("main.html", value = "title")

# GET ROUTE 
@app.route('/cipher/<name>')
def cipher(name): 
  data = None
  if name == "caesar":
    data = GetCaesarCipher()
    content = data['view']
  elif name == "vigenere":
    data = GetVigenere()
    content = data['view']
  return render_template("cipher.html", data=data, content=content)

# UPDATE ROUTE
@app.route('/cipher/<name>', methods=['POST'])
def update_cipher(name):
  data = None
  if name == "caesar":
    data = GetCaesarCipher(int(request.form['shift']), request.form['text'])
  else:
    data = GetVigenere(request.form['key'], request.form['text'])

  content = data['view']
  return render_template("cipher.html", data=data, content=content)

if __name__=="__main__":
  app.run(debug=True)