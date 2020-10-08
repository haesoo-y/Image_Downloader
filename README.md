# Image_Downloader

### 목적
- 이미지를 입력받아 네이버에서 이미지 20장 다운로드

### 주요기능
1. 원하는 이미지를 입력받을 수 있음
2. 네이버에서 크롤링하여 20장이 jpg파일로 다운로드됨
3. 파일명은 입력받은 이미지명과 숫자를 순서대로 출력함.

### 미리보기
![Image_Downloader](https://user-images.githubusercontent.com/71266602/95449626-00563880-09a0-11eb-99a2-1ecf6d2a2fde.png)


이미지를 검색하여 20장 다운로드

### 상세내용
```python
import requests
from bs4 import BeautifulSoup
```
BeautifulSoup 를 임포트하여 웹스크래핑
```python
       with open("image_{}_{}.jpg".format(x, idx + 1), "wb") as f:
              f.write(image_res.content)
```
input값으로 받은 x값과 enmuerate로 증가하는 idx를 이미지 파일명으로 입력함




