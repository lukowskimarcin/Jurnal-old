#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
from flask import request
from service import MetaTraderService
from utils import NpEncoder

app = Flask(__name__)
service = MetaTraderService()

@app.route('/')
def index():
    return json.dumps({'app': 'python mt5 connector'})


@app.route('/api/copy_rates_from_pos', methods=['GET'])
def copy_rates_from_pos():
    symbol = request.args.get('symbol')
    timeframe = request.args.get('timeframe')
    count = int(request.args.get('count'))

    print(f"args: symbol-{symbol} timeframe-{timeframe} count-{count}")

    if count:
        result = service.copy_rates_from_pos(symbol, timeframe, count)
    else:
        result =  service.copy_rates_from_pos(symbol, timeframe)

    return json.dumps(result, cls=NpEncoder)



app.run(host="0.0.0.0", port=5080, debug=True)
