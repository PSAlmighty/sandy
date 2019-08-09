import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
plt.style.use('seaborn')
import pandas
#from urllib.request import urlopen
#import urllib.request
#from selenium  import webdriver
#import time
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path='C:\Webdriver\chromedriver.exe')
#driver.get("https://www.shine.com/job-search/oracle-plsql-jobs")
#proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}

print("=========WEBSITE SCRAPER===========")
print("===========SHINE.COM==================")
print("==BUILT BY: Sandeep ===========================")

t=input("Keyword Search: ")

def split_string(string): 
  
    list_string = string.split(' ') 
      
    return list_string 
  
def join_string(list_string): 
  
    string = '-'.join(list_string) 
      
    return string 

lt = str.lower(t)
ls = split_string(lt)
ns = join_string(ls)
ur2 = ns.lower()
ur1 = "https://www.shine.com/job-search/-"


ur = ur1+ur2+"-jobs-"

pages = int(input("No. of pages you want: "))



import csv
#w = csv.writer(open("shine.csv","w"))
w = csv.writer(open("shine("+t+").csv","w"))
#w.writerow(['Company','Location','Description','Experience Reqd','Date Posted'])
w.writerow(['Company','Location','Description','Experience Reqd'])
for j in range (1,pages):    
    #url = "https://www.shine.com/job-search/oracle-plsql-jobs-"+str(j)
    url = ur+str(j)
    print(url)
    r = requests.get(url,headers=headers)
    #r = requests.get("https://www.shine.com/job-search/oracle-plsql-jobs-"+str(j),proxies=proxies)
    c = r.text
        
    soup = BeautifulSoup(c,"html.parser")

    headin = soup.find_all("li",{"class":"snp cls_jobtitle"})
   
    cmp_name = soup.find_all("li",{"class":"snp_cnm cls_cmpname cls_jobcompany"})

    title = soup.find_all("li",{"class":"snp_yoe_loc jobList-year-loc"})

    job_desc = soup.find_all("li",{"class":"srcresult"})    

   # pos = soup.find_all("li",{"class":"time share_links jobDate cls_job_date_format"})
    
    for i in range(0,len(headin)):
        w.writerow([str(cmp_name[i].text.replace("\n"," ").lstrip().rstrip().encode(encoding='UTF-8',errors='strict'))[2:-1],
                    str(title[i].find_all("em",{"class":"snp_loc"})[0].text.replace("\n"," ").lstrip().rstrip().encode(encoding='UTF-8',errors='strict'))[2:-1],
                    str(job_desc[i].text.replace("\n","").lstrip().rstrip().encode(encoding='UTF-8',errors='strict'))[2:-1],
                    str(title[i].find_all("span",{"class":"snp_yoe cls_jobexperience"})[0].text.replace("\n","").lstrip().rstrip().encode(encoding='UTF-8',errors='strict'))[2:-1]])
                    #pos[i].text.replace("\n","").lstrip().rstrip()])
        

df1 = pandas.read_csv("shine.csv")

df1['Location'].value_counts().sort_values().plot(kind='barh', color='darkgrey')
plt.title("No. of "+str.upper(t)+" jobs available")
plt.ylabel("Cities")
plt.xlabel("No. of jobs")
plt.savefig('shine_visual('+t+').png')
      
#encode('uft8')
input("Prompt:")

