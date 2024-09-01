from flask import Flask
# from flask_cors import CORS, cross_origin
import json
import csv
from flask import redirect, request, url_for, jsonify

import config


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.Config)

    with app.app_context():
        import routes
        import model

 #   cors = CORS()
 #   cors.init_app(app)
    return app


with open('BoulderTrailHeads.json') as json_file:
    data = json.load(json_file)

    # for reading nested data [0] represents
    # the index value of the list
    print(data['1']['FID'])
    # create an object of trail and populate based on the it's json
    # create a list of key value pairs(map)

    # create trail object
    # for k, v in data.items():
    #     print(k, v)
# get bicile is yes and show result
    # Get all available trails


if __name__ == '__main__':
    app = create_app
    app.run(debug=True)
