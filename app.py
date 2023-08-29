import numpy as np
# import os.path
from flask import Flask, render_template, request
import joblib


app = Flask(__name__)


# Load the already trained ML model
model = joblib.load("loan_model.pkl")

# Index page
@app.route("/")
def home():
    return render_template("index.html")

# Contact us page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Validation page
@app.route("/validation")
def loan_val():
    # Changed loan val to loan_val.html
    return render_template("loan_val.html")

# Prediciton button
@app.route("/predict", methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    valid = ["No", "Yes"]
    # print(f"Eligible for loan??: {valid[output]}")
    return render_template("loan_val.html", prediction_text="Eligible to receieve a loan: {}".format(valid[output]))





if __name__ == "__main__":
    app.run(debug=True)