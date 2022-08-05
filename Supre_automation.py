# Importing Selenium for ATC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.headless = True
driver = webdriver.Chrome('chromedriver path here', chrome_options=options)

# Address information

category = "t-shirts"
name = "first_last"
email = "email_here"
telephone = "phone number"
address_1 = "address here"
address_2 = ""
zip_code = "zipcode here"
City = "city_name"
State = "state name (XX)"
card_number = "card number (xxxx_xxxx_xxxx_xxxx)"
month = "(xx)"
year = "(xxxx)"
cvv = "(xxx) or (xxxx)"

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
driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(card_number)
driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(month)
driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(year)
driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(cvv)
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="pay"]/input').click()

