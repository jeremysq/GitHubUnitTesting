from GithubUnitTesting.app import app
import requests

app.run(debug=True,host="0.0.0.0")

def test_example():
    x = requests.get('http://localhost:5000/shutdown')
    assert x == "Server shutting down..."