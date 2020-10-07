import requests
from bs4 import BeautifulSoup

x = input("Image : ")
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(x)
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


# with open("images.html", "w", encoding="utf8") as f :
#     f.write(soup.prettify()) # html문서를 예쁘게

images = soup.find_all("img", attrs={"class":"_img"})
# print(images)


for idx, image in enumerate(images):
       print(image["data-source"])