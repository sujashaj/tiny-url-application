from flask import Flask
from routes.Routes import Routes  # Import the Blueprint

app = Flask(__name__)
routes = Routes()
app.register_blueprint(routes.bp)  # Register the Blueprint


if __name__ == "__main__":
    app.run(port=8080, debug=True)