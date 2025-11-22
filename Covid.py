import pandas as pd

#Load
file_path = "daily situation.csv"  
df = pd.read_csv(file_path)

print("Original data:")
print(df.head())

# Convert
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# Convert district 
district_columns = df.columns.tolist()
district_columns.remove('Date')  
df[district_columns] = df[district_columns].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)


df_long = df.melt(id_vars=['Date'], var_name='District', value_name='Daily_Cases')

# Save clean CSV
output_file = "sri_lanka_daily_situation.csv"
df_long.to_csv(output_file, index=False)

print(f"Daily situation saved as '{output_file}'")
print(df_long.head(10))
