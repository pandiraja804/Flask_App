from flask import Flask, render_template
import os

template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

app = Flask(__name__, template_folder=template_path)

print("Template folder:", template_path)
print("Template exists:", os.path.exists(os.path.join(template_path, "index.html")))

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)