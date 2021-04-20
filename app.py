from flask import Flask, render_template, redirect


# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/bitcoin<br/>"
        f"/ethereum<br/>"
        f"/dogecoin")

@app.route("/bitcoin")
def bitcoin():
    return render_template("index.html")


# @app.route("/ethereum")
# def ethereum():
#     return render_template("")

# @app.route("/dogecoin")
# def ethereum():
#     return render_template("")

if __name__ == "__main__":
    app.run(debug=True)



