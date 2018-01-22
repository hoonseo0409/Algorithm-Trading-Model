import platform
import pandas as pd
import test

print (platform.architecture())
i=1
df64=pd.DataFrame([[0,64], [0,64]])


while True:

    df64_add = pd.DataFrame([[i, 64], [i, 64]])
    df64=df64.append(df64_add)
    print (df64.shape)
    df64.to_csv("../df64.csv", encoding="utf-8")
    i=i+1