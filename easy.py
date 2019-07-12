# python GUI 编程
from tkinter import *
import requests
import json
import pyttsx3
import control

def action():
    result = entry.get().strip()
    print(result)
    control2 = control.Order()
    control.run(result)

def show():
    result = entry.get().strip()
    print(result)
    # 和机器人聊天 ->人工智能->图灵机器人
    #apikey：cc43de65472b4a278ee2818429d285d9
    #调用API接口
    request_data = {
        'key': 'cc43de65472b4a278ee2818429d285d9',
        'info': result,
        'userid': 'joe study Python '
    }
    url = 'http://www.tuling123.com/openapi/api'
    #发送请求API
    response = requests.post(url, request_data)
    #print(response.text)
    # 格式转换
    js_respon = json.loads(response.text)
    #取出想要的值 切片
    respon = js_respon['text']
    # 让结果说出来
    engine = pyttsx3.init()
    engine.say(respon)
    engine.runAndWait()
    #结果输出在第二个显示框
    res.set(respon)

#创建GUI
master = Tk()
master.title('机器人')
#窗口宽X高 ，X轴 Y轴
master.geometry('300x100+450+300')
#设置不能调节大小
master.resizable(False,False)
Label(master, text='输入指令：',font=('黑色',16),fg='blue').grid(row=0, column=0)
Label(master, text='输出指令：',font=('黑色',16),fg='blue').grid(row=1, column=0)
#两个输入框
entry = Entry(master)
entry.grid(row=0, column=1)
res = StringVar()
entry_out = Entry(master, textvariable=res)
entry_out.grid(row=1, column=1)
#按钮
Button(master,text='点击运行',width=10,command=show).grid(row=2, column=0)
Button(master,text='控制电脑',width=10,command=action).grid(row=2, column=1)


master.mainloop()