import pandas as pd
from sklearn import preprocessing


def fill_nan(table):        # Filling empty columns and rows
    # Filling the numerical values first
    table['Credit_History'] = table['Credit_History'].fillna(table['Credit_History'].mean())
    # Loan Amount Term
    table['Loan_Amount_Term'] = table['Loan_Amount_Term'].fillna(table['Loan_Amount_Term'].mean())
    # Loan Amount
    table['LoanAmount'] = table['LoanAmount'].fillna(table['LoanAmount'].mean())

    # Filling up the categorical values next

    # Gender
    table['Gender'] = table['Gender'].fillna(table['Gender'].mode()[0])
    # Married
    table['Married'] = table['Married'].fillna(table['Married'].mode()[0])
    # Self_Employed
    table['Self_Employed'] = table['Self_Employed'].fillna(table['Self_Employed'].mode()[0])
    # The dependent column is an object but to do what I need to do I will have to first strip the values of the column
    # From the + in front of it
    table['Dependents'] = table['Dependents'].apply(lambda x: str(x).rstrip('+'))
    # Then convert to numbers
    table['Dependents'] = pd.to_numeric(table['Dependents'], errors='coerce', downcast='integer')
    # Then fill them up
    table['Dependents'] = table['Dependents'].fillna(table['Dependents'].mode()[0])
    # Drop the LOAN ID on the csv file
    table.drop(['Loan_ID'], axis=1, inplace=True)
    # Creating Total Income column because that's what we trained it with
    table['Total_Income'] = table['ApplicantIncome'] + table['CoapplicantIncome']
    table.drop(['ApplicantIncome', 'CoapplicantIncome'], axis=1, inplace=True)
    return table


def mapping(table):         # Manually encoding the categorical values
    # Gender Variable
    table['Gender'] = table['Gender'].map({'Male': 0, 'Female': 1}).astype(int)
    # Married Variable
    table['Married'] = table['Married'].map({'No': 0, 'Yes': 1}).astype(int)
    # Education Variable
    table['Education'] = table['Education'].map({'Not Graduate': 0, 'Graduate': 1}).astype(int)
    # Self_Employed Variable
    table['Self_Employed'] = table['Self_Employed'].map({'No': 0, 'Yes': 1}).astype(int)
    # Credit_History Variable
    table['Credit_History'] = table['Credit_History'].astype(int)
    # Property_Area Variable
    table['Property_Area'] = table['Property_Area'].map({'Urban': 0, 'Rural': 1, 'Semiurban': 2}).astype(int)
    # Dependents Variable
    table['Dependents'] = table['Dependents'].astype(int)
    return table


def scale(table):           # Scaling down the dataframe
    table = preprocessing.StandardScaler().fit_transform(table.astype(float))
    return table


def cleaner(table):         # Creating the clean table function from everything we have done
    b = fill_nan(table)
    a = mapping(b)
    c = scale(a)
    return c


def p_mapping(i_d, prediction):         # Mapping out the final result of the prediction
    data = {"Loan_ID": i_d, "Loan_Status": prediction}
    new_df = pd.DataFrame(data)
    new_df['Loan_Status'] = new_df['Loan_Status'].map({0: "No", 1: "Yes"}).astype(object)
    return new_df
