#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
from flask import request
from service import MetaTraderService
from utils import NpEncoder
import py_eureka_client.eureka_client as eureka_client

rest_port = 5080
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="mt5-service",
                   instance_port=rest_port)



app = Flask(__name__)
service = MetaTraderService()

@app.route('/')
def index():
    return json.dumps({'app': 'python mt5 connector'})


@app.route('/api/mt5/v1/copy_rates_from_pos', methods=['GET'])
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



app.run(host="0.0.0.0", port=rest_port, debug=True)
