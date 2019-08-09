import requests
from bs4 import BeautifulSoup
import csv

print("=========WEBSITE SCRAPER===========")
print("===========TIMES JOBS==================")
print("======Built By: ==================")

t=input("Search: ")
def split_string(string): 
  
    list_string = string.split(' ') 
      
    return list_string 
  
def join_string(list_string): 
  
    string = '%20'.join(list_string) 
      
    return string 

sv = str.lower(t)
 
ls1 = split_string(t)
ur1 = join_string(ls1)

ls2 = split_string(str.lower(t))
ur2 = join_string(ls2)
ur = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords="+ur1+"&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords="+ur2+"&pDate=I&sequence="

pages = int(input("Enter the number of pages you want: "))

proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}

page_nr = 1
w = csv.writer(open("times("+sv+").csv","w"))
w.writerow(["Company","Location","Experience Required","Skills Required"])
for j in range(0,pages):
    
    #url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Oracle%20PL%20SQL%20Developer&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=oracle%200DQT0pl%20sql%20developer0DQT0&pDate=I&sequence="+str(page_nr)+"&startPage=1"
    url = ur+str(page_nr)+"&startPage=1"
    r = requests.get(url,proxies = proxies)
    #r.status_code
    c = r.content

    soup = BeautifulSoup(c,"html.parser")


    all = soup.find_all("li",{"class":"clearfix job-bx wht-shd-bx"})

    print("=========== "+str(page_nr)+" ===============")
    print(url)
    #print("\n")
    #url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Oracle%20PL%20SQL%20Developer&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=oracle%200DQT0pl%20sql%20developer0DQT0&pDate=I&sequence="+str(page_nr)+"&startPage=1"
    page_nr = page_nr+1
    for i in range(0,25):
        w.writerow([all[i].find_all("h3",{"class":"joblist-comp-name"})[0].text.replace("\r","").replace("\n","").lstrip().rstrip(),
                    all[i].find_all("span")[0].text.lstrip().rstrip(),
                    all[i].find_all("li")[0].text.replace("card_travel","").lstrip().rstrip(),
                    all[i].find_all("span",{"class":"srp-skills"})[0].text.replace("\n","").replace("\r","").replace(",","-").lstrip().rstrip()])
        
    #print("\n")
    
    
    #print("\n")