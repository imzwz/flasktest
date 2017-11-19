# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
path = "http://sc.chinaz.com/tupian/"
urlpre="rentiyishu_"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"}
#headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,     like Gec    ko) Chrome/50.0.2661.86"}
cookies = {"SUB":"_2A253C9_GDeThGeBO41MV-SnOyzWIHXVU9-GOrDV6PUJbktAKLXPQkW0bP81-DJOpRtZ_EQfHvEhrGAgaHg..", "_T_WM":"4cf6995c969bbc6014318d68fcf2f55d", "SCF":"Ao7zgvhWf6yewEBq7gC4fesKQQafgCrFtDaVLVmAFMwe_HTZyZ6JATXY2N_wBEeMq6iBDyl0NbRuD2K1JPLWR2E"}
#cookies = {"SUB":"_2A251NafqDeTxGeNK6FUQ9C3Owz2IHXVW2cmirDV6PUJbkdANLVWnkW1by7ov4XTE97HZ33Ji3dkAcDc9Cg..", "_T_WM":"fbd3382d8afbd98ee941a00deaf3ae98", "gsid_CTandWM":"4uBG67281dy2LKzQmZwfLmOrR4x"}
proxies = {'http':'http://127.0.0.1:8087'}

def imagedown(imageurl):
    name = imageurl.split("/")[-1]
    imgpath = "data/"+name
    imgrep = requests.get(imageurl,headers=headers)
    chunk_size=512 #设置chunk大小
    with open(imgpath, 'wb') as fd:
        for chunk in imgrep.iter_content(chunk_size):
            fd.write(chunk)

def get_comments(comment_url, headers, cookies):
    r=requests.get(comment_url,headers=headers,cookies=cookies)
    soup = BeautifulSoup(r.content, 'lxml')
    for tag in soup.find_all(id="M_"):
        weibo_content = tag
    for tag in soup.find_all('a', string = re.compile(u'查看更多热门')):
        hot_url = tag['href']
        get_hot_comments(hot_url, headers, cookies)

def get_hot_comments(hot_url, headers, cookies):
    url_prefix = "https://weibo.cn"
    hot_comment_url = url_prefix + hot_url
    r=requests.get(hot_comment_url,headers=headers,cookies=cookies)
    soup = BeautifulSoup(r.content, 'lxml')
    for tag in soup.find_all(class_="ctt"):
        print(tag)

    
for i in range(2,3):
#    url = path+urlpre+str(i)+".html"
    #url = "http://weibo.cn/kaifulee"
    url = "https://weibo.cn/search/mblog/?keyword=%E5%88%98%E5%BC%BA%E4%B8%9C%E5%9B%9E%E5%BA%94%E4%B8%8D%E7%9F%A5%E5%A6%BB%E7%BE%8E&sort=hot"
    print(url)
#    r=requests.get(url,headers=headers,proxies=proxies)
    r=requests.get(url,headers=headers,cookies=cookies)
    soup = BeautifulSoup(r.content,'lxml')
    for tag in soup.find_all(class_="cc"):
        #print(tag.attrs['href'])
        comment_url = tag.attrs['href']
        print(comment_url)
        get_comments(comment_url, headers, cookies)
    #    print(tag)


