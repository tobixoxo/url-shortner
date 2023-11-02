from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def app():
    return '<h1>Hello, World!</h1>'
