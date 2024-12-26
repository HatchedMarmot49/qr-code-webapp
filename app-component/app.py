from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
