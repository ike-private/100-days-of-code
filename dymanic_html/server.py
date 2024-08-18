from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    now = datetime.now()  # current date and time
    current_year = now.strftime("%Y")
    return render_template("index.html", current_year=current_year)


@app.route("/guess/<name>")
def guess_name(name):
    name = name.capitalize()
    response = requests.get(f"https://api.genderize.io?name={name}")
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender = response.json()["gender"]
    a = age_response.json()["age"]
    return render_template("index.html", name=name, gender=gender, age=a)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/7798826d5fe3bcac90ee"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blogs.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
