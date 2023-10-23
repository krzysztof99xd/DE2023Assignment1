## This is the assignment 1 for Data Engineering course at JADS ##
This is a simple application is for predicting stroke based on the few parameters which user inputs on the web page.

In the `prediction-api` folder there all necessary files to deploy a simple API which predicts whether someone is likely or not likely to have a stroke.

In the `prediction-ui` folder there are all necessary files to deploy a simple UI which calls the prediction API to see whether someone is likely to have a stroke or not based on the simple input.  

Both `prediction-api` and `predictio-ui` are containerized into Dockerfiles and deployed using Cloud Run.

Inside `ml_pipeline` there is a `train_pipeline.ipynb` file which is responsible for downloading the data from GCS bucket, trains (tbc by @Kyriakos) ML models and uploads them in the in GCS bucket as well in models folder.

Inside `builder_tool` there are multiple files which are responsible for CI/CD pipelines.
- `cloud_build_ml_app.json` downloads the `stroke_model.h5` from GCS bucket, replaces the local model inside `prediction-api` folder and then build `prediction-api` and `prediction-ui`.
- `pipeline_executor_tool_cloudbuild.json` allows us to build and execute ML pipelines
- `stroke_predictor_pipeline_execution_cloudbuild.json` is responsible for building and executing `stroke_predictor_pipeline` (`train_pipeline.ipynb`)

Within this project there are multiple triggers for CI/CD pipelines. They are all done using Google Cloud Build services
- automatic execution of `cloud_build_ml_app.json` whenever something is pushed to MASTER branch
- manual trigger for executing `pipeline_executor_tool.json`
- manual trigger for executing `stroke_predictor_pipeline_execution_cloudbuild.json`


Edit to trigger CI/CD pipeline (CI/CD testing)