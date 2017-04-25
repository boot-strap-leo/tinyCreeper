#coding=utf-8
#python version 2.7
#author: bootstrap

import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS

def crawl(page, word, baseUrl='http://www.baidu.com/s'):
    #baseUrl = 'http://www.baidu.com/s'
    #page = 1
    #word = 'vergin'

    data = {'wd':word,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
    data = urllib.urlencode(data)
    url = baseUrl+'?'+data

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    except urllib2.HttpError,e:
        print e.code
        exit(0)
    except urllib2.URLError,e:
        print e.reason
        exit(0)

    html = response.read()
    soup = BS(html)
    return soup


def dealResult(text, href, time, soup, printFlag):
    td = soup.find_all(class_='f')

    for item in td:
        text.append(item.h3.a.get_text())
        href.append(item.h3.a['href'])
        if printFlag:
            print item.h3.a.get_text()
            print item.h3.a['href']

        realtime = item.find_all('div',attrs={'class':'realtime'})
        if realtime:
            realtime_str = realtime[0].get_text()
        else:
            realtime_str = "no_specific_time"
        time.append(realtime_str)
        if printFlag:
            print realtime_str + "\n"

        #uin = raw_input("continue?Y/N (default yes):\n")
        #if uin == "N" or uin == "n" or uin == "no" or uin == "No":
        #    return
    return

def printResult(result_name, result):
    print "\n" + result_name
    for item in result:
        print item

def getResult(word, pageMax, printFlag=False):
    text = []
    href = []
    time = []
    for page in range(1, pageMax+1):
        soup = crawl(page, word)
        dealResult(text, href, time, soup, printFlag)
    print "Everything works fine, begin to print result:"
    printResult("text", text)
    printResult("href", href)
    printResult("time", time)
    return text, href, time


getResult("Synereo", 2, True)
