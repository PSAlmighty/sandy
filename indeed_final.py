import requests
from bs4 import BeautifulSoup
import csv

print("=========WEBSITE SCRAPER===========")
print("===========INDEED==================")
print("====BUILT BY: =====================")

t=input("Keyword Search: ")
def split_string(string): 
  
    list_string = string.split(' ') 
      
    return list_string 
  
def join_string(list_string): 
  
    string = '+'.join(list_string) 
      
    return string 

str.lower(t)
ls = split_string(t)
ur2 = join_string(ls)
ur1 = "https://www.indeed.co.in/jobs?q="

pages = int(input("The Number of Pages you want: "))

w = csv.writer(open("Indeed("+t+").csv", "w"))
w.writerow(['Job Title','Company','Location','Description'])
page_nr = 0;
proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}

for j in range(0,pages):
    k = 0
    if(j == 0):
        url = ur1+ur2+"+&l="
        print(url)
        #print("https://www.indeed.co.in/jobs?q=oracle+plsql&l=")
        r = requests.get(url,proxies=proxies)
        #r = requests.get("https://www.indeed.co.in/jobs?q=oracle+plsql&l=",proxies=proxies)
        c = r.content
    else:
        url = ur1+ur2+"&start="+str(page_nr)
        print(url)
        #print("https://www.indeed.co.in/jobs?q=oracle+plsql&start="+str(page_nr))
        r =  requests.get(url,proxies=proxies)
        #r = requests.get("https://www.indeed.co.in/jobs?q=oracle+plsql&start="+str(page_nr),proxies=proxies)
        c = r.content
    page_nr = page_nr+10;    
    
    soup = BeautifulSoup(c,"html.parser")
    
    title = soup.find_all("div",{"class":"title"})
    
    desc = soup.find_all("div",{"class":"summary"})
    
    cmp = soup.find_all("span",{"class":"company"})
    
    loc = soup.find_all("div",{"class":"location"})
    
    loc1 = soup.find_all("span",{"class":"location"})
    
    for i in range(0,10):
        try:
            w.writerow([str(title[i].text.replace("\n"," ").lstrip().rstrip().encode('utf-8'))[2:-1],
                       str(soup.find_all("span",{"class":"company"})[i].text.replace("\n"," ").lstrip().rstrip().encode('utf-8'))[2:-1],
                       str(loc[i].text.rstrip().encode('utf-8'))[2:-1],
                       str(desc[i].text.replace("\n"," ").lstrip().rstrip().encode('utf-8'))[2:-1]])
        except:
            w.writerow([str(title[i].text.replace("\n"," ").lstrip().rstrip().encode('utf-8'))[2:-1],
                       str(soup.find_all("span",{"class":"company"})[i].text.replace("\n"," ").lstrip().rstrip().encode('utf-8'))[2:-1],
                       str(loc1[k].text.rstrip().encode('utf-8'))[2:-1],
                       str(desc[i].text.replace("\n"," ").lstrip().rstrip().encode('utf-8'))[2:-1]])  
            k = k + 1
            
    