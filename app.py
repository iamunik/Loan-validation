import numpy as np
from flask import Flask, render_template, request
import joblib
import pandas as pd  # Assuming you're working with CSV data
import condition


app = Flask(__name__)
app.static_folder = 'static'

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


# User Validation page
@app.route("/validation")
def loan_val():
    # Changed loan val to loan_val.html
    return render_template("loan_val.html")


# Admin validation page
@app.route("/admin")
def dummy():
    return render_template("dummy.html")


# Selection dummy admin or user
@app.route("/validate")
def selection():
    return render_template("selection.html")


# Prediciton button
@app.route("/predict", methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    valid = ["No", "Yes"]
    # print(f"Eligible for loan??: {valid[output]}")
    return render_template("loan_val.html", prediction_text=f"Eligible to receive a loan: {valid[output]}\nPlease go to the nearest branch to finalise the loan")



@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file is provided in the request
    if 'file' not in request.files:
        return render_template("dummy.html", error_1="No file provided")

    file = request.files['file']

    # Check if the file has a valid filename
    if file.filename == '':
        return render_template("dummy.html", error_2="No selected file")

    # Check columns
    cols = ['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome',
            'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']

    df = pd.read_csv(file)
    col = list(df.columns)

    # Check if the columns on the file uploaded matches what we want.
    for i in range(len(cols)):
        if not cols[i] in col:
            return render_template("dummy.html", error_3="Follow the procedure explained on the site")

    # Assuming you're working with a CSV file
    if file:
        # Preprocessing was performed in the condition.py file called the clean() function
        test_ID = df['Loan_ID']
        abc = condition.cleaner(df)

        # Make predictions using your model
        predictions = model.predict(abc)
        predction = list(predictions)

        # Mapping the prediction to make it presentable
        mapas = condition.p_mapping(test_ID, predction)

        # Returning the predictions to display them as needed
        return render_template("dummy.html", tabs=mapas.to_html())  # Display predictions as an HTML table


if __name__ == "__main__":
    app.run(debug=True)

