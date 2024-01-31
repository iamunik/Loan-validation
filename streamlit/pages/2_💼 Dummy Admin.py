import streamlit as st
import pandas as pd
import condition
import joblib

st.set_page_config(
    page_title="Admin file upload",
    page_icon="💼",
)

model = joblib.load("./loan_model_class.pkl")

upload_file_extension = st.selectbox("What type of file do you want to upload?", ['CSV', 'XLS', 'XLSX'], index=None)
st.write(f"You want to upload a/an {upload_file_extension} file.")


try:
    if upload_file_extension == "CSV":
        a = st.file_uploader("Upload your file", type='.csv')
        df = pd.read_csv(a)
        col = df.columns

        if a:
            try:
                # Preprocessing was performed in the condition.py file; called the cleaner() function
                test_id = df['Loan_ID']
                cleaned_data = condition.cleaner(df)

                # Make predictions using your model
                predictions = model.predict(cleaned_data)
                prediction = list(predictions)

                # Mapping the prediction to make it presentable; called the p_mapping() function in condition.py
                mapas = condition.p_mapping(test_id, prediction)
                st.table(mapas)
            except KeyError:
                st.warning("Please visit the Rules for Upload page to see how to arrange your data.")

    elif upload_file_extension in ['XLS', 'XLSX']:
        a = st.file_uploader("Upload your file", type=['.xls', '.xlsx'])
        df = pd.read_excel(a, engine='openpyxl')
        col = df.columns

        try:
            if a:
                # Preprocessing was performed in the condition.py file; called the cleaner() function
                test_id = df['Loan_ID']
                cleaned_data = condition.cleaner(df)

                # Make predictions using your model
                predictions = model.predict(cleaned_data)
                prediction = list(predictions)

                # Mapping the prediction to make it presentable; called the p_mapping() function in condition.py
                mapas = condition.p_mapping(test_id, prediction)
                st.table(mapas)
        except KeyError:
            st.warning("Please visit the Rules for Upload page to see how to arrange your data.")
    else:
        st.warning("Select a file type")

except ValueError:
    st.warning("No file uploaded!")
