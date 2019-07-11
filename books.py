import requests
from lxml import etree
import os, time
from selenium import webdriver

#1、请求首页，拿到HTML抽取小说名、小说链接
headers={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)" 
                  " Chrome/63.0.3239.132 Mobile Safari/537.36",
    "Connection": "keep-alive",
    "Cookie": "_csrfToken=cpfqJzQaswWGfyEUsfs6bHk24eKBLmapVNtdV3ZC; newstatisticUUID=1562762458_1503595130; e1=%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_B58%22%2C%22l1%22%3A5%7D; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; e2=%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_B58%22%2C%22l1%22%3A5%7D; lrbc=1010468795%7C386305455%7C0%2C1004608738%7C346953260%7C1; rcr=1010468795%2C1004608738; bc=1010468795",
    "Host": "book.qidian.com",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language" : "zh-CN,zh;q=0.9"
}

class Spider(object):
    def index_request(self):
        response = requests.get('https://www.qidian.com/all')
        html = etree.HTML(response.text)
        booktitle_list = html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        booksrc_list = html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        for title, src in zip(booktitle_list, booksrc_list):
            if os.path.exists(title) == False:
                os.mkdir(title)
            print(title, src)
            self.detail_request(title, src)

    # 2、请求拿到目录数据，抽取章名、章链接
    def detail_request(self, bigtitle, src):
        url = 'https:'+src
        #response = requests.get(url, headers=headers)
        brower = webdriver.Chrome()
        brower.get(url)
        brower.find_element_by_xpath('//*[@id="j_catalogPage"]').click()
        time.sleep(1)
        item_list = brower.find_elements_by_xpath('//*[@id="j-catalogWrap"]/div[*]/div[*]/ul/li/a')
        #.find_elements_by_class_name('cf')
        for item in item_list:
            #提取到目录名称和链接
            print(item.text,item.get_attribute('href'))

        #print(response.text)
        #html = etree.HTML(response.text)
        '''
        littitle_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        litsrc_list = html.xpath('//ul[@class="cf"]/li/a/@href')
        for title, src in zip(littitle_list, litsrc_list):
            print(bigtitle, title, src)
            #self.conten_request(bigtitle, title, src)
'''
    def conten_request(self, bigtit, littitle, src):
        response = requests.get('https:' + src, headers=headers)
        html = etree.HTML(response.text)
        content = '\n'.join(html.xpath('//div[@class="read-content j_readContent]/p/text()'))
        filename = bigtit+'\\'+littitle + '.txt'
        with open(filename, 'wb', encoding='utf-8') as f:
            f.write(content)

#3、请求文章，拿到HTML数据，抽取文章内容并保存

spider = Spider()
spider.index_request()