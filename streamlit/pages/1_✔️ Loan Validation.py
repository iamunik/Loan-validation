from condition import education_, relation, gende_r, pro_perty, employ_ment
import streamlit as st
import numpy as np
import os
import joblib


st.set_page_config(
    page_title="Admin file upload",
    page_icon="✔️",
)

st.title("Loan Validation")
st.text("Please fill the form to see if you're eligible for a loan.")

parent_dir = os.path.dirname(os.path.dirname(__file__))
path = model_path = os.path.join(parent_dir, "loan_model_class.pkl")

model = joblib.load(path)

try:
    with st.form("My Form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            dependents = st.number_input("Number of dependents")

        with col2:
            applicant = st.number_input("Applicant yearly income in $")

        with col1:
            co_applicant = st.number_input("Co-applicant income")

        with col2:
            credit_history = st.number_input("Applicant credit history")

        with col1:
            loan_duration = st.number_input("Loan duration in days")

        with col2:
            loan_amount = st.number_input("Loan amount in $")

        with col1:
            property_area = st.radio("Property Area", [0, 1, 2], index=None, format_func=pro_perty)

        with col2:
            gender = st.radio("Gender", [0, 1], index=None, format_func=gende_r)

        with col1:
            relationship = st.radio("Relationship Status", [1, 0], index=None, format_func=relation)

        with col2:
            education = st.radio("Educational Status", [1, 0], index=None, format_func=education_)

        with col1:
            employment = st.radio("Employment Status", [0, 1], index=None, format_func=employ_ment)

        property_area = property_area
        submitted = st.form_submit_button("Submit")
        if submitted:
            lst = [dependents, applicant, co_applicant, credit_history, loan_duration, loan_amount, education, relationship,
                   employment, gender, property_area]

            int_features = [int(x) for x in lst]
            final_features = [np.array(int_features)]
            prediction = model.predict(final_features)

            output = prediction[0]

            valid = ["No", "Yes"]

            if valid[output] == 'Yes':
                st.success("Eligible for a loan")
            else:
                st.warning("Not Eligible for a loan")
except TypeError:
    st.warning("Please fill the form appropriately.")
