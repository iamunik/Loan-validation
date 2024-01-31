# Importing necessary libraries for the project
import joblib
import zipfile
import condition
import numpy as np
import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)
model = joblib.load("loan_model_class.pkl")


# Index page
@app.route("/")
def home():
    return render_template("index.html")


# Contact us page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Rules page
@app.route("/rules")
def rules():
    return render_template("rules.html")


# User Validation page
@app.route("/validation")
def loan_val():
    return render_template("loan_val.html")


# Admin validation page
@app.route("/admin")
def dummy():
    return render_template("dummy.html")


# Selection dummy admin or user
@app.route("/validate")
def selection():
    return render_template("selection.html")


# Prediction button
@app.route("/predict", methods=["POST"])
def predict():
    try:
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = prediction[0]

        valid = ["No", "Yes"]
    except ValueError:
        return render_template("loan_val.html", error_3="Please fill the form correctly")

    if valid[output] == "No":
        return render_template("loan_val.html", prediction_text=f"Loan Eligibility: {valid[output]}\n"
                                                                f"Sorry you are not eligible to get a loan")
    else:
        return render_template("loan_val.html", prediction_text=f"Loan Eligibility: {valid[output]}\n"
                                                                f"Please go to the nearest branch to finalise the loan")


@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file is provided in the request
    if 'file' not in request.files:
        return render_template("dummy.html", error_="No file provided")

    file = request.files['file']

    # Check if the file has a valid filename
    if file.filename == '':
        return render_template("dummy.html", error_="Please upload a file.")

    # Check columns
    cols = ['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome',
            'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']

    file_type = condition.detect_file_type(file)

    try:
        if file_type == ".csv":
            df = pd.read_csv(file)
            col = list(df.columns)
        elif file_type == ".xlsx" or ".xls":
            df = pd.read_excel(file, engine='openpyxl')
            col = list(df.columns)
    except UnicodeDecodeError:
        return render_template("dummy.html", error_="Cannot upload file please check the guidelines page")
    except zipfile.BadZipfile:
        return render_template("dummy.html", error_="Acceptable files are .xls and .csv files, "
                                                    "please check the guidelines page")

    # Check if the columns on the file uploaded matches what we want.
    for i in range(len(cols)):
        if not cols[i] in col:
            return render_template("dummy.html", error_="Follow the procedure explained on the guideline page")

    # Assuming you're working with a CSV file
    if file:
        # Preprocessing was performed in the condition.py file; called the cleaner() function
        test_id = df['Loan_ID']
        cleaned_data = condition.cleaner(df)

        # Make predictions using your model
        predictions = model.predict(cleaned_data)
        prediction = list(predictions)

        # Mapping the prediction to make it presentable; called the p_mapping() function in condition.py
        mapas = condition.p_mapping(test_id, prediction)

        # Returning the predictions to display them as needed
        return render_template("dummy.html", tabs=mapas.to_html())  # Display predictions as an HTML table


if __name__ == "__main__":
    app.run(debug=True)
