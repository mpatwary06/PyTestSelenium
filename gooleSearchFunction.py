from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class BrowserInteractions():


    def test(self):
        baseUrl = ("https://www.nfl.com")

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get(baseUrl)
        driver.implicitly_wait(10)

        title = driver.title

        print("Title of the web page is: " + title)



        currentUrl = driver.current_url
        print("Current url of the web pagee is: " + currentUrl)

        driver.refresh()
        print("Browser Refreshed 1st time")


        driver.get(driver.current_url)
        print("Browser refreshed the 2nd time")

        driver.get("https://www.google.com")

        currentUrl = driver.current_url
        print("Current url of the web pagee is: " + currentUrl)


        driver.back()
        print("Browser Back")

        currentUrl = driver.current_url
        print("Current url of the web pagee is: " + currentUrl)

        driver.forward()
        print("Browser Forward")

        currentUrl = driver.current_url
        print("Current url of the web pagee is: " + currentUrl)

        pageSource = driver.page_source

        time.sleep(3)

        #driver.close()

        driver.close()

ff = BrowserInteractions()
ff.test()





