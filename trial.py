# Merge the two DataFrames based on the 'PATIENT' ID
merged_df = pd.merge(df_patients, df_conditions, how='left', left_on='Id', right_on='PATIENT')

# Select and rearrange relevant columns
final_df = merged_df[['Id', 'FIRST', 'LAST', 'DESCRIPTION', 'AGE', 'GENDER', 'RACE', 'ETHNICITY']]

# Save the merged DataFrame to a new Excel file
final_df.to_excel('patient_conditions.xlsx', index=False)

# Display the first few rows of the final DataFrame
print(final_df.head())