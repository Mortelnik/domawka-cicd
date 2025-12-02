from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status_check', methods=['GET'])
def get_status():
    data = {
        "status": "OK",
        "service": "Мой или мое API",
        "version": "1.0.0"
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)

# домашка сделана или нет?