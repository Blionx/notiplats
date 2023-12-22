from bs4 import BeautifulSoup
import lxml
import requests
import time
from mails import MailApi

oldlinks = []
count =  0
while(True):
  html_text = requests.get('https://nya.boplats.se/sok?types=1hand&area=508A8CB406FE001F00030A60&rooms=3').text
  soup = BeautifulSoup(html_text, 'lxml')
  print("SENDING " + str(count))
  should_update = True

  jobs = soup.find_all('div', class_='pure-u-1 pure-u-md-1-2')
  links = []
  for job in jobs:
    date = job.find('div', class_='pure-u-1 publ-date')
    if date.text == "Publ. idag":
      link = job.find('a', class_='search-result-link')
      links.append(link.attrs['href'])
  links.sort()
  oldlinks.sort()
  if len(links) == len(oldlinks):
     should_update = False
     for i in range(0, len(links)):
        if(links[i] != oldlinks[i]):
          should_update = True
        

  if should_update:
    oldlinks = links
    print(oldlinks)
    count+=1
    mail_api = MailApi()
    mail_api.set_bodyifo(oldlinks,count)
    mail_api.SendMail()
  else :
    print("no updated")
  time.sleep(10)

