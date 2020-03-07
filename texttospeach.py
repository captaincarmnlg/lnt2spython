from gtts import gTTS
import argparse
import time
import os
parser = argparse.ArgumentParser()
parser.add_argument('series',help="add series url part",type=str)
parser.add_argument("--name","-n",type=str,help="-i or --item + integer of the list nr")
parser.add_argument("--text","-t",type=str,help="-i or --item + integer of the list nr")
args = parser.parse_args()

name = args.name.replace("_"," ")
series = args.series
filepath = args.text.replace("_"," ")
f = open(filepath,"r",encoding="utf-8")
txt = f.read()
try:
    os.mkdir("speach/"+series)
    pass        
except OSError:
    pass   
loc = "speach/{}/{}.mp3"
location =  loc.format(series,name)
myobj = gTTS(txt)
try:
    myobj.save(location)
    pass
except:
    print("exeption")
    pass
        
print(name+": succes")
time.sleep(1)
txt=""
del myobj                    
pass