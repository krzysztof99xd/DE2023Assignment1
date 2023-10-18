import json
import os

import pandas as pd
from flask import jsonify
from keras.models import load_model
import logging
from io import StringIO
# from google.cloud import storage


class StrokePredictor:
    def __init__(self):
        self.model = None

    # def download_model_from_gcs(self, bucket_name, source_blob_name, destination_file_name):
    #     """Downloads a model file from a Google Cloud Storage bucket."""
    #     if not os.path.exists(destination_file_name):
    #         storage_client = storage.Client(project=project_id)
    #         bucket = storage_client.bucket(bucket_name)
    #         blob = bucket.blob(source_blob_name)
    #         blob.download_to_filename(destination_file_name)
    #         print(f"Model downloaded from GCS to {destination_file_name}")

    def predict_single_record(self, prediction_input):
        logging.debug(prediction_input)
        if self.model is None:
            try:
                model_repo = os.environ['MODEL_REPO']
                file_path = os.path.join(model_repo, "model_stroke.h5")
                self.model = load_model(file_path)
            except KeyError:
                print("MODEL_REPO is undefined")
                self.model = load_model('model_stroke.h5')

        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        y_pred = self.model.predict(df)
        logging.info(y_pred[0])
        status = (y_pred[0] > 0.5)
        logging.info(type(status[0]))
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status[0])}), 200
