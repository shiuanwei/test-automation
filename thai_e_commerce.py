# Selenium Setup and Test
#Test Case Variables
PATH = "/usr/local/bin/chromedriver"
URL ="https://www.powerbuy.co.th/th"
SEARCH="TV"
EXPECTEDCART="2"
SKU1="264098"
SKU2="258784"
#SKU3="dummysku"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(PATH)
action = webdriver.ActionChains(driver)

#Launch Browser and Navigate to Page
driver.get(URL)
#driver.maximize_window()
print("1. Launch "+ URL + " Webpage - Pass")

#Search Item
search = driver.find_element_by_id("txt-searchBox-input")
search.send_keys(SEARCH)
search.send_keys(Keys.RETURN)
print("2. Search " + SEARCH + " Content - Pass")

#Filter for 44-55 inch
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="layout"]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div[30]/div[2]/div/div/div[1]/div[1]/div').click()
print("3. Filter - Pass")

#Select Product and Add to Cart
time.sleep(3)
driver.find_element_by_xpath('//*[@id="lnk-viewProduct-'+ SKU1 +'-name"]').click()
print("4. Selecting " + SKU1 + " - Pass")
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="btn-addCart-'+ SKU1 +'"]').click()
print("5. Add " + SKU1 + " to Cart - Pass")

#Navigate on breadcrumb
time.sleep(3)
#homepage = driver.find_element_by_xpath('//*[@id="lnk-viewHome"]').click()
#layer2breadcrumb
driver.find_element_by_xpath('//*[@id="lnk-viewBreadcrumb-2"]').click()
print("6. Navigate on Breadcrumb - Pass")
#currentlayerbreadcrumb = driver.find_element_by_xpath('//*[@id="lnk-viewBreadcrumb-currentProduct"]').click()

#Filter for 32-43 inch
driver.implicitly_wait(10)
driver.execute_script("window.scrollBy(0,2000)","")
driver.find_element_by_xpath('//*[@id="layout"]/div[2]/div[3]/div[3]/div/div[3]/div[1]/div/div/div/div/div[8]/div[2]/div/div/div[2]/div[1]/div').click()
print("7. Filter - Pass")

#Select Product and Add to Cart
time.sleep(3)
driver.find_element_by_xpath('//*[@id="lnk-viewProduct-'+ SKU2 +'-name"]').click()
print("8. Selecting " + SKU2 + " - Pass")
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="btn-addCart-'+ SKU2 +'"]').click()
print("9. Add " + SKU2 + " to Cart - Pass")

#Navigate to Cart
driver.find_element_by_xpath('//*[@id="btn-openMiniCart"]/div').click()
print("10. Go to Cart - Pass")


#Validate Cart Count
time.sleep(3)
minicartcount = driver.find_element_by_xpath("//*[@id='btn-openMiniCart']/div/span").text
headercartcount = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/h1/span[1]/span").text    #xpath of header cart count
cartlist = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/div[3]/div/div[1]/div[2]").text     #xpath of cart list
time.sleep(3)
cartlistcount=str(cartlist.count("SKU:"))

print("\n\n---CART VALIDATION---")
print("Total " + cartlistcount + " items in cart list")

if cartlistcount == EXPECTEDCART:
    print("Cart List Count Correct")
else:
    print("Cart List Count INCORRECT")

if minicartcount == EXPECTEDCART:
    print ("Cart Button Count correct")
else:
    print("Cart Button Count INCORRECT")

if headercartcount == EXPECTEDCART:
    print ("Cart Header count correct")
else:
    print ("Cart Header count INCORRECT")


#Validate Cart Item
cartitem = [SKU1,SKU2]
for sku in cartitem:
    try:
        cartlist.index(sku)
    except ValueError:
          print(""+ sku +" NOT FOUND in Cart List")

time.sleep(3)
print("Test Run - End")
#driver.quit()
