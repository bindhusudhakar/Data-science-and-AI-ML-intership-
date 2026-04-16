from ucimlrepo import fetch_ucirepo
import pandas as pd

student = fetch_ucirepo(id=320)

X = student.data.features
y = student.data.targets

df = X.copy()
df['G3'] = y['G3']

df.to_csv('student_performance.csv', index=False)

print("Dataset saved!", df.shape)