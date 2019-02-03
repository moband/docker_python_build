from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'HELLO, FLASK!'


@app.route('/json')
def hello_json():
    return jsonify({
        "message": 'hello, flask!'
    }), 200


if __name__== '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)