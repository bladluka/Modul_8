from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/mypage/me")
def mypageme():
    return render_template("mypage.me.html")


if __name__ == "__main__":
    app.run()
