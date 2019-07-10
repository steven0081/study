from aip import AipSpeech

app_id = ''
api_key=''
secret_key =''

client = AipSpeech(app_id,,api_key,secret_key)

result = client.synthesis('','zh', 1, {

})

with open('audio.mp3', 'wb') as f:
    f.write(result)