from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud Computing Lab Work 1</h1>
    <h2>Docker Containerization</h2>
    <p>Hello from GitHub Codespaces and Docker!</p>
    <p>The application is running successfully inside a Docker container.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)