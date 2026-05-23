import pandas as pd
d={"A":[1,2,2,None],"B":[5,6,6,7]}
df=pd.DataFrame(d)
df=df.drop_duplicates()
df=df.dropna()
print(df)