from flask import Flask, Response
import json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


with open('BoulderTrailHeads.json') as json_file:
    data = json.load(json_file)
    # create trail object
    # for k, v in data.items():
    #     if v['BikeTrail'] == 'Yes':
    #         print(v['BikeTrail'], data[k])
# get bicile is yes and show result
    # Get all available trails


@app.route('/biketrail', methods=['GET'], strict_slashes=False)
def get_bycicle_roads():
    results = {}
    for k, v in data.items():
        if v['BikeTrail'] == 'Yes':
            results[k] = data[k]
    return results


@app.route('/fishing', methods=['GET'], strict_slashes=False)
def get_fishing_roads():
    results = {}
    for k, v in data.items():
        if v['FISHING'] == 'Yes':
            results[k] = data[k]
    return results


if __name__ == "__main__":
    app.run()
