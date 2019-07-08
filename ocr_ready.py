import json
import base64
import requests

#1、读取图片数据
with open('text.png', 'rb') as f:
    pic1 = f.read()

image_data = json.dumps(
    [
        {'image': str(base64.b64encode(pic1), 'utf-8'), 'language_type': 'CHN_ENG'}
    ]
)
#2、拼接API接口
get_token = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=tYUZROdFGh8RM8vw6q6y1zFy&client_secret=y9bSmfPrpEAp70YtR6Bv2Rz3GbAd0QcR'
API_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token='

text = requests.get(get_token).text
access_token = json.loads(text)['access_token']
print(access_token)
url = API_url + access_token
#3、请求API接口传入数据，返回图片相似度
response = requests.post(url, data= image_data)
print(response.text)

