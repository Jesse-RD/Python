from flask import Flask

app = Flask(__name__)

app.secret_key = "this is a secret be quiet"