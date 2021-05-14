#抓gradate原始碼
import urllib.request as req
url="https://www.ptt.cc/bbs/graduate/index.html"
#建request物件，附加headers
request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    })

data=req.urlopen(request).read().decode("utf-8")


import bs4 

root=bs4.BeautifulSoup(data, "html.parser")#data=html的原始碼
titles=root.find_all("div",class_="title") #找class ="title"的div標籤，find all=找全部
for title in titles:
    if title.a !=None:#如果標題包含a印出來
        print(title.a.string)