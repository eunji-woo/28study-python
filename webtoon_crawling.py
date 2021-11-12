import os
import urllib.request
from bs4 import BeautifulSoup

opener = urllib.request.build_opener()
opener.addheaders=[('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")]
urllib.request.install_opener(opener)

os.chdir("C:\python28")
os.mkdir("겟백")
os.chdir("겟백")

web = urllib.request.urlopen('https://comic.naver.com/webtoon/list?titleId=727798')
soup = BeautifulSoup(web, 'html.parser')

webtoon_list = []
webtoon_img_list = []
webtoon = soup.findAll('td', {"class": "title"})

count = 1

for i in range(0,10):
    plus_url = webtoon[i].find('a')["href"] # 각 회차로 이동 시켜주는 링크가 있는 부분 추출
    name = webtoon[i].find('a').text # 각 회차의 제목 추출
    os.mkdir(name) # 각 회차의 제목으로 겟백 밑에 폴더 생성
    os.chdir(name) # 폴더 이동
    web2 = urllib.request.urlopen("https://comic.naver.com" + plus_url)
    soup2 = BeautifulSoup(web2, 'html.parser')
    webtoon2 = soup2.find('div', {"class": "wt_viewer"})
    webtoon_img = webtoon2.findAll('img') # 한 회차에 있는 이미지들
    for k in webtoon_img: # 한 회차에 있는 이미지들 반복문 돌며 .jsp로 저장
        urllib.request.urlretrieve(k['src'], './'+str(count)+".jpg")
        count = count + 1
    os.chdir('../')
    count = 1 # 다음 회차로 넘어가기 전 다시 count 1로 초기화

print("종료") # 모든 회차 크롤링 후 종료 메시지
