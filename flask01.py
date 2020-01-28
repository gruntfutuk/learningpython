from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hey there!"

@app.route('/stuart')
def stuart():
    return "Hey there Stuart, welcome!"


if __name__ == '__main__':
    app.run(debug=True)
