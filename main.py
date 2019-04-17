import os
from flask import Flask

def create_instance(config=None):
    app = Flask(__name__)

    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
    @app.route("/")
    def hello_world():
        return "Greetings Sauce Labs! Greetings from Raj!"

    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_instance()
    app.run(host="0.0.0.0", port=port)