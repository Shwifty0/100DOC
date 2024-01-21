from flask import Flask
from flask import request, render_template
import random

numbers = [i for i in range(11)]
random_number = random.choice(numbers)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/<int:guess>")
def logic(guess):
        print(random_number)
        if guess == random_number:
            return render_template("found.html")
        elif guess < random_number:
            return render_template("higher.html")
        else:
            return render_template("lower.html")


if __name__ == "__main__":
    app.run(debug=True)