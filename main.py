
import requests
import re
import time
import json
from bs4 import BeautifulSoup
import urllib
from random import getrandbits
from threading import Thread
from Queue import Queue
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
import threading
threadLock = threading.Lock()
proxies = False

requests.packages.urllib3.disable_warnings()

def load_proxies(filename):
    proxies = []
    with open(filename) as fh:
        for line in fh:
            line = line.strip()
            data = line.split(":")
            proxies.append(data)
    return proxies
if proxies:
    proxies = load_proxies("")
    print "Loaded: {} proxies".format(len(proxies))
else:
    print "Not using proxies!!"
class Presto(object):
    counter = 1
    s = requests.Session()
    url = "https://docs.google.com/forms/d/e/1FAIpQLSdhFkAfM1VGDvbp0f3ETi-DaNRTswB7IgIC9uoWbECCd7sI6g/viewform"
    posturl = "https://docs.google.com/forms/d/e/1FAIpQLSdhFkAfM1VGDvbp0f3ETi-DaNRTswB7IgIC9uoWbECCd7sI6g/formResponse"


    postheaders = {
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "X-Client-Data": "CJG2yQEIorbJAQjEtskBCKmdygEI153KAQioo8oB",
        "X-Chrome-Connected": "id=113292259032357480973,mode=0,enable_account_consistency=false",
        "Referer": "https://docs.google.com/forms/d/e/1FAIpQLSdhFkAfM1VGDvbp0f3ETi-DaNRTswB7IgIC9uoWbECCd7sI6g/viewform?fbzx=-7523426717494581000",
        "Accept-Encoding": "gzip, deflate, br1",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        }

    def loopThrough(self):
        print "\n"
        print "Made by https://twitter.com/thebotsmith - follow for free scripts every week!!"
        print "\n"

        time.sleep(5)
        x = 100#TODO change amount of entries per thread
        if proxies:
            r = self.s.get(self.url,headers=self.headers1,verify=False,proxies=proxies)
        else:
            r = self.s.get(self.url,headers=self.headers1,verify=False)
        for i in range(x):
            email = 'maxbanes101+{}@gmail.com'.format(getrandbits(40)),#TODO change all these!!
            try:
                data = {
                    "emailAddress":email,
                    "entry.1884265043":"your name",
                    "entry.1938400468":"your second name",
                    "entry.1450673532_year":"1990",
                    "entry.1450673532_month":"9",
                    "entry.1450673532_day":"20",
                    "entry.71493440":"1 WEST road",
                    "entry.1981412943":"gl80 bms",
                    "entry.950259558":"london",
                    "entry.1622497152":"United Kingdom",
                    "entry.1850033056":"078874747400",
                    "entry.769447175":"myinsta",#TODO instagram username (must be publioc)
                    "entry.256744251_sentinel":"",
                    "entry.256744251":"Autorizzo il trattamento dei miei dati personali, ai sensi del D.lgs. 196 del 30 giugno 2003",
                    "entry.715796591":"10", #TODO size in us format
                    "fvv":"1",
                    "draftResponse":'[null,null,"-7523426717494581264"]',
                    "pageHistory":"0",
                    "fbzx":"-7523426717494581264"
                    }
                if proxies:
                    r = self.s.post(self.posturl,headers=self.postheaders,verify=False,data=data,proxies=proxies)
                else:
                    r = self.s.post(self.posturl,headers=self.postheaders,verify=False,data=data)

                if "Thank you for subscribing" in r.text:
                    print "entered sccessfully"
                    self.counter += 1
                    self.s.cookies.clear()
                    with open ("enteredaccounts.txt","a") as f:
                        f.write(email + "\n")
                else:
                    print "failed to enter."
            except Exception as e:
                print(e)
    def run(self):
            self.loopThrough()
            print(Fore.GREEN + "** {} FINISHED WORK CLOSING THREAD **".format(threading.current_thread().name))

bots = []

for i in range(25):#TODO amount of threads
    bot=Presto()
    bots.append(bot)

threads = []
count = 1
for bot in bots:
    print(Fore.YELLOW +" ** bot {} started **".format(count))
    time.sleep(1)
    t = Thread(target=bot.run)
    threads.append(t)
    count += 1
    t.start()

for t in threads:
    t.join()
