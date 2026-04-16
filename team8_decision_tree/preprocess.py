import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('student_performance.csv')

cat_cols = df.select_dtypes(include=['object']).columns

for col in cat_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

# Target creation
df['pass'] = (df['G3'] >= 10).astype(int)

df.drop('G3', axis=1, inplace=True)

df.to_csv('student_clean.csv', index=False)

print("Preprocessing done!")