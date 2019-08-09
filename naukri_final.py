import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import csv

print("=========WEBSITE SCRAPER===========")
print("===========NAUKRI.COM==================")
print("==BUILT BY: ===========================")

t=input("Keyword Search: ")

def split_string(string): 
  
    list_string = string.split(' ') 
      
    return list_string 
  
def join_string(list_string): 
  
    string = '-'.join(list_string) 
      
    return string 
name = t

ls = split_string(t)

ns = join_string(ls)
ur2 = ns.lower()
ur1 = "https://www.naukri.com/"


ur = ur1+ur2+"-jobs-"
#url ="https://www.naukri.com/oracle-plsql-jobs"
pages = int(input("No. of pages you want: "))

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
l = []
full = int(pages)+1
for j in range(1,full):
    #t = count
    url = ur+str(j)
    print(url)
    r = requests.get(url, headers=headers)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")

    title = soup.find_all("span",{"class":"org"})
    #print(len(title))
    loc = soup.find_all("span",{"class":"loc"})
    
    desc = soup.find_all("span",{"class":"skill"})
    
    exp = soup.find_all("span",{"class":"exp"})
    
    
    
    for i in range(0,len(title)):
        d = {}
        d["Company"] = title[i].text.lstrip().rstrip()
        d["Location"] = loc[i].text
        d["Skills Required"] = desc[i].text.replace(",","-")
        d["Experience Required"] = exp[i].text
        l.append(d)

df = pd.DataFrame(l)
df.to_csv("Naukri("+name+").csv",index=False)

input("PRESS ENTER TO EXIT")