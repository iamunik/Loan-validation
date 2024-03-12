import pandas as pd
from sklearn import preprocessing


# Function to fill the null values of the uploaded file
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
    return table


# Encoding the categorical values using pd.series.map() method
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


# Scaling the df down
def scale(table):           # Scaling down the dataframe
    table = preprocessing.StandardScaler().fit_transform(table.astype(float))
    return table


# This function combines the fill_nan(), mapping() and scale() functions
def cleaner(table):         # Creating the clean table function from everything we have done
    clean_table = fill_nan(table)
    map_table = mapping(clean_table)
    scale_table = scale(map_table)
    return scale_table


# This is to map the prediction since it returns numbers we have to convert it to what the users will understand
def p_mapping(i_d, prediction):         # Mapping out the final result of the prediction
    data = {"Loan_ID": i_d, "Loan_Status": prediction}
    new_df = pd.DataFrame(data)
    new_df['Loan_Status'] = new_df['Loan_Status'].map({0: "Not Eligible", 1: "Eligible"}).astype(object)
    return new_df


# This function and all below it until stated otherwise were created to pass integers to the model
# The education radio button
def education_(educate):
    if educate == 1:
        return "Graduate"
    else:
        return "Non Graduate"


# Relationship radio button
def relation(relate):
    if relate == 1:
        return "Married"
    else:
        return "Not Married"


# Gender radio button
def gende_r(sex):
    if sex == 1:
        return "Female"
    else:
        return "Male"


# Property area radio button
def pro_perty(area):
    if area == 0:
        return "Urban"
    elif area == 1:
        return "Rural"
    else:
        return "Semi Rural"


# Employment status radio button
def employ_ment(employ):
    if employ == 0:
        return "Employee"
    else:
        return "Self Employed"
