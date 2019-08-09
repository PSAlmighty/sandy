import tkinter as tk
from tkinter import messagebox  
import requests
from bs4 import BeautifulSoup
import PIL
from PIL import ImageTk
from PIL import Image
import pandas as pd
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
	name = t
	ls = split_string(t)
	ns = join_string(ls)
	ur2 = ns.lower()
	ur1 = "https://www.naukri.com/"
	ur = ur1+ur2+"-jobs-"
	page = my_entry2.get()
	
	#pages = int(page)
	if(page =="" ):
		pages = 2
	else:
		pages = int(page)
	#print(pages)

	#input("PRESS ENTER to EXIT")
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
	        try:
	        	d["Company"] = title[i].text.lstrip().rstrip()
	        except:
	        	d["Company"] = None
	        try:
	        	d["Location"] = loc[i].text
	        except:
	        	d["Location"] = None
	        try:
	        	d["Skills Required"] = desc[i].text.replace(",","-")
	        except:
	        	d["Skills Required"] = None
	        try:
	            d["Experience Required"] = exp[i].text
	        except:
	            d["Experience Required"] = None
	        
	        l.append(d)

	df = pd.DataFrame(l)
	df.to_csv("Naukri("+name+").csv",index=False)
	        

	#df1 = pandas.read_csv("shine.csv")
	messagebox.showinfo("SUCCESFULLY SCRAPED","You file is stored in: Naukri("+name+").csv")  
	root.destroy()

root = tk.Tk()

root.title("WWW.NAUKRI.COM")

path = "naukri-product.jpg"

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
my_head2 = tk.Label(root,text="BUILT BY: ")
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
