# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import urllib2
import sys
import time
import datetime
import random

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"}
cookies = {"SUB":"_2A253FogTDeThGeBO7FUU9S7IzDqIHXVU-ChbrDV6PUJbktANLWL_kW1NHetkT2woukv4pz4mMa896p4uw0eODadY", "SCF":"Ao7zgvhWf6yewEBq7gC4fesKQQafgCrFtDaVLVmAFMweZ0KnaDx9Msob3KxImqnUwGDuARmSV3Q1pegqS5axrhg."}
#cookies = {"SUB":"_2A253C9_GDeThGeBO41MV-SnOyzWIHXVU9-GOrDV6PUJbktAKLXPQkW0bP81-DJOpRtZ_EQfHvEhrGAgaHg..", "_T_WM":"4cf6995c969bbc6014318d68fcf2f55d", "SCF":"Ao7zgvhWf6yewEBq7gC4fesKQQafgCrFtDaVLVmAFMwe_HTZyZ6JATXY2N_wBEeMq6iBDyl0NbRuD2K1JPLWR2E"}
proxies = {'https':'https://10.2.170.20:80', 'http':'http://10.2.170.20:80'}
#conn=MySQLdb.connect(host="10.18.65.69",user="recom_tag_rw",passwd="+3jF1cr3z5B4CbB",db="recom_tag",charset="utf8") 
#cursor=conn.cursor()
#proxies = {'https':'https://101.200.235.234:3128'}


def get_comments(keyword, comment_url):
    r=requests.get(comment_url,headers=headers,cookies=cookies)
    soup = BeautifulSoup(r.content, 'lxml')
    content_id = save_content(keyword, comment_url, soup)
    '''
    tag = soup.find('a', string = re.compile(u'查看更多热门'))
    hot_url = tag['href']
    get_hot_comments(hot_url, headers, cookies)
    '''
    pages = soup.find(attrs={'name':'mp'})
    if pages != None:
        pagenum = int(pages.attrs['value'])
    else:
        pagenum = 0
    save_comments(keyword, content_id, soup)
    for i in range(2, pagenum+1):
        next_comment_url = comment_url[:-7] + "&page=" + str(i)
        r=requests.get(next_comment_url,headers=headers,cookies=cookies)
        soup = BeautifulSoup(r.content, 'lxml')
        save_comments(keyword, content_id, soup)
        time.sleep(random.random()+0.5)

def save_content(keyword, url, soup):
    weibo_content = soup.find(id="M_")
    print("weibo_content:\t")
    print(weibo_content)
    content_id = random.randint(1, 10000)
    author = weibo_content.find('a')['href']
    url = url
    text = weibo_content.find(class_="ctt").get_text().lstrip(':')
    #print(text)
    sourceTime = weibo_content.find(class_="ct").string
    shareNum = get_digit(soup.find(attrs={'href': re.compile('/repost/*')}).string)
    likeNum = get_digit(soup.find(attrs={'href': re.compile('#attitude')}).string)
    commentNum = get_digit(soup.find('span', class_="pms").string)
    query = keyword
    contentHtml = weibo_content
    res = (content_id, author, url, text, sourceTime, shareNum, likeNum, commentNum, query, contentHtml)
    print(res)
    return content_id
    
def get_digit(strs):
    return filter(str.isdigit, str(strs))

def save_comments(keyword, content_id, soup):
    parentId = content_id
    comment_id = random.randint(1, 10000)
    for tag in soup.find_all(id = re.compile('C_.*')):
        origin_id = get_digit(tag.attrs['id'])
        author = tag.find('a')['href']
        textWord = tag.find(class_="ctt").get_text()
        sourceTime = tag.find(class_="ct").get_text()
        likeNum = get_digit(tag.find(attrs={'href': re.compile('/attitude/*')}).string)
        query = keyword
        commentHtml = tag
        res = (origin_id, author, textWord, sourceTime, likeNum, query, commentHtml)
        print(res)


def get_hot_comments(hot_url):
    url_prefix = "https://weibo.cn"
    hot_comment_url = url_prefix + hot_url
    r=requests.get(hot_comment_url,headers=headers,cookies=cookies)
    soup = BeautifulSoup(r.content, 'lxml')
    print("weibo_comments:\t")
    for tag in soup.find_all(class_="ctt"):
        print(tag)
        #print(tag.string)


def imagedown(imageurl):
    name = imageurl.split("/")[-1]
    imgpath = "data/"+name
    imgrep = requests.get(imageurl,headers=headers)
    chunk_size=512 #设置chunk大小
    with open(imgpath, 'wb') as fd:
        for chunk in imgrep.iter_content(chunk_size):
            fd.write(chunk)


def get_weibo_content(keyword, url):   
    r=requests.get(url,headers=headers,cookies=cookies)
    soup = BeautifulSoup(r.content,'lxml')
    for tag in soup.find_all(class_="cc"):
        comment_url = tag.attrs['href']
        print(comment_url)
        get_comments(keyword, comment_url)
        time.sleep(1)
    pages = soup.find(attrs={'name':'mp'})
    if pages != None:
        pagenum = pages.attrs['value']
    else:
        pagenum = 0
    return pagenum


def run(keyword):
    strs = urllib2.quote(keyword)
    url = "https://weibo.cn/search/mblog/?keyword=" + strs + "&sort=hot"
    #url = "https://weibo.cn/search/mblog/?keyword=%E5%88%98%E5%BC%BA%E4%B8%9C%E5%9B%9E%E5%BA%94%E4%B8%8D%E7%9F%A5%E5%A6%BB%E7%BE%8E&sort=hot"
    print(url)
    r=requests.get(url, headers=headers, cookies=cookies)
    #r=requests.get(url, headers=headers, cookies=cookies, proxies=proxies)
    soup = BeautifulSoup(r.content,'lxml')
    for tag in soup.find_all(class_="ctt"):
        print(tag)
    #print(soup.pretiffy())

def run_test(keyword):
    strs = urllib2.quote(keyword)
    url = "https://weibo.cn/search/mblog/?keyword=" + strs + "&sort=hot"
    #url = "https://weibo.cn/search/mblog/?keyword=%E5%88%98%E5%BC%BA%E4%B8%9C%E5%9B%9E%E5%BA%94%E4%B8%8D%E7%9F%A5%E5%A6%BB%E7%BE%8E&sort=hot"
    print(url)
    pagenum = int(get_weibo_content(keyword, url))
    #for i in range(2, pagenum+1):
    for i in range(2, 2):
        nexturl = url + "&page=" + str(i)
        print nexturl
        #get_weibo_content(keyword, nexturl)
        #time.sleep(1)

if __name__ == "__main__":
    run_test("不知妻美刘强东")
    #run("不知妻美刘强东")
