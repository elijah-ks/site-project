from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary user storage
users = []

@app.route("/")
def index():
    return render_template("introductory_page.html")

@app.route("/signup", methods=["POST"])
def signup():
    # Get form data
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    # Store user (replace with database logic later)
    users.append({"username": username, "email": email, "password": password})

    # Redirect back to home page
    return redirect(url_for("index"))

@app.route("/login", methods=["POST"])
def login():
    # Get form data
    username = request.form["username"]
    password = request.form["password"]

    # Verify user credentials
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)
    if user:
        return f"Welcome back, {username}!"
    else:
        return "Invalid credentials. Please try again."

if __name__ == "__main__":
    app.run(debug=True)

