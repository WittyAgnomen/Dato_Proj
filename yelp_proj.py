from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Remote(command_executor='http://192.168.99.101:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME) #need for ip on instance, i think

driver = webdriver.Firefox()
driver.get("http://www.yelp.com/c/seattle/food") #yelp site
time.sleep(3)

"""
cat_head=[]
cate=driver.find_element_by_css_selector("[class*='arrange arrange--12 arrange--wrap arrange--6-units']")
cate1=cate.find_elements_by_css_selector("[class*='ylist']")
for i in cate1:
    cate2=i.find_elements_by_css_selector('a')
    for j in cate2:
        cat_head.append(j.get_attribute('href'))
    
print cat_head

cats=[]
for i in cat_head:
    cats.append(i.rsplit('/',1)[1])

print cats



cat_sites={} #init empty for dict to hold links

#loop over cat_heads and return websites for each cat head in dict
j=0
for x in cat_head[0:2]:
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
"""


#get data from a single page
driver.get("http://www.yelp.com/biz/blazing-bagels-seattle") #change to dynamic later
time.sleep(3)

"""
#grab comp data
info=[]
info.append(driver.find_element_by_class_name('biz-page-header-left').find_element_by_tag_name('h1').text)
info.append(driver.find_element_by_class_name('rating-very-large').find_element_by_tag_name('i').get_attribute('title'))
info.append(driver.find_element_by_class_name('address').text)
info.append(driver.find_element_by_class_name('biz-phone').text)
info.append(driver.find_element_by_class_name('biz-website').find_element_by_tag_name('a').text)
info.append(driver.find_element_by_css_selector("[class*='nowrap price-description']").text)
#info.append(driver.find_element_by_class_name('ywidget').find_elements_by_tag_name('li').text) #more business info

print info
"""

#grab reviews

cur_page=1


peeps=[]
rates=[]
revs=[]

can=driver.find_element_by_css_selector("[class*='page-of-pages arrange_unit arrange_unit--fill']").text
cant=int(can[-1:]) #a counter for loopiing through review pages

while cur_page<=cant:
    peep=driver.find_elements_by_class_name('user-passport-info')
    for i in peep:
        peeps.append(i.text)

    rev=driver.find_elements_by_class_name('review-content')
    for i in rev:
        rates.append(i.find_element_by_class_name('rating-very-large').find_element_by_tag_name('i').get_attribute('title'))
        revs.append(i.find_element_by_tag_name('p').text) 

    print len(rates)

    if cur_page<cant:
        driver.find_element_by_css_selector("[class*='page-option prev-next next']").click()
        time.sleep(2)
        cur_page+=1
    else:
        cur_page+=1

print len(peeps)
print len(rates)
print len(revs)
print rates


#still add dictionary add

"""   
reviews=dict(zip(peeps,revs))
print reviews
"""

"""
#grab pic urls
driver.find_element_by_css_selector("[class*='see-more show-all-overlay']").click()
time.sleep(2)
driver.find_element_by_css_selector("[class*='biz-shim js-lightbox-media-link']").click()
time.sleep(2)

count=driver.find_element_by_css_selector("[class*='tab-link js-tab-link tab-link--nav js-tab-link--nav is-selected']").get_attribute('data-media-count')
count=int(count)
url={}
while count>19:
    abc=driver.find_element_by_css_selector("[class*='photo-box-img']").get_attribute('src')
    edf=driver.find_element_by_css_selector("[class*='caption selected-photo-caption-text ytype']").text

    print count
    print abc
    print edf

    driver.find_element_by_css_selector("[class*='i ig-common i-nav-arrow-right-common']").click()
    time.sleep(2)
    url.update({edf:abc})
    count-=1
    
print url
"""
#need to think about storage, possibbly writing as functions

driver.close()


