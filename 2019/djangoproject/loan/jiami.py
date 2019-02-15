#coding:utf-8
from selenium import webdriver
import time
import hashlib

#公用参数
# appid = '10005'
# key = 'EUZ9NunT9DQN+wg6p33vgw=='

############md5程序加密###################
def md5(s):
    md5 = hashlib.md5()
    sign_bytes_utf8 = s.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    sign = md5.hexdigest()
    print('加密结果：'+sign)
    return sign