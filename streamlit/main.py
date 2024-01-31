import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Welcome to G-oan",
    page_icon="💰",
)

st.title("Welcome to G-oan")

st.subheader("Your Trusted Financial Partner")

file_ = open("GIFFY.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="500" height="250">',
    unsafe_allow_html=True,
)
file_.close()

st.write("""<br>
At <b>G-oan</b>, we understand that life is full of opportunities and challenges that may require a helping hand.  
As a premier fictional loan company, we take pride in being your trusted financial partner, dedicated to providing 
personalized and reliable lending solutions. With a commitment to excellence and customer satisfaction, we are here to
support you on your journey to financial success.""", unsafe_allow_html=True)

# Functionalities of the site.

st.markdown("""
# Functionalities of this web app
### User Input Prediction:
- Users have the option to manually input loan details through a user-friendly interface.
- Input fields cover essential loan parameters such as amount, duration, interest rate, etc.
- Predictions are generated based on the provided user inputs.

### File Upload Prediction:
This part of the web app is for the admin, incase there are customers that comes to check their eligibility and there 
are back logs the admin can upload a csv file or an excel file for the purpose of predicting the customers 
that are eligible for a loan.

### Limitations:
- This web app is not global for all loan companies, that is because the ML algorithm in use was created with data from
a particular source, if you want this you will have to <a href="https://oluwaseun-ogundeko.netlify.app/contact">
contact me</a> and we can discuss building one for
your organisation.
- This web app is mainly for testing purpose just to show what is possible using Machine Learning.
""", unsafe_allow_html=True)
st.warning("Development is still ongoing for this web app to improve the ML algorithm.")

