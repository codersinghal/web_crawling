import requests
from bs4 import BeautifulSoup

def college_notification_spider():
    url = "https://academics.mnnit.ac.in/"
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    #print(plainText)
    soup = BeautifulSoup(plainText)
    notificationList = []
    for link in soup.findAll('strong'):
        notification = link.string
        notificationList.append(notification)
    c = 0
    for link in soup.findAll('div', {'class': 'leftnormaltxt', 'style': 'font-size:13px;'}):
        notificationLink = link.findAll('a')
        c=c+1
        if notificationLink:
            print(c,":",notificationList[c-1])
            for i in notificationLink:
                final=str(i)
                print(url+final[9:final.find('>')-1])
        else:
            print(c, ":",notificationList[c-1])
            print("->",link.string)

college_notification_spider()
