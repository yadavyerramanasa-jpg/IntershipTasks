import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
d={"A":[1,2,3,4],"B":[2,4,6,8],"C":[1,3,5,7]}
df=pd.DataFrame(d)
sns.heatmap(df.corr(),annot=True)
plt.show()