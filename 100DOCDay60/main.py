from flask import Flask, render_template, request
app = Flask("__name__")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def forms():
    if request.method == 'POST':    
        email = request.form.get("email")
        password = request.form.get("password")
        print(email, password)
        return f"<h1> {email}, {password} </h1>"
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)