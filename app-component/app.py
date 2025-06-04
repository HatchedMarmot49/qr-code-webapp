from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import configparser

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
