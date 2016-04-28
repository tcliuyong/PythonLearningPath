# -*- coding:utf-8 -*-
import getURLContent
from Shop import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
MAX_SIZE = 10
PATH  = "D:\\shop.txt"
p = re.compile(r"<a class=\"link f3\" href=(.*) target=\"_blank\">")
URL = "http://hrb.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.4.in1gfzeu"
if __name__ == "__main__":
    f = open(PATH, "w")

    browser = webdriver.Chrome()
    browser.get(URL)
    browser.maximize_window()
    time.sleep(1)

    while MAX_SIZE > 0:
        for i in range(17):
            time.sleep(1)
            ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
        dic = {}
        htmlContent =  browser.page_source
        urls = p.findall(htmlContent)
        for url in urls:
            url = url.replace("\"", "")
            title, dic = getURLContent.getCateFromURL(url)
            for k, v in dic.items():
                if(k == None or v == None):
                    continue
                f.write(title + "\t")
                f.write(k + "\t")
                f.write(v + "\t")
                f.write("\n")
        time.sleep(2)
        browser.find_element_by_partial_link_text("下一页").click()
        time.sleep(2)
        MAX_SIZE = MAX_SIZE - 1
        del (dic)
    f.close();