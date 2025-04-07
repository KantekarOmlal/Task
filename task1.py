import pandas as pd
df = pd.read_csv("Medical Appointment No Shows.csv")  

#1
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
)

# 2.Converting date columns to datetime
df['scheduledsay'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# 3.Standardize categorical text data
df['gender'] = df['gender'].str.upper().str.strip()
df['no-show'] = df['no-show'].str.capitalize().str.strip()

# 4.Removing duplicates
df.drop_duplicates(inplace=True)

# 5. Check and handle missing values
print(df.isnull().sum())
df.dropna()

print(df.dtypes)  

df = df[df['age'] >= 0]

# Save dataset
df.to_csv("cleaned_data.csv", index=False)