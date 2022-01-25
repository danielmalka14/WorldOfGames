import sys
import time
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scores_service():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
    chrome_driver.get("http://172.18.0.4:80")
    score = chrome_driver.find_element(By.CLASS_NAME, 'scores').text
    score_int = int(score)
    if score_int in range(0, 1000):
        test_results = True
        return test_results
    else:
        test_results = False
        return test_results

def main_function():
    test_results = test_scores_service()
    if test_results == True:
        return sys.exit(0)
    elif test_results == False:
        return sys.exit(1)

main_function()