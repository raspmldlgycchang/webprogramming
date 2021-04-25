import os#디렉터리 없을 때 쓰려고 하는 os.mkdirs도 쓰려고
import urllib.request as req
from bs4 import BeautifulSoup
import urllib
import re

url="https://www.weather.go.kr/weather/forecast/timeseries.jsp"
hdr={'User-Agent':'Mozilla/5.0'}

savename="../html/forecast.html"
#그림저장
savename_part="../html/forecaststate.png"
dirname=os.path.dirname(savename)

#디렉터리가 없다면 만들고
if not os.path.exists(dirname):
    os.makedirs(dirname)
#파일이 없다면 다운
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

###
# filename, mode, encoding: 사용할 변수들 아래에서 소개
# 파싱:url로 먼저 다운로드한 파일을(filename) 바이너리로 읽어서(mode) encoding
# 타입으로 data에 저장한다
###
res = req.urlopen(url).read()
with open(savename, "wb") as fp:
    fp.write(res)
    print("저장완료")
data = res.decode("euc_kr")

#soup에 파싱한 결과 저장
f = open(savename, "r", encoding="euc_kr")
soup = BeautifulSoup(f, "html.parser")

#html파일을 find등의 메서드를 이용해 css 선택자로 원하는 결과 가졍괴
#이거를 바로 정적페이지에 js랑 html,css이용해서 원하는 정적페이지 만들기
