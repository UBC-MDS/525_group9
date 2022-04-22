from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from sklearn.ensemble import RandomForestRegressor
## Import any other packages that are needed

app = Flask(__name__)

# 1. Load your model here
model = load("notebooks/backup_notebooks/model.joblib")

# 2. Define a prediction function
def return_prediction(content):
    data = np.array(content["data"]).reshape(1, -1)  # this extracts the Inpute attribute from the JSON content
    data = data.reshape(1, -1)
    return model.predict(data)

# 3. Set up home page using basic html
@app.route("/")
def index():
    # feel free to customize this if you like
    return """
    <h1>Welcome to our rain prediction service</h1>
    To use this service, make a JSON post request to the /predict url with 25 climate model outputs.
    """

# 4. define a new route which will accept POST requests and return model predictions
@app.route('/predict', methods=['POST'])
def rainfall_prediction():
    content = request.json  # this extracts the JSON content we sent
    prediction = return_prediction(content)[0]
    results = {
        "Input": content["data"],
        "Prediction": prediction
    }  # return whatever data you wish, it can be just the prediction
                     # or it can be the prediction plus the input data, it's up to you
    return jsonify(results)