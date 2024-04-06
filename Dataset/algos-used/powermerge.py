import pandas as pd
from io import BytesIO
from google.colab import files

# Upload CSV files
uploads = [files.upload() for _ in range(5)]

# Read uploaded files into pandas DataFrames
files_list = [pd.read_csv(BytesIO(next(iter(upload.values())))) for upload in uploads]

# Concatenate the DataFrames horizontally
merged_data = pd.concat(files_list)

# Save the merged data to a new CSV file
merged_data.to_csv('Power19-23.csv', index=False)

# Download the merged file
files.download('Power19-23.csv')