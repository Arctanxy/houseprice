from lxml import html
import pandas as pd
from selenium import webdriver
import multiprocessing
import threading
import pymysql
from sqlachemy import creat_engine



def get_info(page):
    tree = html.fromstring(page)
    saleprice = tree.xpath('//div[@class="trl-item sty1"]/i/text()')
    firstpay = tree.xpath('//div[@class="trl-item"]/text()')
    housetype = tree.xpath('//div[@class="trl-item1"]/div/text()')
    houseestate = tree.xpath('//div[@class="rcont"]/a/text()')
    address = tree.xpath('//div[@id="address"]/a/text()')
    otherinfo = tree.xpath('//div[@class="cont clearfix qu_bianqu1"]/div/span/text()')
    return saleprice,firstpay,housetype,houseestate,address,otherinfo

def clawler(district,start,end):
    driver = webdriver.PhantomJS('/home/ka/bin/phantomjs-1.9.7-linux-x86_64/bin/phantomjs')
    saleprices = []
    firstpays = []
    housetypes = []
    houseestates = []
    addresss = []
    otherinfos = []
    for j in district[start:end]:
        driver.get(j)
        page=driver.page_source
        saleprice,firstpay,housetype,houseestate,address,otherinfo = get_info(page)
        saleprices.append(saleprice)
        firstpays.append(firstpay)
        housetypes.append(housetype)
        houseestates.append(houseestate)
        addresss.append(address)
        otherinfos.append(otherinfo)
        print(jingkai.index(j))
    df= pd.DataFrame({
            'saleprice':saleprices,
            'firstpay':firstpays,
            'housetype':housetypes,
            'houseestate':houseestates,
            'address':addresss,
            'otherinfo':otherinfos
        })
    engine = creat_engine('mysql+pymysql://root:@127.0.0.1:3306/estates?charset="utf-8"')
    df.to_sql('estates_info',con=engine,index=False,if_exists='append')
    return df

def multithread(district):
    threads = []
    for index in range(4):
        one_thread = threading.Thread(target=clawler,args=(district,len(district)*index/4,len(district)*(i+1)/4))
        threads.append(one_thread)
        print('threads %r started' % index)

    for thread in threads:
        thread.start()

    for j in threads:
        j.join()


def multiprocess(district_list):
    processes = []
    for district in district_list:
        each_process = multiprocessing.Process(target=multithread,args=(district))
        processes.append(each_process)
        print('process %r started' % district_list.index(district))

    for one_process in processes:
        one_process.start()

    for j in processes:
        j.join()


if __name__ == '__main__':
    luyang = pd.read_csv('~/Downloads/Luyang_fangtianxia_houselink.csv')
    xinzhan = pd.read_csv('~/Downloads/Xinzhan_fangtianxia_houselink.csv')
    jingkai = pd.read_csv('~/Downloads/Jingkai_fangtianxia_houselink.csv')
    jingkai = ['http://esf.hf.fang.com'+j for j in list(jingkai['House_links'])]
    xinzhan = ['http://esf.hf.fang.com'+j for j in list(xinzhan['House_links'])]
    luyang = ['http://esf.hf.fang.com'+j for j in list(luyang['House_links'])]
    district_list = [jingkai,luyang,xinzhan]
    multiprocess(district_list=district_list)
