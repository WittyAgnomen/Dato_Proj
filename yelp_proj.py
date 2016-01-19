from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Remote(command_executor='http://192.168.99.101:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME) #need for ip on instance, i think

driver = webdriver.Firefox()
driver.get("http://www.yelp.com/c/seattle/food") #yelp site
time.sleep(3)
#image = driver.get_screenshot_as_base64()
#from IPython.display import HTML
#HTML("""<img src="data:image/png;base64,{0}">""".format(image))


cats=['Bagels',	'Bakeries']#	'Beer, Wine & Spirits']
"""	'Breweries',	'Bubble Tea',	'Butcher',	'CSA',	'Candy Stores',	'Cheese Shops',	'Chocolatiers & Shops',	'Cideries',	'Coffee & Tea',	'Convenience Stores',	'Cupcakes',	'Desserts',	'Distilleries',	'Do-It-Yourself Food',	'Donuts',	'Empanadas',	'Ethnic Food',	'Ethnic Grocery',	'Farmers Market',	'Food Delivery Services',	'Food Trucks',	'Fruits & Veggies',	'Gelato',	'Grocery',	'Health Markets',	'Herbs & Spices',	'Ice Cream & Frozen Yogurt',	'Internet Cafes',	'Juice Bars & Smoothies',	'Macarons',	'Meat Shops',	'Organic Stores',	'Pasta Shops',	'Popcorn Shops',	'Pretzels',	'Seafood Markets',	'Shaved Ice',	'Specialty Food',	'Street Vendors',	'Tea Rooms',	'Wine Tasting Room',	'Wineries']"""


cat_head=[]
for cat in cats:
    cat_head.append(driver.find_element_by_link_text(cat).get_attribute('href'))

print cat_head


cat_sites={} #init empty for dict to hold links

#loop over cat_heads and return websites for each cat head in dict
j=0
for x in cat_head:
    #figure out location switch later, this next section should be robust for loop
    tes=x
    driver.get(tes)
    time.sleep(3)
    driver.find_element_by_partial_link_text("Search for more").click()
    time.sleep(3)
    
    #page 1 of what ever category; need to loop for lists
    biz = driver.find_elements_by_class_name('indexed-biz-name')
    print len(biz)

    links=[]
    for i in biz:
        time.sleep(1)
        links.append(i.find_element_by_css_selector('a').get_attribute('href'))

    print links # to test


    #for addtional pages
    addon1="/search?cflt="
    addon2="&amp;find_loc=Seattle%2C+WA%2C+USA&amp;start="

    #page 2
    num="10"
    addon1="/search?cflt="
    addon2="&amp;find_loc=Seattle%2C+WA%2C+USA&amp;start="
    test=tes+addon1+cats[j]+addon2+num
    print test
    driver.get(test)
    time.sleep(3)
    biz = driver.find_elements_by_class_name('indexed-biz-name')
    print len(biz)

    for i in biz:
        time.sleep(1)
        links.append(i.find_element_by_css_selector('a').get_attribute('href'))

    print links #to check
    print len(links)


    #page 3
    num="20"
    test=tes+addon1+cats[0]+addon2+num
    print test
    driver.get(test)
    time.sleep(3)
    biz = driver.find_elements_by_class_name('indexed-biz-name')
    print len(biz)

    for i in biz:
        time.sleep(1)
        links.append(i.find_element_by_css_selector('a').get_attribute('href'))

    print links #to check
    print len(links)

    #page 4
    num="30"
    test=tes+addon1+cats[0]+addon2+num
    print test
    driver.get(test)
    time.sleep(3)
    biz = driver.find_elements_by_class_name('indexed-biz-name')
    print len(biz)

    for i in biz:
        time.sleep(1)
        links.append(i.find_element_by_css_selector('a').get_attribute('href'))

    print links #to check
    print len(links)
    
    cat_sites[cats[j]]=links
    j+=1
        

print cat_sites #to test dict store

#get data from a single page


"""biz = {}
for section in sections:
    section.click()
    time.sleep(1)
    content = best.find_element_by_class_name('main-content')
    sec_name = content.text.split('\n')[0]
    biz_names = content.find_elements_by_class_name('biz-name')
    biz_names = [name.text for name in biz_names if name.text]
    biz[sec_name] = biz_names"""



driver.close()


#elem = driver.find_element_by_name("q")
##content = driver.find_element_by_class_name('regular-search-result')
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
##assert "No results found." not in driver.page_source
##driver.close()

##print contentbiz
