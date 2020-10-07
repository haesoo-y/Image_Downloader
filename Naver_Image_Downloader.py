import requests
from bs4 import BeautifulSoup

x = input("Image : ")
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(x)
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


images = soup.find_all("img", attrs={"class":"_img"})

for idx, image in enumerate(images):
       image_url = image["data-source"]
       image_res = requests.get(image_url)
       image_res.raise_for_status()
       with open("image_{}_{}.jpg".format(x, idx + 1), "wb") as f:
              f.write(image_res.content)

       if idx >= 19:  # 상위 20개 이미지까지만 다운로드
              break
print("저장 완료")