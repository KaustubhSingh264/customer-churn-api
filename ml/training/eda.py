import pandas as pd
DATA_PATH="ml/data/customer_churn.csv"


df=pd.read_csv(DATA_PATH)

#SHAPE OF DATAFRAME
print("SHAPE",df.shape) #5 rows and 21 columns

#COLUMNS OF DATA FRAME
print(df.columns.to_list(),"columns") #21 columns

#First 5 Rows
print("First 5 Rows:")
print(df.head())

#null values
print(df.isnull().sum()) #no null values

#target variable distribution
print("Target Variable Distribution:")
print(df['Churn'].value_counts()) #NO=5174 ,YES=1869


#TARGET PERCENTAGE
print("Target Variable Percentage:")
print(df['Churn'].value_counts(normalize=True)*100) #NO=73.46%,YES=26.54%

print(df["TotalCharges"].dtype)
print(df["TotalCharges"].tail())

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Check missing values created by conversion
print("Missing TotalCharges:", df["TotalCharges"].isnull().sum())


df = df.dropna(subset=["TotalCharges"])

print(df.isnull().sum().sum())