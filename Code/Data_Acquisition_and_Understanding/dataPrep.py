#Load the CSV File
import pandas as pd

#Load the CSV file using pandas
url = 'https://github.com/HanSquared/cmu-95829-Azure-TDSP/blob/main/Sample_Data/Raw/WA_Fn-UseC_-Telco-Customer-Churn.csv' 
data = pd.read_csv(url)
# Display the first few rows of the dataframe to ensure it's loaded correctly
print(data.head())
