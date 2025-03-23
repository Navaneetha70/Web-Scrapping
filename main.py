import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.iplt20.com/auction/2020"
r=requests.get(url)

#print(r)
soup=BeautifulSoup(r.text,"html.parser")
table=soup.find("table",class_="ih-td-tab w-100 auction-tbl")
#print(table)
header=table.find_all("th")
titles=[]
for i  in header :
    title=i.text
    titles.append(title)
    #print(title)
    df=pd.DataFrame(columns=titles)
    #print(df)
rows=table.find_all("tr")
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_= "ih-pt-ic")
    data=i.find_all("td")[1:]
    row =[tr.text for tr in data]
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row
    df["TEAM"] = df["TEAM"].apply(lambda x: x.strip())
print(df)
df.to_csv("IPL_auction_states_2022.csv")