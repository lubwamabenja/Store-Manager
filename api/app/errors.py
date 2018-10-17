from flask import Flask ,request,json,jsonify


app = Flask(__name__) 

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Invalid request/input'}), 400


@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server Error has occured, Check input'}), 500
