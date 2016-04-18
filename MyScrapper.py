import sys
import boto3
from bs4 import BeautifulSoup as BS
from myscript import scrape
import json
import requests
import csv

#this cralwer only works for the domian of search involving categories=men
#if there is this tag in the search query then its fine otherwise we will append it

################################################utilities to support the controller##########################################
#assimng that the crawler is on  an EC2 Instance , and it had stopped earlier at some positon in the read file,
#we will store the last position of read from the read file everytime we read into sqs
# on reinitiation from failure we will resume from that position
#get the last query position from the input file
def get_inp_line():
   s3 = boto3.resource('s3')
   sqs = boto3.client('sqs')
   
   inp = s3.get_object(Bucket='my_bucket', Key='input.csv')
   f = open(inp['Body'])
   reader = csv.reader(f)
   
   queue = sqs.get_queue_by_name(QueueName='my_queue')
   pos = queue.attributes.get('read_position')
   return f ,pos

#try to read next line from the csv fine   
def get_next_line(reader ):
     try:
       line = reader.next()
     except :
       return "EOF"
      
# simple utility to check is st is in string query   otherwise add st    
def check_for_domain(st , query):
   if st in query:
      return 1
   else :
      return 0
      

###############################################Main Controller that will control the inputs / scrapping / write in to DB###############################   
def  scrape_controller(domain):
   
    base_url = "http://www.hm.com/us/products/search?"
    inp_file,pos = get_inp_line()
    mark =0
    reader = open(inp_file,'r')
    while mark <pos:
         mark+=1
         reader.next()
    
     
    inp_line = get_next_line(reader)
    
    while inp_line !="EOF" :
    
            search_q , db_entry = inp_line.split('|')
            
            #to sort by new arrivals
            if !  check_for_domain("Orders=newfrom_desc",search_q):
                 search_q =  "Orders=newfrom_desc&"+search_q
            
            #in case none of the domain
            if !check_for_domain("categories=men",search_q)  and  !check_for_domain("categories=ladies",search_q)  and   !check_for_domain("categories=kids",search_q)  and  !heck_for_domain("categories=sale",search_q)  :
                  search_q =  domain+"&"+search_q
            # incase given domain
            elif check_for_domain(domain,search_q) : 
                     ;
            #incase of no doamin
            else :
                  continue
            
            q_url = base_url + search_q
            try: 
                my_items= scrape(q_url)
                save_to_db(my_items)
            except :
                print ("unable to scrape from "+q_url)
                
            inp_line=get_next_line(reader)
            
           
           
     
                
            
            
            
            
  
        
    
    
         
    
    
    
    
         
       
     
   
   
        



