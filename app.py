from flask import Flask, request
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return "Hello, World!"
    key = request.json['key']
    if (key == 'DockerTest'):
        return "Hello, World! This docker is working!"
    else:
        return "This isn't right!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()