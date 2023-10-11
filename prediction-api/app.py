import os

from flask import Flask, request

from stroke_predictor import StrokePredictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/stroke_predictor/', methods=['POST']) # path of the endpoint. Except only HTTP POST request
def predict_str():
    # the prediction input data in the message body as a JSON payload
    prediction_input = request.get_json()
    return sp.predict_single_record(prediction_input)


sp = StrokePredictor()
# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)

