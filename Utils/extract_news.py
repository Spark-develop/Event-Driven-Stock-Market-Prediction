import datetime
from os import link
from pandas.core.frame import DataFrame
import requests
import bs4
from datetime import date
import pandas as pd
import math

def getStartTime(yr,dy,txt_month,month):
    d = date(1899,12,30)
    crr_d = date.today()
    d1 = date(yr,month,dy)
    delt1 = d - crr_d
    delt2 = d1 - crr_d
    final_delt = (delt1.days)-(delt2.days)+1
    link2 = 'https://economictimes.indiatimes.com/archivelist/year-%d,month-%d,starttime%d.cms'%(yr,month,final_delt)
    return link2

def extract_news(link2,f):
    # Extraction of data from a day
    print("extarcting %s"%link2)
    dayres = requests.get(link2)
    daysoup1 = bs4.BeautifulSoup(dayres.text, 'html.parser')
    tag = daysoup1.select('b', class_=".contentbox5")
    tag1 = daysoup1.findAll('ul', attrs={'class': 'content'})
    tag2 = tag1[1].select('li')
    tag3 = tag1[0].select('li')
    info = []
    for j in tag3:
        info.append(j.getText())
    for i in tag2:
        info.append(i.getText())
    for sent in info:
        wrds =sent.split()
        for wrdl in wrds:
            if(wrdl == 'Microsoft' or wrdl=='MSFT' or wrdl=='Bill Gates' or wrdl=='Redmond' or wrdl == 'Xbox360' or wrdl == 'Xbox' or wrdl=='msn' or wrdl == 'Onfolio'):
                print("%s     MSFT   %s\n"%(tag[2].getText(),sent))
                f.write("%s     MSFT   %s\n"%(tag[2].getText(),sent))
            elif(wrdl == 'Apple' or wrdl=='AAPL' or wrdl=='Steve jobs' or wrdl=='ipad' or wrdl == 'iphone' or wrdl == 'i-phone' or wrdl=='iwatch' or wrdl == 'i-watch' and wrdl != 'helipad' ):
                print("%s     AAPL   %s\n"%(tag[2].getText(),sent))
                f.write("%s     AAPL   %s\n"%(tag[2].getText(),sent))
            elif(wrdl == 'Amazon' or wrdl=='Jeff Bezos' or wrdl== 'AMZN' or wrdl == 'Zappos' or wrdl == 'aws' or wrdl == 'woot' or wrdl=='blink home' or wrdl =='abebooks' or wrdl =='shopbop' or wrdl =='IMDB tv' or wrdl =='pillpack' or wrdl == 'zoox'):
                print("%s     AMZN   %s\n"%(tag[2].getText(),sent))
                f.write("%s     AMZN   %s\n"%(tag[2].getText(),sent))
        

# Extraction from year 2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021
TrainDateList = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
ValidDateList = [2016,2017,2018,2019,2020,2021]
TestDateList = [2020,2021]
datad = ['valid','test'] #'train',
dataf = [ValidDateList,TestDateList] #TrainDateList,
Bigmonths = ['Jan','Mar','May','Jul','Aug','Oct','Dec']
BigMonthNum = [1,3,5,7,8,10,12]
Smallmonths = ['Apr','Jun','Sep','Nov']
smallMonthsNum = [4,6,9,11]
for dty in range(len(dataf)):
    f = open("datasets/%s.txt"%datad[dty], "w",encoding="utf-8")

    for yr in range(len(dataf[dty])):
        for mon in range(len(Smallmonths)):
            for dy in range(1,31):
                link2 = getStartTime(dataf[dty][yr],dy,Smallmonths[mon],smallMonthsNum[mon])
                try:
                    extract_news(link2,f)
                except Exception:
                    print('completed!')
                    break


    for yr in range(len(dataf[dty])):
        for mon in range(len(Bigmonths)):
            for dy in range(1,32):
                link2 = getStartTime(dataf[dty][yr],dy,Bigmonths[mon],BigMonthNum[mon])
                try:
                    extract_news(link2,f)
                except Exception:
                    print('completed!')
                    break

    for yr in range(len(dataf[dty])):
        if (dataf[dty][yr] % 4) == 0:
            if (dataf[dty][yr] % 100) == 0:
                if (dataf[dty][yr] % 400) == 0:
                    for dy in range(1,30):
                        link2 = getStartTime(dataf[dty][yr],dy,'Feb',2)
                        try:
                            extract_news(link2,f)
                        except Exception:
                            print('completed!')
                            break
                else:
                    for dy in range(1,29):
                        link2 = getStartTime(dataf[dty][yr],dy,'Feb',2)
                        try:
                            extract_news(link2,f)
                        except Exception:
                            print('completed!')
                            break
            else:
                for dy in range(1,29):
                    link2 = getStartTime(dataf[dty][yr],dy,'Feb',2)
                    try:
                        extract_news(link2,f)
                    except Exception:
                        print('completed!')
                        break
        else:
            for dy in range(1,29):
                link2 = getStartTime(dataf[dty][yr],dy,'Feb',2)
                try:
                    extract_news(link2,f)
                except Exception:
                    print('completed!')
                    break
f.close()