import requests
from bs4 import BeautifulSoup
import smtplib
from decimal import Decimal
import time

URL = 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=MIS&bolum=MANAGEMENT+INFORMATION+SYSTEMS#'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

def price_checker():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    
    code = soup.find('tr', class_='schtd2').get_text()
    print(code)

    # name = soup.find('span', class_='pt_v8').get_text()
    # # print(price)

    # days = soup.find('span', class_='pt_v8').get_text()
   
    # hours = soup.find('span', class_='pt_v8').get_text() 
    
    
'''
    converted_price = Decimal(price)
    # print(converted_price)
    
    if(converted_price < 12.000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("yusufcoskun2003@gmail.com", "dbxnxblutlwseywn")
    
    subject = 'PRICE DROPPED!'
    body = "Price drop:" + URL
    msg = "Subject:" +subject+'\n\n'+body
    
    server.sendmail("yusufcoskun2003@gmail.com","yusufcstudy@gmail.com",msg)
    
    print("Email has been sent")
    
    server.quit()
'''
    
while (True):
    price_checker()
    time.sleep(60*60*6)