import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service():
    chrome_driver = webdriver.Chrome(executable_path=r"/home/daniel/Downloads/chromedriver_linux64/chromedriver")
    chrome_driver.get("http://10.0.2.15:5000/")
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