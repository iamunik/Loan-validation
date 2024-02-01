import streamlit as st

st.set_page_config(
    page_title="Rules for file upload",
    page_icon="🧾",
)

st.write("""
               # File Upload Guidelines
               <hr>

               <h3><u>Introduction:</u></h3>
               <p>Welcome to our file upload guideline page! This platform allows users to upload spreadsheet files to
                test a machine learning algorithm designed to predict the validity of customers for loan collection.</p>

               <h3><u>File Types:</u></h3>
               <p>You can upload files in the following formats:
                    <ul>
                         <li>Comma Seperated Values (.csv)</li>
                         <li>Excel spreadsheet (.xls)</li>
                    </ul>
               </p>

               <h3><u>User Authentication:</u></h3>
               <p>No user authentication is required for this test run. Feel free to upload files without the need to 
               log in.</p>

               <h3><u>Privacy and Security:</u></h3>
               <p>Rest assured, uploaded files are not stored on our servers. They are used solely for making 
               predictions, and your privacy and security are not compromised, as files are not retained and also please
            note that file uploads are not moderated or reviewed before processing, hence the need for users to read 
            through the <b>"Acceptable Content"</b> section thoroughly</p>

               <h3><u>Acceptable Content:</u></h3>
               <p>Uploaded files must follow a specific format and contain the following columns names with the 
               corresponding data types:</p>

               <table style="width: 100%;" class="table text-light">
               <thead>
                    <tr>
                         <th style="width: 50%;"><b>Column Name</b></th>
                         <th><b>Data Type</b></th>
                    </tr>
               </thead>
               <tbody>
                    <tr>
                         <td>Loan_ID</td>
                         <td>Unique Identifier (Alphanumeric)</td>
                    </tr>
                    <tr>
                         <td>Gender</td>
                         <td>Text (Male/Female)</td>
                    </tr>
                    <tr>
                         <td>Married</td>
                         <td>Text (Yes/No)</td>
                    </tr>
                    <tr>
                         <td>Dependents</td>
                         <td>Integer (Number of Dependents)</td>
                    </tr>
                    <tr>
                         <td>Education</td>
                         <td>Text (Graduate/Not Graduate)</td>
                    </tr>
                    <tr>
                         <td>Self_Employed</td>
                         <td>Text (Yes/No)</td>
                    </tr>
                    <tr>
                         <td>ApplicantIncome</td>
                         <td>Float (Applicant's Income)</td>
                    </tr>
                    <tr>
                         <td>CoapplicantIncome</td>
                         <td>Float (Coapplicant's Income)</td>
                    </tr>
                    <tr>
                         <td>LoanAmount</td>
                         <td>Float (Loan Amount in Dollars)</td>
                    </tr>
                    <tr>
                         <td>Loan_Amount_Term</td>
                         <td>Intger (Loan Term in Days)</td>
                    </tr>
                    <tr>
                         <td>Credit_History</td>
                         <td>Float (0.0 - 1.0)</td>
                    </tr>
                    <tr>
                         <td>Property_Area</td>
                         <td>Text (Urban/Semiurban/Rural)</td>
                    </tr>
               </tbody>
               </table>

               <p>Below is an explanation for each of the columns required for loan data:</p>

               <ul>
                    <li>
                         <strong>Loan_ID:</strong> This column should contain a unique identifier, typically 
                         alphanumeric, to identify each loan record.
                    </li>
                    <li>
                         <strong>Gender:</strong> This column represents the gender of the applicant 
                         (e.g., Male or Female).
                    </li>
                    <li>
                         <strong>Married:</strong> This column indicates whether the applicant is married 
                         (e.g., Yes or No).
                    </li>
                    <li>
                         <strong>Dependents:</strong> It specifies the number of dependents of the applicant, typically 
                         represented as a numeric value.
                    </li>
                    <li>
                         <strong>Education:</strong> This column indicates the education level of the applicant 
                         (e.g., Graduate or Not Graduate).
                    </li>
                    <li>
                         <strong>Self_Employed:</strong> It represents whether the applicant is self-employed 
                         (e.g., Yes or No).
                    </li>
                    <li>
                         <strong>ApplicantIncome:</strong> This column should contain the numeric value representing 
                         the applicant's income.
                    </li>
                    <li>
                         <strong>CoapplicantIncome:</strong> It contains the numeric value representing the 
                         coapplicant's income.
                    </li>
                    <li>
                         <strong>LoanAmount:</strong> This column represents the numeric value indicating the loan 
                         amount, typically in thousands.
                    </li>
                    <li>
                         <strong>Loan_Amount_Term:</strong> It specifies the numeric value representing the loan term 
                         in months.
                    </li>
                    <li>
                         <strong>Credit_History:</strong> This column typically contains the credit history of the 
                         applicant, represented as a numeric value between 0.0 and 1.0.
                    </li>
                    <li>
                         <strong>Property_Area:</strong> This column indicates the property area where the applicant 
                         resides (e.g., Urban, Semiurban, or Rural).
                    </li>
               </ul>

               <h3><u>Ownership:</u></h3>
               <p>Everyone has the right to upload content. There are no restrictions on who can submit files for 
               testing.</p>

               <h3><u>User Agreement:</u></h3>
               <p>No user agreements are required for file uploads. You can start uploading right away.</p>

               <h3><u>User Support:</u></h3>
               <p class="mb-5">Should you have any questions or concerns regarding file uploads or the testing process 
               or if you need to reach out for any reason, our user support team is here to assist you. Fill the 
               <a href="https://oluwaseun-ogundeko.netlify.app/contact">Contact form</a> stating your
               issue and potential upgrades for assistance.</p>

""", unsafe_allow_html=True)
