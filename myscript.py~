from bs4 import BeautifulSoup as BS
import json

import requests
#NEED BOTO connection to push the function to the AWS EMR
#NEED EBS connection object to write csv on server
#NEED REDIS server object to logg onto AWS or local machine
#NEED fabric for deploying on AWS using authorization id and secret key

link = "http://www.hm.com/us/products/ladies/dresses_jumpsuits"

def crawler(link)
 r= requests.get()
 soup = BS(r.text)
 prlist = soup.find_all('ul', {'class': 'products-list'})
 soup= prlist[0].find_all('li')
 for item in soup:
       # soup1 = BS(item)
        #print "#######################################"
        
        item_id="";   category="";item_name="";  size="";   color=""; 
        pattern=""; item_pic="" ; price="" ;    item_link="";
        
        prod={}     
        
        #item picture  
        try: 
            tmp =    item.find_all('div' , {'class' : 'image'})[0]
            item_pic = tmp.find_all('img')[0]['src']
            prod['item_pic'] = 'http:'+item_pic
            #print "item_pic   ",(prod['item_pic'])
        except :
            pass
            
        #item link
        try: 
            tmp =    item.find_all('div')[0]
            prod['item_link'] = tmp.find_all('a')[0]['href'] 
            prod['item_id']  = prod['item_link'].split("article=")[1] 
            #print "item_id   ",(prod['item_id'])  
            #print "item_link   ",(prod['item_link'])  
        except :
            pass
         
        #item name    
        try :
           #print item.find_all('a')[0]
           prod['item_name']= item.find_all('a')[0]['title']
           print "item_name  ",(prod['item_name'])
        except :
            pass
            
        #item inofrmation
        try : 
           info = item.find_all('div',{'class' : 'product-info'})[0]
           #print info
           prod['details']=info.findAll("div", {"class": "details"})[0].string.strip(" ")
           prod['price'] = info.findAll("div", {"class": "price"})[0].findAll('span')[0].string.strip(" ")
           #print "item_details  ",(prod['details']) 
           #print "item_price  ",prod['price']
        except :
            pass
            
        try : 
           clrs = item.find_all('ul',{'class' : 'colours'})[0]
           
           clrs1= clrs.findAll('li')[0].findAll('div')[0]['style'].split('(')[1] 
           prod['color']=clrs1.split(')')[0]
           #print clrs1
           #prod['color']=clrs.findAll('div')[0]['style'].split('(').split(')')
           #print "item_color  ",(prod['color']) 
        except :
            pass   
        
        
        
        #print json.dumps(prod,indent=4)
        #print prod['details']
        #print len(prlist)
        


crawler(link)

'''
Category//
ID//
Item_name// 
Size //
Color 
Pattern //
Price//
ImageURL//
Item_link
'''
