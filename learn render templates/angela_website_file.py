from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("angela_website_2.html")


if __name__ == '__main__':
    app.run(debug=True)
