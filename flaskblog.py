from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "714bef120ec961848f50ae5653252767"

posts = [
    {
        "author": "Yui Iida",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 20,2022",
    },
    {
        "author": "Yui Iida",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "April 21,2022",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)
    # return '''<!doctype html>
    # <html>
    # '''
    # can write lile this


@app.route("/about")
def about():
    return render_template("about.html", title="About")
    # return "<h1>About page</h1>"


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
