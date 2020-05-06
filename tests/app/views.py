from flask import Flask, render_template, request, url_for, redirect, session, jsonify, Response, g
from app import app

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return "This is a GET"
    key = request.json['key']
    if (key == 'DockerTest'):
        return "Hello World! This docker is working!"
    else:
        return "This isn't right!"

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'