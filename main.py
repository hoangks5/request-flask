from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login_user():
    if request.method == 'POST':
        username = request.form["un"]
        password = request.form["pass"]
        if username == "admin" and password == "123":
            return render_template('index.html')
        else:
            return "Sai mat khau"
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)