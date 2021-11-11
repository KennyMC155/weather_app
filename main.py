import requests
from bs4 import BeautifulSoup

def tempereture():
    url = 'https://ua.sinoptik.ua'
    sourse = requests.get(url)
    page = sourse.text
    soup = BeautifulSoup(page)
    temp_today = soup.find('p',{'class':'today-temp'})
    temp_today = temp_today.text
    tm = temp_today[:2]
    return(tm)

def closes_desision(a):
    if a <= 10:
        print(f"Oh, it's too cold, take some warm closes")
    else:
        print(f"It's not very cold, you can take some light closes")

print(f"Temperature today is {tempereture()}°C")
closes_desision(int(tempereture()))


