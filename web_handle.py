# -*- coding:utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import platform

class HandleWeb:

    options = Options()

    def init_web_page(self, url, WebBrowser):
        if(platform.system() == "Windows"):
            chromDriver = "C:\chromedriver.exe"  # Windows
        elif(platform.system() == "Darwin"):
            chromDriver = '/Users/ksoh/PycharmProjects/chromedriver' # MAC
        else:
            # chromDriver = '/Users/ksoh/PycharmProjects/chromedriver' # MAC
            chromDriver = 'chromedriver'  # Docker
            self.options.add_argument('disable-gpu')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('headless')

        driver = webdriver.Chrome(executable_path=chromDriver, options=self.options)
        driver.set_window_size(1440, 960)
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(5)

        try:
            # Login 동작 수행
            userID = driver.find_element_by_xpath('//*[@id="sc-login-form"]/div/div[1]/div/input')
            userID.send_keys('humax')
            time.sleep(1)

            userPW = driver.find_element_by_xpath('//*[@id="sc-login-form"]/div/div[2]/div/input')
            userPW.send_keys('humax@!')
            time.sleep(1)

            sign_in = driver.find_element_by_xpath('//*[@id="sc-login-form"]/div/div[3]/a')
            sign_in.click()
            time.sleep(2)

            #driver.find_elements_
        except:
            print("error or already login completed")

        WebBrowser.append(driver)
        return True

    def web_find_element(selfself, WebBrowser, element):
        html = WebBrowser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        td = soup.find(element)
        print(td.get_text())
        return td.get_text()

    def web_find_point(selfself, WebBrowser, element):
        html = WebBrowser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        td = soup.find('span', {'class': element})
        print(td.get_text())
        return td.get_text()

    def webdriver_shutdown(self, WebBrowser):
        driver = WebBrowser[0]
        driver.close()
        driver.quit()

"""    def get_web_page(self, url, WebBrowser):
        driver = WebBrowser[0]
        driver.set_window_size(1440, 960)
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(5)
        WebBrowser.append(driver)
        return True"""

handleweb = HandleWeb()