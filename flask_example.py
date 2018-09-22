from flask import Flask, request

app = Flask(__name__)


def fiz():
    print(request)


def buzz():
    print(request)


@app.route("/")
def hello():
    fiz()
    buzz()

    return "Hello World!"


if __name__ == '__main__':
    app.run()
