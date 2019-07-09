from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นางสาว ชณาพัฒน์ วิรุฬห์วณิชย์ เลขที่ 26 ชั้น ม.4/9"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    userText = decoded["events"][0]['message']['text']
    #sendText(user,userText)
    if (userText == 'สวัสดี') :
        sendText(user,'สวัสดีค่ะ')
    elif (userText == 'บาย') :
        sendText(user,'ลาก่อน โชคดีค่ะ')
    elif (userText == 'เธอชื่ออะไร') :
        sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    elif (userText == 'ชื่อไร') :
        sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    elif (userText == 'ชื่ออะไร') :
        sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    elif (userText == 'คุณชื่อไร') :
        sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    elif (userText == 'ฮิรากะ') :
        sendText(user,'ว่าไงคะ? ฮิรากะยินดีรับฟังค่ะ')
    elif (userText == 'รักนะ') :
        sendText(user,'ถึงฉันจะเป็นแค่บอทแต่ว่าก็ยินดีค่ะ รักคุณเหมือนกันนะคะ')
    elif (userText == 'ฉันรักคุณ') :
        sendText(user,'รักคุณเช่นกันค่ะ')
    elif (userText == 'คิดถึง') :
        sendText(user,'เช่นกันค่ะ')
    elif (userText == 'งอล') :
        sendText(user,'เอ๋!!! ฮิรากะทำอะไรผิดไปรึเปล่าคะ ต้องขอโทษด้วยจริงๆค่ะ')
    elif (userText == 'โกรธ') :
        sendText(user,'เอ๋!!! ฮิรากะทำอะไรผิดไปรึเปล่าคะ ต้องขอโทษด้วยจริงๆค่ะ')
    elif (userText == 'กาก') :
        sendText(user,'เอ๋!!! ฮิรากะทำอะไรผิดไปรึเปล่าคะ ต้องขอโทษด้วยจริงๆค่ะ')
    elif (userText == 'หยิ่งหรอ') :
        sendText(user,'เอ๋!!! เปล่านะคะ ต้องขอโทษด้วยค่ะ')
    elif (userText == 'ลาก่อน') :
        sendText(user,'ล่าก่อนค่ะ')
    elif (userText == 'ฝันดี') :
        sendText(user,'ฝันดีค่ะ')
    elif (userText == 'สบายดีเปล่า') :
        sendText(user,'ฉันเป็นแค่บอทไม่มีความรู้สึกนึกคิดหรอกค่ะ')
    elif (userText == 'สบายดีมั้ย') :
        sendText(user,'ฉันเป็นแค่บอทไม่มีความรู้สึกนึกคิดหรอกค่ะ')
    elif (userText == 'ประยุทธคือใคร') :
        sendText(user,'ฉันขอไม่พูดถึงเรื่องนี้ละกันนะคะ-_-;;')
    elif (userText == 'ประวิตรคือใคร') :
        sendText(user,'เราไม่ควรเข้าเรื่องการเมืองค่ะ-_-;;')
    elif (userText == 'อีดอก') :
        sendText(user,'อย่าใช้คำหยาบคายสิคะ')
    elif (userText == 'เหี้ย') :
        sendText(user,'ไม่เอาไม่ดีนะคะ')
    elif (userText == 'ควาย') :
        sendText(user,'ไม่เอาแบบนี้สิ ไม่น่ารักเลยค่ะ')
    elif (userText == 'กระหรี่') :
        sendText(user,'อย่าทำตัวต่ำไปมากกว่านี้ค่ะ')
    else :
        sendText(user,'เอ่อ...ฉันไม่เข้าใจที่คุณพูดน่ะค่ะ')
 
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
