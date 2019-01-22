'''
This is a GitHub login automation.
Why? Coz I'm lazy
'''
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user=input("Enter GitHub Username: ")
password=getpass.getpass("Enter GitHub password: ")
print("Opening GitHub... Please Wait")
browser=webdriver.Firefox()
browser.get("https://github.com/login")
browser.find_element_by_xpath("//*[@id='login_field']").send_keys(user)
browser.find_element_by_xpath("//*[@id='password']").send_keys(password)
browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[3]").click()
url="https://github.com/{}?tab=repositories".format(user)
browser.get(url)