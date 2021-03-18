from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/mypage/contact", methods=['GET', 'POST'])
def mypagemecontact():
    if request.method == 'GET':
        return render_template("mypage.contact.html")
    elif request.method == 'POST':
        print('We received POST')
        print(request.form)
        return redirect("/mypage/me")


if __name__ == "__main__":
    app.run()