from flask import Flask, render_template, request, url_for, redirect, session, jsonify, Response, g
from app import app

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return "This is a GET"
    key = request.json['key']
    if (key == 'DockerTest'):
        return "Hello World! This docker is working!"
    else:
        return "This isn't right!"