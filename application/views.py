from flask import app

@app.get('/')
def home():
    return "Hello world"