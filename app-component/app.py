from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import configparser
import re

app = Flask(__name__)
CORS(app)

# read environment file
config = configparser.ConfigParser()
config.read('app.env')

# connect to aiven database
aivendb = mysql.connector.connect(
    host=config.get('DB','HOST'),
    port=config.get('DB','PORT'),
    user=config.get('DB','USER'),
    password=config.get('DB','PASSWORD'),
    database=config.get('DB','DATABASE'))
aivencursor = aivendb.cursor()

@app.route('/api/qr-code', methods=['POST'])
def process_qr_code():
    data = request.get_json()
    qr_data = data.get('qrData')
    print("Received QR Code:", qr_data)
    return jsonify({"message": "QR Code processed successfully", "data": qr_data})

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "hello there",
                    "description": "general kenobi"})

# endpoint to retrieve all item records from db
@app.route('/api/items', methods=['GET'])
def getItems():
    aivencursor.execute("select * from items")
    results = aivencursor.fetchall()
    return results

# helper method for formatting sql column, value pairs
def columnValues (col, val):
  return "{0} = '{1}'".format(col, val)

# endpoint to update a particular item record in db
@app.route('/api/item/<name>', methods=['PUT'])
def updateItem(name):
  name = re.sub(r'[^a-zA-Z0-9]', '', name)

  # retrieve request body
  updatesNeeded = request.json

  # map columns to update with values to update in sql parseable manner
  colValues = map(columnValues, updatesNeeded.keys(), updatesNeeded.values())
  colValuesList = list(colValues)
  updateSetList = ', '.join(colValuesList)

  try :
    sqlquery = "update items set {0} where Name = '{1}'".format(updateSetList, name)
  except Exception as e:
    print("sql update failed : {}".format(e))

  return "finished"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
