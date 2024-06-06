from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo
import datetime
import uuid
import requests
import json
from config import MONGO_URI, TWITTER_USERNAME, TWITTER_PASSWORD, PROXY

# MongoDB setup
client = pymongo.MongoClient(MONGO_URI)
db = client['twitter_trends']
collection = db['trends']

# ProxyMesh setup
options = Options()
options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')

# Selenium setup
driver = webdriver.Chrome(options=options)

def login_to_twitter(username, password):
    driver.get('https://twitter.com/login')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'session[username_or_email]')))
    driver.find_element(By.NAME, 'session[username_or_email]').send_keys(username)
    driver.find_element(By.NAME, 'session[password]').send_keys(password)
    driver.find_element(By.NAME, 'session[password]').send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]')))

def get_trending_topics():
    driver.get('https://twitter.com/home')
    trends = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]//span')))
    top_trends = [trend.text for trend in trends[:5]]
    return top_trends

def get_ip_address():
    response = requests.get("http://ipinfo.io/json")
    ip_data = response.json()
    return ip_data['ip']

def save_to_mongodb(trends, ip_address):
    unique_id = str(uuid.uuid4())
    timestamp = datetime.datetime.now()
    data = {
        '_id': unique_id,
        'trend1': trends[0] if len(trends) > 0 else None,
        'trend2': trends[1] if len(trends) > 1 else None,
        'trend3': trends[2] if len(trends) > 2 else None,
        'trend4': trends[3] if len(trends) > 3 else None,
        'trend5': trends[4] if len(trends) > 4 else None,
        'timestamp': timestamp,
        'ip_address': ip_address
    }
    collection.insert_one(data)
    return data

def main():
    try:
        login_to_twitter(TWITTER_USERNAME, TWITTER_PASSWORD)
        trends = get_trending_topics()
        ip_address = get_ip_address()
        result = save_to_mongodb(trends, ip_address)
        driver.quit()
        return json.dumps(result, default=str)
    except Exception as e:
        driver.quit()
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    result = main()
    print(result)
