import tkinter as tk
from tkinter import messagebox  
import requests
from bs4 import BeautifulSoup
import PIL
from PIL import ImageTk
from PIL import Image
#import matplotlib.pyplot as plt
#plt.style.use('seaborn')
#import pandas

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


def split_string(string): 
  
    list_string = string.split(' ') 
      
    return list_string 
  
def join_string(list_string): 
  
    string = '-'.join(list_string) 
      
    return string 


def my_function():
	t = my_entry.get()
	lt = str.lower(t)
	ls = split_string(lt)
	ns = join_string(ls)
	ur2 = ns.lower()
	ur1 = "https://www.shine.com/job-search/-"
	ur = ur1+ur2+"-jobs-"
	#url_member = "https://api.example.com/member?member_id="+str(current_id)
	#print(ur)
	page = my_entry2.get()
	
	#pages = int(page)
	if(page =="" ):
		pages = 2
	else:
		pages = int(page)
	#print(pages)

	#input("PRESS ENTER to EXIT")
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
	        

	#df1 = pandas.read_csv("shine.csv")
	messagebox.showinfo("SUCCESFULLY SCRAPED","You file is stored in: shine("+t+").csv")  
	root.destroy()

root = tk.Tk()

root.title("WWW.SHINE.COM")

path = "NewShinelogo.jpg"

#width = 2000
#height = 1500
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()
root.geometry("400x315")

img = ImageTk.PhotoImage(Image.open(path))


panel = tk.Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(row = 8,column = 0)

my_head = tk.Label(root,text="WEBSITE SCRAPPER")
my_head.grid(row=0,column=1)
my_head2 = tk.Label(root,text="BUILT BY: SANDEEP")
my_head2.grid(row=1,column=1)

my_label = tk.Label(root, text = "Enter KEYWORD: ")
my_label.grid(row = 3, column = 0)
my_entry = tk.Entry(root)
my_entry.grid(row = 3, column = 1)

#my_button = tk.Button(root, text = "Submit", command = my_function)
#my_button.grid(row = 3, column = 1)

my_label2 = tk.Label(root, text = "No. Of Pages You Want: ")
my_label2.grid(row = 5, column = 0)

my_entry2 = tk.Entry(root)
my_entry2.grid(row = 5, column = 1)


my_button2 = tk.Button(root, text = "Submit", command = my_function)
my_button2.grid(row = 6, column = 1)




root.mainloop()
