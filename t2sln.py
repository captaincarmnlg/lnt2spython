#description: this is text to speach for novel website's
import time
import os
import mysql.connector
import argparse
import webln
parser = argparse.ArgumentParser()
parser.add_argument('series',help="add series url part",type=str)
parser.add_argument("--list","-ls", help="display list yes or no",action="store_true")
parser.add_argument("--item","-i",type=int,help="-i or --item + integer of the list nr")
parser.add_argument("--minitem","-mi",type=int,help="-i or --item + integer of the list nr")
parser.add_argument("--maxitem","-xi",type=int,help="-i or --item + integer of the list nr")
parser.add_argument("-all",help="-all ",action="store_true")
args = parser.parse_args()
series = ""#make it last called via sql(optional)
upcount=0
def gettxt(name,isfile=False):
    if isfile == True:
        if name !='':
            f = open(name,"r",encoding="utf-8" )
            txt = f.read() 
            f.close()
            del f
            return txt
        else:
           return name    
def t2s(txt,name):
    query = 'cmd /c "python texttospeach.py {} --name {} --text {}"'
    os.system(query.format(series,name.replace(" ","_"),txt.replace(" ","_")))
class filemanager():
    def __init__(self):
        self.quetxt = []
        self.quemp3 = []
        self.novelweb = webln
        self.lenlist = 0
    #def getseries webcrawler
    def getlist(self,series,show = False):
        i=0
        self.elmt = self.novelweb.listln(series)
        self.lenlist = len(self.elmt)
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

        print(self.elmt[self.arrplace].get_attribute("alink"))
        self.ln = self.novelweb.scrape(self.elmt[self.arrplace].get_attribute("alink"),series)
        time.sleep(2)
        #self.novelweb.destroy()
    
    def downloadmp3(self):      
        if "txt/"+series+"/"+self.ln+".txt" !='':
            t2s("txt/"+series+"/"+self.ln+".txt",self.ln)
            pass
    def quelisttxt(self,series,show = False):
        i=0
        self.elmt = self.novelweb.listln(series)
        self.lenlist = len(self.elmt)
        for x in reversed(self.elmt):
            self.quetxt.append(x.get_attribute("alink"))
            if show:
                indexlistformat = "{}.  {}"
                print(indexlistformat.format(i,x.text))  
                print(self.quetxt[i])
                i+=1
                pass
            pass
    def downloadtxtfull(self):
        for x in self.quetxt:
            y = self.novelweb.scrape(x,series)
            print(y)
            self.quemp3.append(y)
            pass
        print(len(self.quemp3))
    def downloadmp3full(self):
        directory = "txt/"+series
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = "txt/"+series+"/"+filename
                print(filename.replace(".txt",""))
                t2s(filepath,filename.replace(".txt",""))
                continue
            else:
                continue
        
    def destroyremaints(self):
        self.novelweb.quit()
        pass


debug = filemanager()
series = args.series
#list
if args.list:
    debug.getlist(series,args.list)
    debug.destroyremaints()
    pass

#item
if args.item and args.all!=True:
    debug.getlist(series)
    debug.setup(args.item)
    debug.downloadtxt()
    debug.downloadmp3()
    debug.destroyremaints()
    pass
#all

if args.all:
    if args.minitem or args.maxitem:
        debug.getlist(series)
        print(debug.lenlist)
        try:
            os.rmdir("speach/"+series)
            pass
        except OSError as error:
            print(error) 
            pass
        if args.minitem:
            ia = args.minitem
            pass
        else:
            ia = 0
            pass
    
        debug.destroyremaints()
        for e in reversed(debug.elmt):
            time.sleep(1)
            if args.maxitem:
                maxitem = args.maxitem
                pass
            else:
                maxitem = debug.lenlist+1
                pass
        
            if ia >= debug.lenlist or ia >= maxitem:
                break
            else:
                query = 'cmd /c "python t2sln.py {} -i  {}"'
                print(query.format(series,ia))
                time.sleep(5.5)
                os.system(query.format(series,ia))
                time.sleep(1)
                ia += 1
                pass
            pass
        pass
    else:
        debug.quelisttxt(series,True)
        debug.downloadtxtfull()
        time.sleep(1)
        debug.destroyremaints()
        debug.downloadmp3full()
        pass
    pass
#create a comandline interface class
#get list of a novel an select one or one with the comandline