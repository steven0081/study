import requests
import re
import urllib.request

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url_name = []

def get_html():
    url = 'http://www.budejie.com/video/'
    html = requests.get(url).text
    #编写数据选取规则
    url_content = re.compile(r'<div class="j-r-list-c">.*?</div>.*?</div>', re.S)
    url_contents = re.findall(url_content, html)
    for i in url_contents:
        #取视频链接
        url_reg = r'data-mp4="(.*?)"'
        url_items = re.findall(url_reg, i)
        #取视频标题
        if url_items:
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>')
            name_items = re.findall(name_reg, i)
            #print(name_items)
            for i, k in zip(name_items, url_items):
                url_name.append([i, k])
    #print(url_name)
    #保存视频
    for i in url_name:
        print(i[0])
        print(i[1])
        #异常处理
        try:
            urllib.request.urlretrieve(i[1], './video/%s.mp4'%([i[0]]))
        except Exception:
            pass

if __name__ == "__main__":
    get_html()



