# Importing Selenium for ATC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Address information

category = "t-shirts"
name = "John Done"
email = "123testpy@gmail.com"
telephone = "4154923458"
address_1 = "123 Main St"
address_2 = ""
zip_code = "94124"
City = "San Francisco"
State = "CA"
Card_number = "4266567890123456"
month = "04"
year = "2025"
CVV = "359"

# auto checkout
driver.get("https://www.supremenewyork.com/shop/t-shirts/pd75fskci/cwduzct1g")

driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(name)
driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(telephone)
driver.find_element_by_xpath('//*[@id="bo"]').send_keys(address_1)
driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(zip_code)
driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(City)
driver.find_element_by_xpath('//*[@id="state_label"]')
driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys("4266567890123456")
driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys("03")
driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys("2025")
driver.find_element_by_xpath('//*[@id="orcer"]').send_keys("395")
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="pay"]/input').click()




































