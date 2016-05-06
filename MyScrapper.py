import sys
import boto3
from bs4 import BeautifulSoup as BS
from scrape import scrape
import json
import requests
import csv

##############################################connection to the RDS MySQL DB##########################################
'''
try :
 client = boto3.client('rds')
 instances = client.get_all_dbinstances("sunnydb")
 db = instances[0]
 db.status
except :
  print "Failed to connect to DB instance"  
'''
#############################################################################################################


##############################################connection to the AWS SQS anfd S3###########################################
try:
 sqs = boto3.client('sqs')
 queue = sqs.get_queue_by_name(QueueName='my_queue')
 s3 = boto3.resource('s3')
 bucket = s3.Bucket('mishcollins')
 obj = bucket.Object('input.csv')
 inp = obj.get()['Body'].read()
except :
 print "failed to fetch input"
#############################################################################################################



#this cralwer only works for the domian of search involving categories=men
#if there is this tag in the search query then its fine otherwise we will append it
################################################utilities to support the controller##########################################
#assimng that the crawler is on  an EC2 Instance , and it had stopped earlier at some positon in the read file,
#we will store the last position of read from the read file everytime we read into sqs
# on reinitiation from failure we will resume from that position


#########################################get the last query position from the input file##########################################
def get_inp_line():
  
   msgs =queue.receive_messages()
   pos =  int(msgs[0].body)
   return inp ,pos
   
################################################# to update the position of the reader marker in the sqs###########################
def update_reader_pos(mark):
   msgs =queue.receive_messages()
   msgs[0].delete()
   response = queue.send_messages(Entries=[{'Id': '1', 'MessageBody': str(mark) }])
    # Print out any failures
    print(response.get('Failed'))
   
   

############################################################try to read next line from the csv fine  ######################### 
def get_next_line(mark ):
     try:
       return inp[mark]
     except :
       return "EOF"
      
# simple utility to check is st is in string query   otherwise add st    
def check_for_domain(st , query):
   if st in query:
      return 1
   else :
      return 0
      
      
def save_to_db(items_list):
      
      

###############################################Main Controller that will control the inputs / scrapping / write in to DB###############################   
def  scrape_controller(domain):
   
    base_url = "http://www.hm.com/us/products/search?"
    #'''
    #gets from bucket the input file and the last position of scrapping
    inp_file,pos = get_inp_line()
    mark =0
   
    #move reader to the given position
    while mark <pos:
         mark+=1
         
    
    #fetch next line from reader
    inp_line = get_next_line(mark)
    #'''
    #inp_line = "categories=men&term=gingham shirts|type=Gingham,source=H&M"
    
    while inp_line !="EOF" :
    
            search_q , db_entry = inp_line.split('|')
            
            #to sort by new arrivals
            if not check_for_domain("Orders=newfrom_desc",search_q):
                 search_q = search_q+"&"+"Orders=newfrom_desc"
            
            #in case none of the domain
            if  not check_for_domain("categories=men",search_q)  and  not check_for_domain("categories=ladies",search_q)  and   not check_for_domain("categories=kids",search_q)  and  not heck_for_domain("categories=sale",search_q)  :
                  search_q =  domain+"&"+search_q
             incase given domain
            elif check_for_domain(domain,search_q) : 
                     print --
            #incase of no doamin
            else :
                  continue
                  
                  
            
            q_url = base_url + search_q
            print q_url
            try: 
                my_items= scrape(q_url)
                #save_to_db(my_items)
                #for item in my_items:
                   #print item 
            except :
                print ("unable to scrape from "+q_url)
                
             #get the next imput line from the input file   
            inp_line=get_next_line(mark+1)
            #update the position of reader in SQS
            update_reader_pos(mark+1)
            mark=mark+1
            #inp_line ="EOF"
            
           
scrape_controller("categories=men")        
     
                
            
            
            
            
  
        
    
    
         
    
    
    
    
         
       
     
   
   
        



