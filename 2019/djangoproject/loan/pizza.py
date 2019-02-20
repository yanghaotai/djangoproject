# -*- coding:utf-8 -*-

from urllib.parse import quote
from lxml import etree

import json
import requests
import time

"""
    爬取全国各大城市的必胜客餐厅
@Author yht
@Date 2019-2-20
"""


def get_stores(city):
    """ 根据城市获取餐厅信息 """
    session = requests.Session()
    # 对【城市|0|0】进行 Url 编码
    city_urlencode = quote(city + '|0|0')
    # 用来存储首页的 cookies
    cookies = requests.cookies.RequestsCookieJar()
    # print(cookies)

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Host': 'www.pizzahut.com.cn',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }

    # print('============第', count, '个城市:', city, '============')
    resp_from_index = session.get('http://www.pizzahut.com.cn/', headers=headers)
    # 然后将原来 cookies 的 iplocation 字段，设置自己想要抓取城市。
    cookies.set('AlteonP', resp_from_index.cookies['AlteonP'], domain='www.pizzahut.com.cn')
    cookies.set('iplocation', city_urlencode, domain='www.pizzahut.com.cn')
    # print(cookies)

    page = 1
    restaurants = []

    while True:
        data = {
            'pageIndex': page,
            'pageSize': "50",
        }

        response = session.post('http://www.pizzahut.com.cn/StoreList/Index', headers=headers, data=data, cookies=cookies)
        html = etree.HTML(response.text)
        # 获取餐厅列表所在的 div 标签

        divs = html.xpath("//div[@class='re_RNew']")
        # print(divs)
        # print(len(divs))
        temp_items = []
        for div in divs:
            item = {}
            content = div.xpath('./@onclick')[0]
            # print(content)
            # ClickStore('22.538912,114.09803|城市广场|深南中路中信城市广场二楼|0755-25942012','GZH519')
            # 过滤掉括号和后面的内容
            content = content.split('(\'')[1].split(')')[0].split('\',\'')[0]
            # print(content)

            if len(content.split('|')) == 4:
                coordinate = content.split('|')[0]
                restaurant_name = content.split('|')[1] + '餐厅'
                address = content.split('|')[2]
                phone = content.split('|')[3]
                item = '餐厅名:%s；餐厅地址:%s；餐厅电话:%s；餐厅坐标:%s' % (restaurant_name, address, phone, coordinate)
                # print(item)
            else:
                restaurant_name = content.split('|')[0] + '餐厅'
                address = content.split('|')[1]
                phone = content.split('|')[2]
                item = '餐厅名:%s；餐厅地址:%s；餐厅电话:%s' % (restaurant_name, address, phone)

            temp_items.append(item)
            # print(temp_items)

        if not temp_items:
            break
        restaurants += temp_items
        page += 1
        time.sleep(1)
    return restaurants


# t = get_stores('鞍山')
# print(t)
# print(t[0])
