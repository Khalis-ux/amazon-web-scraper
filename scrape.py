from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


proxies = [
    # Use working proxies or the script won't work
    'http://proxy1:port',
    'http://proxy2:port',
    'http://proxy3:port',
]

user_agents = [
    # You can change the user agents
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36',
]

def set_driver(proxy, user_agent):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--incognito')
    options.add_argument('--proxy-server=%s' % proxy)
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=options)

    return driver

def amazon_scraper():
    for _ in range(3):
        # Accessing to the url
        url = input('Insert url: ')
        proxy = random.choice(proxies)
        driver = set_driver(proxy, user_agents)
        driver.get(url)
        driver.implicitly_wait(5)

        try:
            # Reject cookies
            reject_button = driver.find_element(By.ID, "sp-cc-rejectall-link")
            reject_button.click()
            driver.implicitly_wait(5)
        except NoSuchElementException:
            # Localize element if the page reloads
            print('')

        try:
            el =driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-none aok-align-center aok-relative']//span[@class='a-price-whole']")
            elt = el.text
            print('Product Available')
            
        except NoSuchElementException:
            # If the element is not found, then the product is not available
            print('Product Not Available')

        driver.quit()

amazon_scraper()
