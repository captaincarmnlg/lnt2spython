import time
from selenium import webdriver 
import os
driver = webdriver.Chrome()#'./chromedriver.exe'
driver.get("https://novelplanet.com")
while True:
    trys=0
    time.sleep(7)
    try:
        closebtn = driver.find_element_by_class_name("cmpboxbtnno")
        pass
    except :
        print("fail")
        trys += 1
        if trys == 20:
            driver.refresh()
            pass
        pass
        if trys >30:
            if len(driver.find_element_by_class_name("cmpboxbtnno")) != 0:
                break 
            pass
    else:
        time.sleep(1)
        closebtn.click()
        break   
def listln(listuri):
    driver.get("https://novelplanet.com/Novel/"+listuri+"/")
    time.sleep(2)
    if driver.find_elements_by_class_name("rowChapter"):
        elmt = driver.find_elements_by_class_name("rowChapter") 
        pass
      
    return elmt   
def scrape(elmt,series):
    driver.get("https://novelplanet.com"+elmt)
    time.sleep(18)
    title = driver.find_element_by_xpath('//*[@id="main"]/div[3]/h4').text.replace(":"," ")
    txt = title
    txt += " "
    txt += driver.find_element_by_id("divReadContent").text
    b = "()「」"
    for char in b:
        txt = txt.replace(char,"")
    c ="…"
    for char in c:
        txt = txt.replace(char,"...")
    txt.strip()
    try:
        os.mkdir("txt/"+series)
        pass
    except OSError:
        pass
    ftxt = open("txt/"+series+"/"+title+".txt","w",encoding="utf-8" )
    ftxt.write(txt+"end of"+title)
    ftxt.close()
    del ftxt
    return title
def quit():
    driver.quit()
