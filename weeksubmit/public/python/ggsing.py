# -*- encoding: utf-8 -*-
#/고고싱홈페이지에서 봄 룩을 이미지 다운로드 받기 위해(해당 날씨에 맞는 옷을
# 이미지 다운로드받기 위해)
import os, re
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as parse
import sys
import json
import requests

#title = sys.argv[1]
#content= sys.argv[2]
#query_data = sys.argv[3]
#sender=sys.argv[4]
#password=sys.argv[5]
#json_results = json.loads(query_data)

#기본 url을 해놓고 쿼리문자가 없이 이루어진 홈페이지라서 base_url == url이다
#즉, parse가 필요없다(위의 import한 모듈)
base_url="https://www.ggsing.com/product/%ED%94%84%EB%A6%AC%ED%83%84%ED%83%84-%EC%A1%B0%EA%B1%B0%ED%8C%AC%EC%B8%A0-%ED%97%88%EB%A6%AC%EB%B0%B4%EB%94%A9%EA%B8%B0%EC%9E%A5%EB%B3%84%EB%AC%B4%EB%A3%8C%EB%B0%B0%EC%86%A1/56983/category/2455/display/1/"
#url로 접속이 가능한지 콘솔창에서 바로 접속해보려고
#print를 시켜본다
url = base_url
#print(url)

#html파일을 다운로드받아서 저장한다
savename="c:/Users/raspk/Documents/dev/webprog02/week6sub38/weeksubmit/public/html/ggssing_detail.html"
#print(savename)
#디렉터리는 이미 만들어놨기 때문에 해당명령을 쓰지않고 바로 파일을 다운
if not os.path.exists(savename):
   #파일 다운로드(urlretrieve)
    req.urlretrieve(url, savename)
    #print("success_ggsinghtmldownload")

with open(savename, "r", encoding="utf-8") as fp:
    #다운받은 html파일을 html파서로(lxml은 에러가 날때가 있어서) 파싱하고
    soup = BeautifulSoup(fp, "html.parser")
    print("parsing success")

###
#파싱한 것에서 원하는 태그인 이미지 부분만 가져온다
#정규식 작성: 위의 파싱한 결과인 soup를 출력해보면
# <re.Match object; span=(0,11), match='/index.html'이란 부분이 img태그
# 아랫줄에 잇는데, 거기서 /index.html이란 글자에 해당하는 것을 정규식으로
# 하기 위해서 re.compile을 이용해서 정규식을 만들건데
# /는 a태그의 /에 해당하는 url형태의 /이고 [.]은 .에 해당하고 글자는 그 글자 그대로 적혀있는 패턴만 찾는다
#/product/list.html로 a 태그가 시작하는 img태그를 모두 가져온다
#regex_a = re.compile('^/product/list.html')
###

#그리고나서 search나 find나 match메서드로 패턴에 맞는 것을 찾아낸다
#a 태그가 저 패턴과 일치하는 경우의 img태그이 src만을 불러온다
#matchedobj_a = regex_a.match(a_list.attrs['img'])
#cond={"href":matchedobj_a.group(0)}
#list_img =soup.find_all("a", cond)
#divSelector = soup.find_all('div', class_='origin')
#print(divSelector)

#divSelector=soup.find_all('div', {"id": "product_detail"})
divSelector = soup.find(id='product_detail')
#divSelector = soup.find('div', {"class:": "quick_menubg"})
#divSelector = soup.find_all('div')


#print("type(regex_a)=>{}".format(type(regex_a)))
#aList = soup.find_all(['a'])
#matched_a_List=[]
#for i in aList:
#    matchedobj_a = regex_a.match(i.attrs['href'])
#    #print(matchedobj_a)
#    matched_a_List.append(matchedobj_a)
#for i in matched_a_List:
#    #i.find_parents()
#    parents = i.find_parents()
#    for parent in parents:
#        print(parent.name)
#for i in range(len(aSelector)):
#    print(i)

#print(sys.argv)
#divSelector = soup.find_all("div", {"class": "origin"})
#print(divSelector)
#for i in divSelector:
#    print(i)

#regex_img = re.compile('//www[.]ggsing[.]com/web/kimseh9/ksh210414a[0-9]{1}_[0-9]{2}[.]jpg$')
regex_img = re.compile('^https...www.ggsing.com.web.kimseh9.ksh210414a([0-9_]{2})')#/ksh210414a[0-9]{1}_
#regex_img = re.compile('^/yeook/event/pants1st_2050sale_pc[.]jpg$')
#regex_img= re.compile('^//www[.]ggsing[.]com/web')
imgList = divSelector.find_all("img")
#print(len(imgList))#21
#for i in imgList:
#    print(i)
#this is for static_page.html button onclick method where to link to
#button(not related to this python file)
srcList=[]


matched_img_List=[]
matchedobj_img=""
for i in imgList:
    try:
        matchedobj_img = regex_img.match(i.attrs['ec-data-src'])
        #print(len(matched_img_List))
        tmp = str(matchedobj_img)
        #print(tmp)
        if tmp!= 'None':
            matched_img_List.append(i.attrs['ec-data-src'])
            print(i.attrs['ec-data-src'])
            #this is for static_page.html button onclick method where to link to
            #button(not related to this python file)
            srcList.append(i.attrs['ec-data-src'])

    except KeyError:
        pass
#this is for static_page.html button onclick method where to link to
#button(not related to this python file)
f_srcList_path = 'c:/Users/username/pathTofolder/public/pathTxt/srcList.txt'
dirname_srcList = os.path.dirname(f_srcList_path)
if not os.path.exists(dirname_srcList):
    os.makedirs(dirname_srcList)
f_srcList = open(f_srcList_path, "w")
for i in range(len(srcList)):
    f_srcList.write(srcList[i]+"\n")
f_srcList.close()


###for i in matched_img_List:
    ###print(i)
#list_img = divSelector.find('img')

#해당 div태그(부모) 아래의 모든 자식을 선택(find_all)
#list_imgImage=[]
#list_img = divSelector.find_all("img")
#for imgImage in list_img:
#    try:#src속성을 가져와서 리스트(list_img)에 넣어주자
#        #list_a.appned(regex_img.match(list_a.attrs['href'])
#        a = imgImage.attrs['src']
#        #I will comment this for a moment for test
#        #print(matchedobj_a)
##        tmp= matchedobj_a.find_all(["img"])
##        list_img.append(tmp)
#    except KeyError:
#        pass
#    print(a)
#    list_imgImage.append(imgImage.attrs['src'])
#print(list_imgImage)
#sample_list = [v for v in list_img if v]
#print(sample_list)
#for i in list_img:
#    if i:    print(i)
#print(list_img)

#i will comment this for just a moment for test
##print(list_img)

#해당되는 a의 href의 뒤쪽 태그에 img태그가 있는데 그 이미지를 src속성으로 가져온다
#list_imgImage=[]
#for i in list_a:
#    tmp = soup.find_all("img")
#    print(tmp)
#print(list_imgImage)
#list_src = []
#for image in list_imgImage:
#    try:
#        a = image.attrs['src']
#        list_src.append(image.attrs['src'])
#    except KeyError:
#        pass
#    print(a)
#print(list_src)#아무것도 안 들어왔는데에,



#    for i in range(len(list_imgImage)):
#        savename="c:/Users/username/pathTofolder/public/images/GogosingImg/gogosingimg"+str(i)+".png"
#        print(savename)
#        dirname = os.path.dirname(savename)
#        if not os.path.exists(dirname):
#            os.makedirs(dirname)
#        base_url = "https:"
#        base_url+=list_src[i]
#        req.urlretrieve(url, savename)

for i in range(len(matched_img_List)):#there are no None Image!
    savename = "c:/Users/raspk/pathTofolder/public/images/GogosingImg_detail/gogosing"+str(i)+".png"
    print(savename)
    dirname = os.path.dirname(savename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    try:
        tmp = str(matched_img_List[i])
    except TypeError:
        tmp = 0
    target_url = tmp
    print(target_url)
    print(savename)

    #savename_ = 'c:/Users/username/pathTofolder/public/binaryimages/GogosingBinImg/gogosingimg/1.png'
    #because I checked succeeded image(which is urlretrieve succeeded) is only one.
    #dirname_=os.path.dirname(savename_)
    if not os.path.exists(savename):
        try:
            req.urlretrieve(target_url, savename)
            print("success!"+savename)
        except ValueError:
            pass
        #res = requests.get(url)#이제는 url이 무엇인지 알게 되었으므로 정확하므로
        ##url로 바이너리 파일형식으로 다운로드 받는다
        #with open(savename_, "wb") as fp:
        #    fp.write(res)
        #    print("store complete! of "+savename+"as "+savename_)
        #data = res.decode("euc_kr")

#    savename = "c:/Users/username/pathTofolder/public/images/GogosingImg/gogosing"+str(i)+".png"
#    print(savename)
#    dirname = os.path.dirname(savename)
#    #if not os.path.exists(dirname):
#    #    os.makedirs(dirname)
#    #url = "https://www.ggsing.com/"
#    print("type(i의 타입)=>{}".format(type(matched_img_List[i])))
#    #url+= matched_img_List[i]
#    #if not os.path.exists(savename):
#    #    req.urlretrieve(url, savename)
#    #req.urlretrieve(base_url, savename)