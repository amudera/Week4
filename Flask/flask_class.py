from flask import Flask, url_for, redirect, render_template
import random

app = Flask(__name__)


@app.route('/cowsay/<input>',methods=['GET'])

def cowsay(input):
    return str(input + " Moooo!")

@app.route('/cowsay/<int>',methods=['GET'])

def moby(int):
    with open('mobydick.txt', 'r') as f:
        data = f.readlines()
    
    for line in data:
        word = line.split()[int]
        return word


if __name__ == "__main__":
    app.run(debug=True)