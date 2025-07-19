
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def hoem():
    return "Jay Shree Ram"

if __name__ == '__main__':
    app.run(debug=True)