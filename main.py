import os

from flask import Flask

http = Flask(__name__)


@http.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    http.run(debug=False, port=port, host='0.0.0.0')
