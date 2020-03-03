from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = "2f8f7f90b4f98aba5ea51dbc94e5bb3715126ccde69e745379b8f48b9de0decc"
africastalking.initialize(username, api_key)
