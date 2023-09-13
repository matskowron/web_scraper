'''
SKOWRON Mateusz | Web Scraper app
Github @matskowron 

September 2023
'''

import jsonlines
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

PROXY = 'customer-scrapingdojo-cc-us-sessid-0870241768-sesstime-10:vdU232Kc!FQacCq@pr.oxylabs.io:7777'
INPUT_URL = 'http://quotes.toscrape.com/js-delayed/'
OUTPUT_FILE = 'output.jsonl'

class Scrapper:

    def scrapper(self):
            driver = webdriver.Chrome()
            
            with jsonlines.open(OUTPUT_FILE, mode='w') as writer:
                
                for page in range(1, 11):
                    url = INPUT_URL + f'page/{page}/' + '?=' + PROXY 
                    print(f"Scraping page {page}...")
                    driver.get(url)

                    initial_text = driver.find_element(By.ID, "quotesPlaceholder").text

                    def check_text_changed(driver):
                        new_text = driver.find_element(By.ID, "quotesPlaceholder").text
                        return new_text != initial_text

                    wait = WebDriverWait(driver, 100)
                    wait.until(check_text_changed)

                    quote_divs = driver.find_elements(By.CLASS_NAME, "quote")

                    for quote_div in quote_divs:
                        text = quote_div.find_element(By.CLASS_NAME, "text").text
                        author = quote_div.find_element(By.CLASS_NAME, "author").text
                        tags_elements = quote_div.find_elements(By.CLASS_NAME, "tag")
                        tags = [tag.text for tag in tags_elements]

                        data = {
                            "text": text,
                            "by": author,
                            "tags": tags
                        }
                        writer.write(data)
            
            driver.quit()