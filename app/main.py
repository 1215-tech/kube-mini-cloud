from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello from Kubernetes with Ansible & GitLab CI/CD!"