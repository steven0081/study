import json
import base64
import requests
import urllib


#1、读取图片文件
with open('1.png', 'rb') as f:
    pic1 = f.read()
data = dict()
data['languagetype'] = "CHN_ENG"  # 识别文字
data['image'] = str(base64.b64encode(pic1), 'utf-8')
decoded_data = urllib.parse.urlencode(data)
#2、获取access_token，拼接API接口
get_token = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
            'client_id=L8DSGvCxigKvQxYGGR5b6OUn&client_secret=PnLBBvgV71A12NMSEG2PECbhTFxOpmNl'
#通用文字识别
API_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic/?access_token='
#手写文字识别
#API_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting/?access_token='
#高精度文字识别
#API_url= 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic/?access_token='
headers={"Content-Type": "application/x-www-form-urlencoded"}
text = requests.get(get_token).text
access_token = json.loads(text)['access_token']
#print(access_token)
url = API_url + access_token
#3、请求API接口传入数据，返回文字
response = requests.post(url, data= decoded_data, headers=headers)
#print(response.text)
words_result = json.loads(response.text)['words_result']
temp_file = open('temp.txt', 'a')
for words in words_result:
    temp_file.writelines(words['words']+'\n')
    #print(words['words'])

temp_file.close()
