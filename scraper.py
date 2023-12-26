from bs4 import BeautifulSoup
import lxml
import requests

class Scrapper:
    url:str
    oldlinks:list
    should_update:bool

    def __init__(self, url):
        self.url = url
        self.oldlinks = []
        self.should_update = False

    def get_html(self) ->str:
        return  requests.get(self.url).text
    
    def ShouldUpdate(self)-> bool:
        
        return self.should_update
    
    def get_information(self):
        html_text = self.get_html()
        soup = BeautifulSoup(html_text, 'lxml')
        self.should_update = True
        jobs = soup.find_all('div', class_='pure-u-1 pure-u-md-1-2')
        links = []
        for job in jobs:
            date = job.find('div', class_='pure-u-1 publ-date')
            if date.text == "Publ. idag":
                link = job.find('a', class_='search-result-link')
                links.append(link.attrs['href'])

        links.sort()
        self.oldlinks.sort()

        if len(links) == len(self.oldlinks):
            self.should_update = False
            for i in range(0, len(links)):
                if(links[i] != self.oldlinks[i]):
                    self.should_update = True

        if self.should_update:
            self.oldlinks = links

    def get_message(self):
        return self.oldlinks