import requests
from bs4 import BeautifulSoup

url = 'https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/'


def temperature():
    sourse = requests.get(url)
    page = sourse.text
    feaures = "html.parser"
    soup = BeautifulSoup(page, feaures)
    today_temp = soup.find('div', {'class': 'city__main-temp'})
    today_temp = today_temp.text
    tt = today_temp[:2]
    return tt


def real_temp():
    sourse = requests.get(url)
    page = sourse.text
    feaures = "html.parser"
    soup = BeautifulSoup(page, feaures)
    real_temperature = soup.find('span', {'class': 'city__main-feels-like'})
    real_temperature = real_temperature.text
    rt = real_temperature[73:75]
    return rt


def closes_desision(a, b):
    if a <= 0 or b <= 0:
        print(f"Oh, it's too cold, take some warm closes")
    elif a >= 10 or b >= 10:
        print(f"It's warm enough to take some lite closes")
    else:
        print(f"It's quite cold, you can take some medium closes")


print(f"Temperature today is {temperature()}°C")
print(f"But fell's like {real_temp()}°C")
closes_desision(int(temperature()), int(real_temp()))
