from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("angela_testing_website.html")


if __name__ == '__main__':
    app.run(debug=True)
