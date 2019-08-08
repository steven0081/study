import jieba
import requests
import time
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

comment=[]
def make_wordcloud():
    with open('jd_comment_26414687140.txt', mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        for row in rows:
            comment.append(row)
    comment_after_split = jieba.cut(str(comment),cut_all = False)
    print('1')
    word = ''.join(comment_after_split)
    stopwords = STOPWORDS.copy()
    stopwords.add('吃鸡神器')
    stopwords.add('吃鸡')
    stopwords.add('\n')
    stopwords.add("n'")
    bg_image = plt.imread('bg.jpg')
    wc = WordCloud(
        # 设置字体，不指定就会出现乱码，文件名不支持中文
        font_path="simsun.ttf",
        # 设置背景色，默认为黑，可根据需要自定义为颜色
        background_color='white',
        # 词云形状，
        mask=bg_image,
        # 允许最大词汇
        max_words=400,
        # 最大号字体，如果不指定则为图像高度
        max_font_size=100,
        # 画布宽度和高度，如果设置了mask则不会生效
        width=600,
        height=400,
        margin=2,
        # 词语水平摆放的频率，默认为0.9.即竖直摆放的频率为0.1
        prefer_horizontal=0.8
    )
    wc.generate_from_text(word)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file('京东评论云图.jpg')

headers ={
    'Referer': 'https://item.jd.com/26414687140.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def spider_comment(productid,page):
    url = 'https://sclub.jd.com/comment/productPageComments.action?productId={0}&score=0&sortType=6&page={1}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(productid,page)
    print(url)
    response = requests.get(url, headers=headers)
    print(response)
    time.sleep(3)
    content = response.json()
    infos = content['comments']
    for info in infos:
        print(info['content'])
        with open('jd_comment_%s.txt'%productId,'a+', encoding='utf-8') as f:
            f.write(info['content'])

if __name__ =='__main__':
    productId = input('请输入要爬取的商品id:')

    make_wordcloud()

    '''
    for x in range(100):
        print(x)
        spider_comment(productId, x)
    '''


