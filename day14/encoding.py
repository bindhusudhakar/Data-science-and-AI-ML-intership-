import pandas as pd

# Creating dataset
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
}

df = pd.DataFrame(data)

print(df)

df["Transmission"] = df["Transmission"].map({
    "Automatic": 0,
    "Manual": 1
})

print(df)

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df)
