import csv
import urllib.request as req
import urllib
import os,re
from bs4 import BeautifulSoup

base_url = "https://www.weather.go.kr/weather/forecast/timeseries.jsp"
url = base_url
savename = "c:/Users/username/pathTofolder/public/html/forecast.html"
dirname = os.path.dirname(savename)

if not os.path.exists(dirname):
    os.makedirs(dirname)
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print('success downloadinghtml!')

res = req.urlopen(url).read()
with open(savename, "wb") as fp:
    fp.write(res)
    print('success stores bin')
data = res.decode("euc_kr")

f = open(savename, "r", encoding="euc_kr")
soup = BeautifulSoup(f, "html.parser")
f.close()
degList=[]
humList=[]
degSelector = soup.find('tr', {'class': 'degree'}).find_all('td')
humSelector = soup.find('tr', {'class': 'humidity'}).find_all('td')
for i in range(len(degSelector)):
    try:
        a = soup.select("tr.degree > td > p.plus")[i].string
        b = soup.select("tr.humidity > td > p.content")[i].string
    except KeyError:
        pass
    print("temp:"+a)
    degList.append(a)
    print("humi:"+b)
    humList.append(b)
print(degList)
print(humList)
filepath = "c:/Users/username/pathTofolder/public/txt/makeCsv.txt"
dirname = os.path.dirname(filepath)
if not os.path.exists(dirname):
    os.makedirs(dirname)
fp = open(filepath, "w")
for i in range(len(degList)):
    fp.write(degList[i]+"\n")
    fp.write(humList[i]+"\n")
fp.close()
f.close()
