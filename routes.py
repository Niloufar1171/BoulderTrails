import json
import csv


from flask import current_app as app
from flask import redirect, request, url_for, jsonify

# Create a dictionary to holds info converted from csv file into json


def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open("Bouldertrails/BoulderTrailHeads.csv", encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['FID']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


svFilePath = 'Bouldertrails/BoulderTrailHeads.csv'
jsonFilePath = 'Bouldertrails/BoulderTrailHeads.json'

make_json(svFilePath, jsonFilePath)


# Get all available trails
# app.route('/trails', methods=['GET'], strict_slashes=False)
