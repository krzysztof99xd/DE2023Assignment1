## This is the assignment 1 for Data Engineering course at JADS ##
This is a simple application is for predicting stroke based on the few parameters which user inputs on the web page. Data has been downloaded from Kaggle.

Stroke Prediction Dataset. (2021, 26 january). Kaggle. https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

In the `prediction-api` folder there all necessary files to deploy a simple API which predicts whether someone is likely or not likely to have a stroke.

In the `prediction-ui` folder there are all necessary files to deploy a simple UI which calls the prediction API to see whether someone is likely to have a stroke or not based on the simple input.  

Both `prediction-api` and `prediction-ui` are containerized into Dockerfiles and deployed using Cloud Run.

Inside `ml_pipeline` folder there is a `train_pipeline.ipynb` file which is responsible for downloading the data from GCS bucket, training K-Nearest-Neighbours Algorithm as well as Logistic Regression ML models.
The pipeline chooses more accurate model, checks whether it passes the accuracy threshold and uploads them in the in GCS bucket in models folder.

Inside `builder_tool` folder there are multiple files which are responsible for CI/CD pipelines.
- `cloud_build_ml_app.json` downloads the `stroke_model.h5` from GCS bucket, replaces the local model inside `prediction-api` folder and then builds `prediction-api` and `prediction-ui`.
- `pipeline_executor_tool_cloudbuild.json` allows us to build and execute ML pipelines
- `stroke_predictor_pipeline_execution_cloudbuild.json` is responsible for building and executing `stroke_predictor_pipeline` (`train_pipeline.ipynb`)

Inside `assignment_repo` folder there are files which were used to write a report for that assignment.

Within this project there are multiple triggers for CI/CD pipelines. They are all executed using Google Cloud Build services:
- automatic execution of `cloud_build_ml_app.json` whenever something is pushed to MASTER branch
- manual trigger for executing `pipeline_executor_tool.json`
- manual trigger for executing `stroke_predictor_pipeline_execution_cloudbuild.json`

It is important that you upload your parameters.json file into gcs storage with correct parameters to run your pipeline. Make sure to use correct json format.

Edit to trigger CI/CD pipeline (CI/CD testing)