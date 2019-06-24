#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 11:31
# @Author  : dieuroi
# @Site    : 
# @File    : getreviews.py
# @Software: PyCharm
from lxml import etree
from selenium import webdriver
from xslt_lib import *
import re
import xmltodict
import time
import Queue

queue = Queue.Queue()
proxyHost = ""
proxyPort = ""
proxyUser = ""
proxyPass = ""
service_args = [
        "--proxy-type=http",
        "--proxy=%(host)s:%(port)s" % {
            "host" : proxyHost,
            "port" : proxyPort,
        },
        "--proxy-auth=%(user)s:%(pass)s" % {
            "user" : proxyUser,
            "pass" : proxyPass,
        },
    ]


def genRe():
    name_flag = 'profile.php\?USER_ID=(.+)'
    global name_re
    name_re = re.compile(name_flag, re.S)


def readfile(filename, startPos): #'AVA.txt'
    with open(filename) as f:
        text = f.readlines()[startPos-1:]
        for line in text:
            pic_id = line.split()[1]
            queue.put(pic_id)
        return queue.qsize()


def read_userid(text):
    name_regx = name_re.search(text)
    name = name_regx.group(1)
    return name


def editurlist(text, dic_xml):
    review_a_photo = text + '\n'
    if not 'ur' in dic_xml:
        print 'no key [ur]!'
        return None
    if dic_xml['ur'] is None:
        return None
    if not 'item' in dic_xml['ur']:
        print 'no key [item]!'
        return None
    review_num = len(dic_xml['ur']['item'])
    review_a_photo += str(review_num) + '\n'
    if review_num < 1:
        print 'no reviews get!'
    elif review_num == 1:
        review_an_item = read_userid(dic_xml['ur']['item']['user'])+'\n'+dic_xml['ur']['item']['review']+'\n'
        review_a_photo += review_an_item
    else:
        for i in range(review_num):
            review_an_item = read_userid(dic_xml['ur']['item'][i]['user']) + '\n' + dic_xml['ur']['item'][i]['review'] + '\n'
            review_a_photo += review_an_item
    return review_a_photo


def downloading_cmd(url, xslt_root):
    # use webdriver.PhantomJS
    browser = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe', service_args=service_args)
    browser.get(url)
    time.sleep(3)

    transform = etree.XSLT(xslt_root)

    # return DOM after executing js
    html = browser.execute_script("return document.documentElement.outerHTML")
    browser.quit()
    doc = etree.HTML(html)
    # extract keywords from DOM
    result_tree = transform(doc)
    return result_tree



def check_no_author(text):
    url = '''http://www.dpchallenge.com/image.php?IMAGE_ID={0}'''.format(text)
    xslt_root = etree.XML(no_author)
    result_tree = downloading_cmd(url, xslt_root)
    result_str = str(result_tree).split('\n', 1)[1]
    dic_xml = xmltodict.parse(result_str)
    if 'item' in dic_xml['noAuthor']:
        # True: means no comments after the challenge
        return True
    else:
        return False


def downloading_review(text, noAuthor):
    url = '''http://www.dpchallenge.com/image.php?IMAGE_ID={0}'''.format(text)
    review_xslt = ur_no_author if noAuthor else ur_with_author
    xslt_root = etree.XML(review_xslt)
    result_tree = downloading_cmd(url, xslt_root)
    result_str = str(result_tree).split('\n', 1)[1]
    dic_xml = xmltodict.parse(result_str)
    return editurlist(text, dic_xml)


def downloadingreviews(pic_id):
    try:
        # noAuthor = check_no_author(pic_id)
        review_a_photo = downloading_review(pic_id, True)
        if review_a_photo is None:
            review_a_photo = downloading_review(pic_id, False)
        with open('suc-review.txt', 'ab+') as f_review:
            f_review.write(review_a_photo)
            print(pic_id + ':Review Saved!')
    except Exception, e:
        print Exception, ':', e
        with open('failed-review.txt', 'ab+') as f_failed:
            f_failed.write(pic_id + '\n')


if __name__ == '__main__':
    # genRe()
    # text = readfile('AVA.txt', 2919)
    # downloadingreviews(text)
    print readfile('AVA.txt', 2919)

