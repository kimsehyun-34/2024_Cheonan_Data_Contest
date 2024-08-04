from selenium import webdriver
import inspect, os, platform, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def bot():
    options = webdriver.ChromeOptions()

    current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))

    if platform.system() == 'Windows':
        driver_path = os.path.join(current_folder, 'chromedriver.exe')
    else:
        driver_path = os.path.join(current_folder, '..\chromedriver.exe')

    driver = webdriver.Chrome(driver_path, options=options)
    driver.implicitly_wait(10)

    ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/1855282597/review/visitor?reviewItem=0')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 수제빵 연구소.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/17297107/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041510')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,11):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 듀팡과자.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
        
     #이동
    driver.get('https://pcmap.place.naver.com/restaurant/37640731/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041557')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 몽상가인.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/1113169485/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041558')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,11):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 옛날호두과자 본점.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     #이동
    driver.get('https://pcmap.place.naver.com/restaurant/17297121/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041559')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,20):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 꼬망스케잌.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/20496063/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041600')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,45):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 쁘띠빠리.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/1453498511/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041602')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 슈에뜨 베이커리.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/33489623/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041604')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 뚜쥬루돌가마.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/36263119/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041605')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 못난이 꽈배기 본점.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/17236015/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041606')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,15):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 시바앙과자.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/11674512/review/visitor?entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202408041613')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,15):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 호도원호두과자.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     #이동
    driver.get('https://pcmap.place.naver.com/restaurant/34473955/review/visitor?entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202408041615')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 못난이 꽈배기 본점.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     #이동
    driver.get('https://pcmap.place.naver.com/restaurant/36263119/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041605')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 할머니학화호도과자 본점.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/1107998835/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041616')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,20):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 파스텔베이커리.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/17258000/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041617')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,20):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 천안당 호두과자 남천안점.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/1281260605/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041619')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 지씨브레드.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/1781484182/review/visitor?entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202408041619')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,50):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 브레드보드.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
            
     ##이동
    driver.get('https://pcmap.place.naver.com/restaurant/801795893/review/visitor?additionalHeight=76&from=map&fromPanelNum=1&timestamp=202408041621')
    print('로그인중....')
    time.sleep(3)
    
    for i in range(1,20):
        btn = driver.find_element("xpath", '/html/body/div[3]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')
        btn.click()
        time.sleep(2)

    news_titles = driver.find_elements(By.CLASS_NAME, "zPfVt")
    
    for i in news_titles:
        title = i.text
        title=title+"\n\n\n"
        print(title)

        with open("천안 엘림베이커리.txt", "a", encoding='utf-8') as f: #txt추가
            data = title
            f.write(data)
        
            
    print('모든 작업 완료')
    driver.quit()

bot()
os.system('pause')