import pandas as pd
from google.colab import files

# Upload Excel files
upload1 = files.upload()
upload2 = files.upload()

# Read uploaded files into pandas DataFrames
file1 = pd.read_csv(next(iter(upload1)))
file2 = pd.read_csv(next(iter(upload2)))

# Merge the files on the common column
merged_data = pd.merge(file1, file2, on='date')

# Save the merged data to a new Excel file
merged_data.to_csv('Grid2023.csv', index=False)

# Download the merged file
files.download('Grid2023.csv')