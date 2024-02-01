import streamlit as st
import pandas as pd
import condition
import joblib
import os


st.set_page_config(
    page_title="Admin file upload",
    page_icon="💼",
)
# Loading the machine learning model
parent_dir = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(parent_dir, "loan_model_class.pkl")
model = joblib.load(model_path)


st.title("Dummy Admin Page")

# Download button for the test data
st.write("Download the csv file below to test the algorithm")

df = pd.read_csv(os.path.join(parent_dir, "test_loan.csv"))
test_file = st.download_button(label="Download test data",
                               data=df.to_csv(index=False).encode('utf-8'),
                               file_name="Test data.csv")

# Upload file for the web app
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
            st.warning("Please visit the Rules for Upload page to see what data is needed.")
    else:
        st.warning("Select a file type")

except ValueError:
    st.warning("Please confirm that a file is uploaded")
