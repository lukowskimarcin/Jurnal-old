#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'app': 'python mt5 connector'})


app.run(port=5080)
