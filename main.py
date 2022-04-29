import os

from flask import Flask

http = Flask(__name__)


@http.route("/")
def hello():
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <h1>It is a great day</h1>
        </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    http.run(debug=False, port=port, host='0.0.0.0')
