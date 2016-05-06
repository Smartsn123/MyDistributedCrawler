from bs4 import BeautifulSoup as BS
import json
import json
import urllib2

#utility to scrape all the items listed on page hm.com 
def scrape(link):
 page = urllib2.urlopen(link)
 soup = BS(page.read())
 prlist = soup.find('ul', {'class': 'products-list'})
 #print len(prlist)
 prlist = prlist. findAll('li')
 res_list=[]
 i=0
 for item in prlist:
        #print str(i)+"########################################################################"
        #i+=1
        #print item
        prod={}     
        #item picture  
        try: 
            tmp =    item.find_all('div' , {'class' : 'image'})[0]
            item_pic = tmp.find_all('img')[0]['src']
            prod['item_pic'] = 'http:'+item_pic
        except :
            pass
            
        #item link
        try: 
           
            prod['item_url'] = item.find_all('a')[0]['href'] 
            prod['item_id']  = prod['item_url'].split("article=")[1] 
            #print "item_id   ",(prod['item_id'])  
            #print "item_link   ",(prod['item_link'])  
        except :
            pass
         
        #item name    
        try :
           #print item.find_all('a')[0]
           prod['item_name']= item.find_all('a')[0]['title']
           #print "item_name  ",(prod['item_name'])
        except :
            pass
            
        #item inofrmation
        try : 
           info = item.find_all('div',{'class' : 'product-info'})[0]
           #print info
           #prod['pattern']=info.findAll("div", {"class": "details"})[0].string.strip(" ")
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
        
        
        
        if 'item_name' in prod.keys():
            res_list.append(prod)
            #print json.dumps(prod, indent=4)
   
 #print len(res_list)     
 return res_list

#link1 = "http://www.hm.com/us/products/search?categories=ladies&term=gingham%20shirts"
#scrape(link1)

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
