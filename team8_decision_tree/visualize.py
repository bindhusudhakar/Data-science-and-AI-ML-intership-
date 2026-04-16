import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

df = pd.read_csv('student_clean.csv')

X = df.drop('pass', axis=1)
y = df['pass']

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Tree
plt.figure(figsize=(20,10))
plot_tree(model, max_depth=3, filled=True)
plt.savefig("tree.png")
plt.show()

# Feature importance
import pandas as pd
fi = pd.Series(model.feature_importances_, index=X.columns)
fi.nlargest(10).plot(kind='barh')
plt.savefig("importance.png")
plt.show()