from flask import Flask, render_template, request, jsonify
import json
from CaesarCipher import *
from VigenereCipher import *
app= Flask(__name__)

@app.route('/')
def home():
  app.route('/')
  return render_template("main.html", value = "title")

@app.route('/cipher/<name>')
def cipher(name): 
  data = None
  if name == "caesar":
    data = GetCaesarCipher()
  elif name == "vigenere":
    data = GetVigenere()
  return render_template(name+".html", data=data)

@app.route('/cipher/caesar', methods=['POST'])
def update_caesar():
  data = GetCaesarCipher(int(request.form['shift']), request.form['text'])
  # return to page with new data
  return render_template("caesar.html", data=data)

@app.route('/cipher/vigenere', methods=['POST'])
def update_vigenere():
   data = GetVigenere(request.form['key'], request.form['text'])
   return render_template("vigenere.html", data=data)

if __name__=="__main__":
  app.run(debug=True)