#description: this is text to speach for novel website's
import time
import cfscrape
import nltk
from selenium import webdriver 
from gtts import gTTS
import os
from pydub import AudioSegment
series = ""#make it last called via sql(optional)
upcount=0

class novelwebsite():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get("https://novelplanet.com")
        self.driver.minimize_window()
        time.sleep(5)
    def listln(self,listuri):
        self.driver.get("https://novelplanet.com/Novel/"+listuri+"/")
        time.sleep(2)
        closebtn = self.driver.find_element_by_class_name("cmpboxbtnno")
        closebtn.click()
        elmt = self.driver.find_elements_by_class_name("rowChapter")
        
        return elmt    
    
    def gotoitem(self,elmt):
        
        time.sleep(2)
        elmt.click()
    def scrape(self):
        time.sleep(1)
        title = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/h4').text
        txt = title
        txt += " "
        txt += self.driver.find_element_by_id("divReadContent").text
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
        return title
    def destroy(self):
        self.driver.quit()
    def create(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
class t2s():
    def __init__(self,lang="en",slow=False,txt=""):
        self.lang = lang
        self.slow = slow
        self.txt = txt
    def loadstring(self,name,isfile=False):
        if isfile == True:
            if name !='':
                f = open(name,"r",encoding="utf-8" )
                self.txt = f.read() 
                f.close()
        else:
            self.txt = name
                
            pass          
    def t2s(self,name):
        try:
            os.mkdir("speach/"+series)
            pass
        except OSError:
            pass   
        loc = "speach/{}/{}.mp3"
        location =  loc.format(series,name)
        myobj = gTTS(text=self.txt, lang=self.lang, slow=self.slow)
        myobj.save(location)
        print(name+"succes")
        time.sleep(3)
class filemanager():
    def __init__(self):
        self.novelweb = novelwebsite()
        self.t2s = t2s()
    #def getseries webcrawler
    def getlist(self,series,show = True):
        i=0
        self.elmt = self.novelweb.listln(series)
        if show:
            for x in reversed(self.elmt):
                indexlistformat = "{}.  {}"
                print(indexlistformat.format(i,x.text))
                i+=1
    def setup(self,upcount):
        self.arrplace = len(self.elmt)-upcount-1
        #print(len(self.elmt))
    def downloadtxt(self):
        print(self.elmt[self.arrplace].text)
        self.novelweb.gotoitem(self.elmt[self.arrplace])
        self.ln = self.novelweb.scrape()
        time.sleep(2)
        #self.novelweb.destroy()
        self.novelweb.driver.quit()
    def downloadmp3(self):      
        if "txt/"+series+"/"+self.ln+".txt" !='':
            f = open("txt/"+series+"/"+self.ln+".txt","r",encoding="utf-8" )
            txt = f.read() 
            f.close()
            print(len(txt))
            self.t2s.loadstring(txt)
            self.t2s.t2s(self.ln)
            pass



debug = filemanager()
series = input("input series:")
yn  = input("show listY/N: ")
if yn == "Y":
    tf = True
    pass
else:
    tf = False
    pass
debug.getlist(series,tf)
upcount = int(input("input nr of list above:"))
debug.setup(upcount)
debug.downloadtxt()

debug.downloadmp3()






#create a comandline interface class
#get list of a novel an select one or one with the comandline






    