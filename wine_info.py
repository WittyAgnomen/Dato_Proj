from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import itertools
import csv
from random import randint

#read in wine page urls


reader = csv.reader(open('wine_urls.csv', 'rb'))
wines = []
for row in reader:
    wines.append(row[0:])


wines=list(itertools.chain(*wines))
print len(wines)


driver = webdriver.Firefox()

#loop through
for w in wines:
    winefo=[]
    try:
        driver.get(w) #change to dynamic later
        time.sleep(randint(1,2))
    except:
        print 'loading problem'
        driver.get(w) #change to dynamic later
        time.sleep(randint(3,5))
        
    #get prod name

    try: 
        winefo.append(driver.find_element_by_class_name('productAbstract').find_element_by_tag_name('h1').text.encode('ascii', 'ignore'))
    except:
        try:
            winefo.append(driver.find_element_by_class_name('productAbstract').text.encode('ascii', 'ignore'))
        except:
            winefo.append("error")


    
     #get price
    try:
        winefo.append(driver.find_element_by_class_name('regularPrice').text.encode('ascii', 'ignore'))
    except:
        winefo.append("no price")

    try:
        winefo.append(driver.find_element_by_class_name('salesPrice').text.encode('ascii', 'ignore'))
    except:
        winefo.append("no sales price")


    #get pic url
    try:
        winefo.append(driver.find_element_by_css_selector("[class*='hero label']").get_attribute('src'))
    except:
        winefo.append('no pic')
    

    #get about wine/product
    try:
        driver.find_element_by_class_name('viewAll').click()
        time.sleep(1)
    except:
        print "no view all"
    try:
        winefo.append(driver.find_element_by_css_selector("[class*='tabContent aboutTheWine active']").text.encode('ascii', 'ignore'))
    except:
        winefo.append("error")

    #get winery info
    try:
        driver.find_element_by_css_selector("[class*='tab theWinery']").click()
    except:
        print "no winery tab"
    try:
        winefo.append(driver.find_element_by_class_name('winery').text.encode('ascii', 'ignore'))
    except:
        winefo.append('no text about winery or n/a')
    try:
        winefo.append(driver.find_element_by_class_name('winery-map').get_attribute('data-map-geo').encode('ascii', 'ignore'))
    except:
        winefo.append('no loc info')
        
    

    #get reviews
    names=[]
    stars=[]
    revs=[]
    try:
        driver.find_element_by_css_selector("[class*='tab reviews']").click()
    except:
        print "no reviews tab"
    try:
        revers=driver.find_element_by_class_name('topReviews').find_elements_by_class_name('review')
        print len(revers) #test
        
        for r in revers:
            try:
                names.append(r.find_element_by_class_name('reviewAuthorAlias').text.encode('ascii', 'ignore'))
            except:
                names.append('no name')
            try:
                stars.append(r.find_element_by_xpath('.//span[@class = "starRatingText"]').get_attribute('innerHTML').encode('ascii', 'ignore'))
            except:
                stars.append('n/a')
            try:
                revs.append(r.find_element_by_class_name('reviewText').text.encode('ascii', 'ignore'))
            except:
                revs.append('no rev')
    
        zipped=zip(revs,stars)
        reviews=dict(zip(names,zipped))
    
        

    except:
        reviews='no reviews'
                
    winefo.append(reviews)

    print reviews
    
    # write to csv
    filenamed= 'wines.csv'
    writer = csv.writer(open(filenamed, 'a'))
    writer.writerow(winefo)
    



   



