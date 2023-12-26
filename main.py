
import time
from mails import MailApi
from scraper import Scrapper
from decouple import config
#from mailformater import Formater

oldlinks = []
count =  0
new_scrapper = Scrapper(config('SEARCHURL'))
while(True):
  print("SENDING " + str(count))
  new_scrapper.get_information()
  if new_scrapper.ShouldUpdate():
    count+=1
    info = new_scrapper.get_message()
    print(info)
    #mesage = Formater.format(info)
    mail_api = MailApi()
    mail_api.set_bodyifo(info,count)
    mail_api.SendMail()
  
  time.sleep(3)

