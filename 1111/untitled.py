import pandas as pd
from sklearn.preprocessing import Label Encoder

obj_col = ['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']

for col in obj_col[1:]:
    label = LabelEncoder()
    loan[col] = label.fit_transform(loan[col])
    
    
