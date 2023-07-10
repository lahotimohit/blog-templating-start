from flask import Flask, render_template
import requests
data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
blog = data.json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog=blog)


@app.route("/post/<int:index>")
def post_showing(index):
    display_post = None
    for post in blog:
        if post['id'] == index:
            display_post = post
    return render_template("post.html", post=display_post)


if __name__ == "__main__":
    app.run(debug=True)
