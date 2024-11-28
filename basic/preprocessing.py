#drop_na
import pandas as pd
bank=pd.read_csv("#2-bank-data(1).csv")

bank=bank.dropna()

bank.info()
 

#pcut(uniform)
import pandas as pd

bank=pd.read_csv("#2-bank-data(1).csv")
bank.info()

import numpy as np
bank["age"]=np.where(bank["age"].isnull(),np.nanmean(bank["age"]),bank["age"])
bank["income"]=np.where(bank["income"].isnull(),np.nanmean(bank["income"]),bank["income"])

import statistics

bank['married'] = np.where(bank['married'].isnull(),statistics.mode(bank['married']), bank['married'])


print(pd.cut(bank["age"],bins=3).value_counts())

bank["age"]=pd.cut(bank["age"],bins=3,labels=["18-34","35-50","51-67"])

bank.info()     

#qcut(bell-shape)
import pandas as pd

bank=pd.read_csv("#2-bank-data(1).csv")
bank.info()

import numpy as np
bank["age"]=np.where(bank["age"].isnull(),np.nanmean(bank["age"]),bank["age"])
bank["income"]=np.where(bank["income"].isnull(),np.nanmean(bank["income"]),bank["income"])

import statistics

bank['married'] = np.where(bank['married'].isnull(),statistics.mode(bank['married']), bank['married'])


print(pd.cut(bank["age"],bins=3).value_counts())

bank["age"]=pd.cut(bank["age"],bins=3,labels=["18-34","35-50","51-67"])

print(pd.qcut(bank["income"],q=3).value_counts())
bank["income"]=pd.qcut(bank["income"],q=3,labels=["L","M","H"])
bank["'children"]=bank["children"].astype(str)

new=bank.drop(["id"],axis=1,inplace=True)

bank.info()

bank.to_csv(r"bank-new.csv",index=False,encoding="utf_8_sig")
