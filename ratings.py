from bs4 import BeautifulSoup
import requests
import time
import webbrowser

mycf_url="https://codeforces.com/profile/harshitsinghal0006"
mycc_url="https://www.codechef.com/users/harshit128"
#webbrowser.open(my_url)
cfsource=requests.get(mycf_url)
ccsource=requests.get(mycc_url)
cfdetails=cfsource.text
ccdetails=ccsource.text
cfsoup = BeautifulSoup(cfdetails,"html.parser")
ccsoup = BeautifulSoup(ccdetails,"html.parser")
link = cfsoup.findAll('div', {'class': 'info'})
cfprevrating=0
ccprevrating=0
while 1 > 0:
 for div in link:
  span = div.find_all('span')
 ccrating=ccsoup.find('div',{'class': 'rating-number'}).text
 if ccprevrating!=ccrating:
  print("codechef- ",ccrating)
  ccprevrating=ccrating
 currating=span[1].string
 maxrating=span[4].string
 if cfprevrating != currating:
  print("codeforces current rating- ",currating)
  print("codeforces max rating- ",maxrating)
  cfprevrating=currating
 
  

