import pandas as pd
import matplotlib.pyplot

a = pd.read_csv('./incheon.csv')

High_T = a.head(6)['최고기온(℃)']


print(High_T)
print('*'*10)
print(High_T.max())
