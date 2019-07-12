from aip import AipSpeech

app_id = '16787563'
api_key='BWdUiU6W9w45RnvOOGlYIAKQ'
secret_key ='Yg0UZapvh2QYhna1bB2R2mQuaXgFOBWK'

client = AipSpeech(app_id,api_key,secret_key)

with open('凡人修仙之仙界篇\\仙界篇外传一.txt','r') as f:
    str_list  =f.readlines()
    f.close()
for str in str_list:
    #print(str)
    result = client.synthesis(str, 'zh', 1, {
        'vol': 5,  # 合成音频文件的准音量
        'spd': 4,  # 语速取值0-9,默认为5中语速
        'pit': 8,  # 语调音量,取值0-9,默认为5中语调
        'per': 1  # 发音人选择,0为女声,1为男生,3为情感合成-度逍遥,4为情感合成-度丫丫,默认为普通女
    })
    with open('audio.mp3', 'ab') as f:
        f.write(result)


