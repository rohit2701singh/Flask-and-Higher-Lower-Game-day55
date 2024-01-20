from flask import Flask
import random


random_num = random.randint(0, 9)
print(f"guessed number is: {random_num}")

app = Flask(__name__)


def home_page_modify(function):
    def wrapper():
        return (f"<h1 style= 'color: purple'> {function()} </h1>"
                f"<br><br><img src='https://media.giphy.com/media/abHQ4aDqRqlyBTdAP0/giphy.gif' width=700 height=400 />")
    return wrapper


@app.route("/")
@home_page_modify
def home_page():
    return "Guess a number between 0 and 9"


@app.route("/<int:user_input>")
def user_guess(user_input):
    if user_input > random_num:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/l2JHZBaadRwruGn3W/giphy.gif'/>"

    elif user_input < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/DVSpPORBAgDwiXCjzf/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/gIxBtRsuxT0iWuBDY4/giphy.gif'/>"


if __name__ == '__main__':
    app.run(debug=True)
