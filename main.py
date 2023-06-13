from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))
