from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

score_results = False

def test_scores_service():
    chrome_driver = webdriver.Chrome(executable_path=r"/home/daniel/Downloads/chromedriver_linux64/chromedriver")
    chrome_driver.get("http://10.0.2.15:5000/")
    score = chrome_driver.f
    print(score)

    if score in range(0, 1000):
        score_results = True


def main_function():
    test_scores_service()
    if score_results == True:
        print("the test completed successfully.")
    elif score_results == False:
        print("the test failed.")

main_function()
