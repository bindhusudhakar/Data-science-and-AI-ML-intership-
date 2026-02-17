import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
"Customer_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
"Gender":
["Male","Female","Female","Male","Male","Female","Male","Female","Male","Female"],
"Age": [25,32,28,45,36,23,40,29,31,27],
"City_Tier": [1,2,1,3,2,1,3,2,1,2],
"Avg_Session_Time": [15,10,18,8,12,20,7,16,14,19], # in minutes
"Pages_Visited": [5,3,6,2,4,8,2,5,6,7],
"Products_Viewed": [3,2,4,1,2,5,1,3,4,4],
"Previous_Purchases": [2,1,3,0,1,4,0,2,3,3],
"Discount_Used": [1,0,1,0,1,1,0,1,1,1], # 1=Yes, 0=No
"Total_Spend": [1200,600,1800,300,900,2500,250,1500,2000,1700]
}

df = pd.DataFrame(data)

plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
