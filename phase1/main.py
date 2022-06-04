from concurrent.futures import thread
from selenium import webdriver
from threading import Thread
import time
import string
import random
import pandas as pd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


NUM_THREAD = 5
url = "https://www.refinitiv.com/en/sustainable-finance/esg-scores"
path = "/home/hojjat/Desktop/personal/DataColab Task/project/chromedriver"


refinitiv_data = {
    'name': [],
    'ESG_score': [],
    'rank': [],
    'environment': [],
    'social': [],
    'governance': [],
    'company_ticker': [],
}

all_words = []

def getData(search_word):

    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    driver = webdriver.Chrome(path, desired_capabilities=desired_capabilities)

    driver.get(url)
    driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

    try:
        driver.find_element_by_xpath('//*[@id="searchInput-1"]').send_keys(search_word)

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="searchInput-1-typeaheadItem-0"]/button').click()
        time.sleep(1)

        ESG_score = driver.find_element_by_xpath('//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/h3/strong').text

        rank = driver.find_element_by_xpath('//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[2]/div[3]/h4').text

        env = driver.find_element_by_xpath('//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text

        social = driver.find_element_by_xpath('//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[5]/div[2]').text

        
        gov = driver.find_element_by_xpath('//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[10]/div[2]').text
 
        name = driver.find_element_by_xpath('//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[2]/div[2]/p/strong').text
        
        logs = str(driver.get_log("performance"))


        temp = logs[logs.find("ricCode="):]
        ticker =  temp[:temp.find('"')]
        # AZK.MC"},"requestId":"150813.217
        if name not in refinitiv_data['name']:
            refinitiv_data['company_ticker'].append(ticker.replace("ricCode=",""))
            refinitiv_data['ESG_score'].append(ESG_score)
            refinitiv_data['rank'].append(rank)
            refinitiv_data['environment'].append(env)
            refinitiv_data['social'].append(social)
            refinitiv_data['governance'].append(gov)
            refinitiv_data['name'].append(name)
    except:
        print("Words not found.")


def getLetters():
    one = random.choice(string.ascii_letters).lower()
    two = random.choice(string.ascii_letters).lower()

    if one == two:
        two = random.choice(string.ascii_letters).lower()
    
    if (one+two) in all_words:
        one = random.choice(string.ascii_letters).lower()
        two = random.choice(string.ascii_letters).lower()
        if one == two:
            two = random.choice(string.ascii_letters).lower()
    
    all_words.append(one+two)
    return one+two
    

threads = []

for i in range(0,30):
    for j in range(0, NUM_THREAD):
        letters = getLetters()
        print(letters)
        t = Thread(target=getData, args=(letters,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    time.sleep(2)
    print(f"Sleeping...Wait... times: {i}")

print(refinitiv_data)

frame = pd.DataFrame(refinitiv_data)
frame.to_csv("dataCompanies.csv")