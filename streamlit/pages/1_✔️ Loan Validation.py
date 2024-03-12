from condition import education_, relation, gende_r, pro_perty, employ_ment
import streamlit as st
import numpy as np
import os
import joblib

st.set_page_config(
    page_title="Loan Validation",
    page_icon="✔️",
)

st.title("Loan Validation")
st.write("Please fill the form to see if you're eligible for a loan.")

parent_dir = os.path.dirname(os.path.dirname(__file__))
path = model_path = os.path.join(parent_dir, "loan_model_class.pkl")

model = joblib.load(path)

try:
    # The form input
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
        # Submit button
        submitted = st.form_submit_button("Submit")
        if submitted:
            lst = [dependents, applicant, co_applicant, credit_history, loan_duration, loan_amount, education,
                   relationship, employment, gender, property_area]

            # Passing the features into a list and then an array for prediction
            int_features = [int(x) for x in lst]
            final_features = [np.array(int_features)]
            predictions = model.predict_proba(final_features)

            # Checking the eligibility of clients in percentage
            if predictions[0, 0] * 100 > predictions[0, 1] * 100:
                st.error(
                    f"There is a {round(predictions[0, 0] * 100)}% chance that your loan will not be approved")

            elif predictions[0, 1] * 100 > predictions[0, 0] * 100:
                st.success(
                    f"There is a {round(predictions[0, 1] * 100)}% chance that your loan will be approved")

            else:
                st.warning(
                    f"There is a {round(predictions[0, 1] * 100)}% chance that Employee Number'"
                    f"or goes")

    st.markdown("The higher your percentage of eligibility, the higher the chance of getting a loan from us"
                "<br>Please proceed to a branch closest to you for proper documentation", unsafe_allow_html=True)
except TypeError:
    st.warning("Please fill the form appropriately.")
