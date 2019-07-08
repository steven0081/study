import json
import base64
import requests

#1、读取图片数据，整合两张图片JSON数据
with open('6.png', 'rb') as f:
    pic1 = f.read()

with open('china.jpg', 'rb') as f:
    pic2 = f.read()

image_data = json.dumps(
    [
        {'image': str(base64.b64encode(pic1), 'utf-8'), 'image_type': 'BASE64', 'face_type': 'LIVE', 'quality_control': 'LOW'},
        {'image': str(base64.b64encode(pic2), 'utf-8'), 'image_type': 'BASE64', 'face_type': 'IDCARD', 'quality_control': 'LOW'}
    ]
)
#2、拼接API接口
get_token = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=DzDCjiMxSGoc3HtUmxySbtXu&client_secret=dCYoXlz9mcNzsuklqbwdPhxt7SZxGKNo'
API_url = 'https://aip.baidubce.com/rest/2.0/face/v3/match?access_token='

text = requests.get(get_token).text
access_token = json.loads(text)['access_token']
print(access_token)
url = API_url + access_token
#3、请求API接口传入数据，返回图片相似度
response = requests.post(url, data= image_data)
print(response.text)

score = json.loads(response.text)['result']['score']
if score > 80 :
    print('图片相似度为：{} ，同一个人！'.format(score))
else:
    print('图片相似度为：{} ，不是同一个人！'.format(score))

