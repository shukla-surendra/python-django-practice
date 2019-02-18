from flask import Flask
app = Flask(__name__)


# @app.route('/')
# def hello():
#     return "Hello World!"
@app.route('/')
@app.route('/<name>/<age>')
def hello_name(name=None, age=None):
    return "Hello {}, {} !".format(name, age)

if __name__ == '__main__':
    app.run()