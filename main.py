from bs4 import BeautifulSoup
import lxml
import requests
import time

html_text = requests.get('https://nya.boplats.se/sok?types=1hand&area=508A8CB406FE001F00030A60&rooms=3').text
soup = BeautifulSoup(html_text, 'lxml')
oldlinks = []
while(True):
  jobs = soup.find_all('div', class_='pure-u-1 pure-u-md-1-2')
  links = []
  for job in jobs:
    date = job.find('div', class_='pure-u-1 publ-date')
    if date.text == "Publ. idag":
      link = job.find('a', class_='search-result-link')
      links.append(link.attrs['href'])
  if oldlinks != links:
    oldlinks = links
    print(oldlinks)
  else :
    print("not send")
  time.sleep(3)

