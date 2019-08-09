from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

urls = []

url = 'file:///Users/jason.bang/Desktop/data.html'
req = uReq(url)
page_html = req.read()
page_soup = BeautifulSoup(page_html, "lxml")

a = (page_soup.prettify(formatter="html"))
a = ((a.replace("&lt;", "<")).replace("&gt;", ">"))


def find_url(x):
    ssplit = a.split()
    for x in ssplit:
        if x.startswith('<url>'):
            x = x.replace("<url>", "").replace("</url>", "").replace("<![CDATA[", "").replace("]]>", "").replace("<!--", "").replace("-->", "")
            urls.append(x)
        elif x.startswith('<!--url>'):
            urls.append("")


find_url(a)

for x in urls:
    if len(x) <= 8:
        urls.remove(x)

for a in urls:
    print(a)

