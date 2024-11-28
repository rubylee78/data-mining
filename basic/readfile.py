#txt
with open ("cardata.txt","r") as f:
    data=[]
    for line in f:
        data.append(line.strip().split(","))
    
import pandas as pd

new=pd.DataFrame(data,columns=["價格","品質","幾人坐","幾捫","行李箱大小","維修費用","是否推薦"])

#JSON
import json 
import pandas as pd

with open("pokemon.json","r") as file:
    df=pd.DataFrame(json.load(file))
    
with open ("pokemon.json","r") as f:
    pokemon=(json.load(f))
    df2=pd.DataFrame(pokemon)
    
#CSV(開頭為資料)
import pandas as pd
NBApoints_data=pd.read_csv("NBApoints.csv",header=None)

#CSV(開頭為資料)
import pandas as pd
NBApoints_data=pd.read_csv("NBApoints.csv")

#CSV(中文資料)
import pandas as pd
a=pd.read_csv("a.csv",encoding="CP950")

#XML
import xml.etree.ElementTree as ET
tree= ET.parse("read.xml")
root=tree.getroot()

data=[]
for row in root :
    sno=row.find("sno").text
    sna=row.find("sna").text
    tot=row.find("tot").text
    data.append([sno,sna,tot])
    
import pandas as pd 
ubike=pd.DataFrame(data,columns=["sno","sna","tot"])