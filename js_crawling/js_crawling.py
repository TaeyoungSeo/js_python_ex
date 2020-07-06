from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.xi.co.kr/subscription/list")
bsObject = BeautifulSoup(html, "html.parser")

items = bsObject.select(".subscript_list > li")

for item in items:
    print("==============================")
    print(item.find("h4", {"class" : "tit"}).text)
    dls = item.find_all("dl")
    for dl in dls:
        print(dl.find("dt").text + " : " + dl.find("dd").text)
