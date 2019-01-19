'''
This is a code to:
Write a selenium script to login using Facebook on eventful.com.
After login, it should redirect to dashboard page.

Internshala internship assignment from Ercess Incorporation.

Requirements: Python 3.x.x, Selenium, Geckodriver, Firefox

Platform: Windows
'''
#import webdriver, keys(to emulate keyboard) and time(for sleep)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#asking for facebook username and password
fbuser=input("Enter your FaceBook Username: ")
fbpass=input("Enter your FaceBook Password: ")

#starting up Firefox with geckodriver
browser=webdriver.Firefox()

#going to sign-in url and waiting for 2 seconds
browser.get("https://eventful.com/signin")
time.sleep(2)

#find facebook signin option, click and wait for 2 seconds
browser.find_element_by_xpath("//*[@id='facebook-login']").click()
time.sleep(2)

#switch to new window
browser.switch_to.window(browser.window_handles[1])

#input facebook usename, password and click login
browser.find_element_by_xpath("//*[@id='email']").send_keys(fbuser)
browser.find_element_by_xpath("//*[@id='pass']").send_keys(fbpass)
browser.find_element_by_xpath("//*[@id='u_0_0']").click()

#switch to previous window and wait for 2 seconds
browser.switch_to.window(browser.window_handles[0])
time.sleep(2)

#find the usename
findname=browser.find_element_by_xpath("//*[@id='user-panel-username']")

#use the username and go to the dashboard
str="https://eventful.com/users/{}/events".format(findname.text)
browser.get(str)