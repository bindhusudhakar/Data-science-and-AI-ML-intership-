import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned = usernames.str.strip()
cleaned = cleaned.str.lower()
cleaned = usernames.str.strip().str.lower()
contains_a = cleaned.str.contains('a')
print("Cleaned Usernames:")
print(cleaned)

print("\nNames containing letter 'a':")
print(contains_a)
