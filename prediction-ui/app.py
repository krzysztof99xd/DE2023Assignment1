# importing Flask and other modules
import json
import os
import logging
import requests
from flask import Flask, request, render_template, jsonify

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkstroke', methods=["GET", "POST"])
def check_stroke():
    if request.method == "GET":
        return render_template("input_form.html")

    elif request.method == "POST":

        age = request.form.get("age")
        hypertension = True if request.form.get("hypertension") == 'on' else False
        heart_disease = True if request.form.get("heartDisease") == 'on' else False
        avg_glucose_level = request.form.get("avg_glucose")
        bmi = request.form.get("bmi")
        gender_1 = True if request.form.get("gender") == 'male' else False
        ever_married_1 = True if request.form.get("married") == 'on' else False
        work_type_Never_worked = True if request.form.get("work_type") == 'Never_worked' else False
        work_type_Private = True if request.form.get("work_type") == 'Private' else False
        work_type_Self_employed = True if request.form.get("work_type") == 'Self-employment' else False
        work_type_children = True if request.form.get("work_type") == 'children' else False
        Residence_type_1 = True if request.form.get("Residence_type") == 'Urban' else False
        smoking_status_never_smoked = True if request.form.get("smokes") != 'on' else False
        smoking_status_smokes = True if request.form.get("smokes") == 'on' else False

        prediction_input = [[age, hypertension, heart_disease, avg_glucose_level,
                             bmi, gender_1, ever_married_1, work_type_Never_worked,
                             work_type_Private, work_type_Self_employed, work_type_children,
                             Residence_type_1, smoking_status_never_smoked, smoking_status_smokes]]

        scaler = joblib.load('scaler.pkl')
        pred_scaled = scaler.transform(new_obs) #prediction input scaled

        ###Example of how pred_scaled should be used for the best model, in this case RF###
        #y_pred_rf = best_rf_classifier.predict(pred_scaled)


        logging.debug("Prediction input : %s", prediction_input)
        print(prediction_input)
        # use requests library to execute the prediction service API by sending an HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        # json.dumps() function will convert a subset of Python objects into a json string.
        # json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
        predictor_api_url = os.environ['PREDICTOR_API']
        res = requests.post(predictor_api_url, json=json.loads(json.dumps(prediction_input)))

        prediction_value = res.json()['result']
        logging.info("Prediction Output : %s", prediction_value)
        return render_template("response_page.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkstroke' path


@app.route('/another_page')
def another_page():
    return render_template('another_page.html')


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
