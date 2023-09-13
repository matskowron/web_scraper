'''
SKOWRON Mateusz | Web Scraper app
Github @matskowron 

September 2023
'''

from WebScrapping.web_scraper import *

class UI:
    
    def run(self):
        print("\nSKOWRON Mateusz for Sigmoidal\nGithub @matskowron\nJuly 2023\n")
        
        web_scrapper = Scrapper()
        web_scrapper.scrapper()
        print(f" Scraping finished! Check the output.jsonl file\n")