from selenium import webdriver
import time

path = "C:\chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://zzzscore.com/1to50/")

for i in range(1, 51): # 1~50 반복문
    buttons = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]') # 모든 버튼을 xpath를 이용해 가져온다
    for btn in buttons: # 가져온 모든 버튼을 반복문 돌면서
        if btn.text == str(i): # 버튼의 번호와 count 변수의 값이 같으면
            btn.click() # 버튼 클릭
            break

time.sleep(1000)
