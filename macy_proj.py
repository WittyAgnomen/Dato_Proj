from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import itertools
import csv
from random import randint
#from bs4 import BeautifulSoup
#import urllib2


#read urls from csv...
reader = csv.reader(open('macy_item_urls_wofurn.csv', 'rb'))
products = []
for row in reader:
    products.append(row[1:])


products=list(itertools.chain(*products))
#print products[2:5]
print len(products)

where=0

driver = webdriver.Firefox()

for p in products[0:6]:
    item_info=[]
    try:
        driver.get(p) 
        time.sleep(randint(1,3))
    except:
        print 'loading problem'
        driver.get(p) 
        time.sleep(randint(3,5))
        
    #get prod name

    try: 
        item_info.append(driver.find_element_by_id('productTitle').text.encode('ascii', 'ignore'))
    except:
        item_info.append("error")

    
     #get price
    try:
        price=driver.find_element_by_id('priceInfo').text.encode('ascii', 'ignore')
        item_info.append(price)
       
    except:
       
        item_info.append('no price')
        
    #get pic url
    try:
        item_info.append(driver.find_element_by_id('mainView_1').get_attribute('src'))
    except:
        try:
            item_info.append(driver.find_element_by_class_name('productImageSection').find_element_by_tag_name('img').get_attribute('src'))

        except:
            item_info.append('no pic')
    
    #get colors available
    try:
        grab=driver.find_element_by_class_name('colors').find_element_by_class_name('colorway').find_element_by_class_name('hidden')
        item_info.append(grab.get_attribute('src'))
    except:
        item_info.append('no choices')
        
    #get prod details
    try:
        grab=driver.find_element_by_id('memberProductDetails').find_element_by_id('prdDesc')
        item_info.append(grab.text.encode('ascii', 'ignore'))
        
    except:
        item_info.append('no details')
        


    #get reviews, frustrating look at later
    rate=[]
    title=[]
    user=[]
    des=[]
    rec=[]

    try:
        driver.find_element_by_id('productReviewTab').click()
        time.sleep(1)
        reviews=driver.find_elements_by_id('BVSubmissionPopupContainer')
        for r in reviews:
            try:
                rate.append(r.find_element_by_class_name('BVRRRatingNormalImage').find_element_by_class_name('BVImgOrSprite').get_attribute('title').encode('ascii', 'ignore'))
                
            except:
                rate.append('no score')
            
            try:
                title.append(r.find_element_by_class_name('BVRRReviewTitleContainer').text.encode('ascii', 'ignore'))
                
            except:
                title.append('no title')

            try:
                user.append(r.find_element_by_class_name('BVRRNickname').text.encode('ascii', 'ignore'))
                
            except:
                user.append('no user')
                
            try:
                des.append(r.find_element_by_class_name('BVRRReviewText').text.encode('ascii', 'ignore'))
            
            except:
                des.append('no text')

            try: 
                rec.append(r.find_element_by_css_selector("[class*='BVRRValue BVRRRecommended']").text.encode('ascii', 'ignore'))

            except:
                rec.append('no rec')

        zipped=zip(rate,title,des,rec)
        res=dict(zip(user,zipped))      
        item_info.append(res)

    except:
        item_info.append('no ratings')

        

    
    # write to csv
    filenamed= 'macy_products.csv'
    writer = csv.writer(open(filenamed, 'a'))
    writer.writerow(item_info)
       

    where+=1
    print where
         
driver.close()

        
    

            
        
    
