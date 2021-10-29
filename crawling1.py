import urllib.request
from bs4 import BeautifulSoup

web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')

print("학과                    홈페이지")

for i in range(0,5):
    #학과 이름 크롤링
    department_name = soup.findAll('ul', {"class":"col_list0"})
    department_name_list = department_name[i].findAll('a')

    #학과 홈페이지 크롤링
    for p in department_name_list:
        print("{:20}".format(p.text), end='')
        # print(p["href"])
        web2 = urllib.request.urlopen("http://www.swu.ac.kr" + p["href"])
        soup2 = BeautifulSoup(web2, 'html.parser')

        if soup2.find('a', {"class":"btn btn_xl btn_blue_gray"}) and soup2.find('a', {"class":"btn btn_xl btn_blue_gray"}).text.replace(" ","") == "홈페이지바로가기":
            department_url = soup2.find('a', {"class":"btn btn_xl btn_blue_gray"})['href']
        else:
            department_url = "홈페이지가 없습니다."
        print(department_url)




