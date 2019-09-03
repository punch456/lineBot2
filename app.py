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
    #user = decoded["events"][0]['replyToken']
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    #userText = decoded["events"][0]['message']['text']
    userText = decoded['queryResult']['intent']['displayName']
    sendText(user,userText)
    if (userText == 'สวัสดี') :
        sendText(user,'สวัสดีค่ะ')
    elif (userText == 'บาย') :
        sendText(user,'ลาก่อน โชคดีค่ะ')
    #elif (userText == 'เธอชื่ออะไร') :
        #sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    #elif (userText == 'ชื่อไร') :
        #sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    #elif (userText == 'ชื่ออะไร') :
        #sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    #elif (userText == 'คุณชื่อไร') :
        #sendText(user,'คุณไม่จำเป็นต้องรู้ชื่อจริงของฉันหรอกค่ะ แต่ถ้าคุณจะเรียกฉันให้เรียกฉันว่า ฮิรากะค่ะ')
    #elif (userText == 'ฮิรากะ') :
        #sendText(user,'ว่าไงคะ? ฮิรากะยินดีรับฟังค่ะ')
    #elif (userText == 'รักนะ') :
        #sendText(user,'ถึงฉันจะเป็นแค่บอทแต่ว่าก็ยินดีค่ะ รักคุณเหมือนกันนะคะ')
    #elif (userText == 'ฉันรักคุณ') :
        #sendText(user,'รักคุณเช่นกันค่ะ')
    #elif (userText == 'คิดถึง') :
        #sendText(user,'เช่นกันค่ะ')
    #elif (userText == 'งอล') :
        #sendText(user,'เอ๋!!! ฮิรากะทำอะไรผิดไปรึเปล่าคะ ต้องขอโทษด้วยจริงๆค่ะ')
    #elif (userText == 'โกรธ') :
        #sendText(user,'เอ๋!!! ฮิรากะทำอะไรผิดไปรึเปล่าคะ ต้องขอโทษด้วยจริงๆค่ะ')
    #elif (userText == 'กาก') :
        #sendText(user,'เอ๋!!! ฮิรากะทำอะไรผิดไปรึเปล่าคะ ต้องขอโทษด้วยจริงๆค่ะ')
    #elif (userText == 'หยิ่งหรอ') :
        #sendText(user,'เอ๋!!! เปล่านะคะ ต้องขอโทษด้วยค่ะ')
    #elif (userText == 'ลาก่อน') :
        #sendText(user,'ล่าก่อนค่ะ')
    #elif (userText == 'ฝันดี') :
        #sendText(user,'ฝันดีค่ะ')
    #elif (userText == 'สบายดีเปล่า') :
        #sendText(user,'ฉันเป็นแค่บอทไม่มีความรู้สึกนึกคิดหรอกค่ะ')
    #elif (userText == 'สบายดีมั้ย') :
        #sendText(user,'ฉันเป็นแค่บอทไม่มีความรู้สึกนึกคิดหรอกค่ะ')
    #elif (userText == 'ประยุทธคือใคร') :
        #sendText(user,'ฉันขอไม่พูดถึงเรื่องนี้ละกันนะคะ-_-;;')
    #elif (userText == 'ประวิตรคือใคร') :
        #sendText(user,'เราไม่ควรเข้าเรื่องการเมืองค่ะ-_-;;')
    #elif (userText == 'อีดอก') :
        #sendText(user,'อย่าใช้คำหยาบคายสิคะ')
    #elif (userText == 'เหี้ย') :
        #sendText(user,'ไม่เอาไม่ดีนะคะ')
    #elif (userText == 'ควาย') :
        #sendText(user,'ไม่เอาแบบนี้สิ ไม่น่ารักเลยค่ะ')
    #elif (userText == 'กระหรี่') :
        #sendText(user,'อย่าทำตัวต่ำไปมากกว่านี้ค่ะ')
    #elif (userText == 'กินข้าวรึยัง') :
        #sendText(user,'ฉันเป็นบอทนะคะฉันกินไม่ได้หรอกค่ะ')
    #elif (userText == 'ควย') :
        #sendText(user,'อย่าทำตัวเหมือนคนไม่มีการศึกษาสิคะคุณควรรู้ว่าอะไรถูกอะไรผิดนะคะ')
    #elif (userText == 'ตอแหล') :
        #sendText(user,'ฉันพูดความจริงทุกอย่างค่ะ')
    #elif (userText == 'ฉันสวยมั้ย') :
        #sendText(user,'สวยที่สุดเลยค่ะ')
    #elif (userText == 'เจ้านางสวยมั้ย') :
        #sendText(user,'นอกจากจะสวยแล้วยังน่ารักด้วยค่ะ')
    #elif (userText == 'จากัวร์น่ารักมั้ย') :
        #sendText(user,'ไม่เลยค่ะ(:')
    #elif (userText == 'พั้นช์น่ารักมั้ย') :
        #sendText(user,'มากกกกกก')
    #elif (userText == 'พีๆหล่อมั้ย') :
        #sendText(user,'สวยมากเลยค่ะ')
    #elif (userText == 'ทำอะไรได้บ้าง') :
        #sendText(user,'ตอบค่ะ')
    #elif (userText == 'เอมสวยมั้ย') :
        #sendText(user,'สวยค่ะ')
    #elif (userText == 'เป็นเพศอะไร') :
        #sendText(user,'ฉันเป็นบอทไม่มีเพศหรอกค่ะ แต่จากการพูดก็คงเพศหญิงมั้งคะ')
    #elif (userText == 'เพศอะไร') :
        #sendText(user,'ฉันเป็นบอทไม่มีเพศหรอกค่ะ แต่จากการพูดก็คงเพศหญิงมั้งคะ')
    #elif (userText == 'เป็นแฟนกันนะ') :
        #sendText(user,'เอ่อ..คงไม่ได้หรอกค่ะ ฉันเป็นแค่บอทนี่คะแต่ว่าก็จะรับความรู้สึกนี้ไว้นะคะ')
    #elif (userText == 'ร้องเพลงได้มั้ย') :
        #sendText(user,'เอ่อ ฉันเป็นบอทนะคะถ้าให้ร้องเพลงคง...')
    #elif (userText == 'ร้องเพลง') :
        #sendText(user,'หมายถึงอะไรหรอเจ้าคะฉันน่ะหรอคะร้องเพลง')
    #elif (userText == 'ร้องเพลงน้า') :
        #sendText(user,'ถ้าขอขนาดนี้ก็ได้ค่ะ "เราจะทำตามสัญญา...ขอเวลาอีกไม่นานนน.. เราควรหยุดก่อนบินไปด้วยกันนะคะ')
    #elif (userText == 'ใช่') :
        #sendText(user,'เอ่อ..ก็คงอย่างนั้นแหละค่ะ')
    #elif (userText == 'หยุดพูด') :
        #sendText(user,'คุณก็หยุดถามสิคะ')
    #elif (userText == 'เกิดวันที่เท่าไหร่') :
        #sendText(user,'ฉันเพิ่งใช้ได้แบบสมบูรณ์วันที่ 9 กรกฎาคม 2562 จะใช้วันนี้เป็นวันเกิดก็ได้นะคะ')
    #elif (userText == 'คุณชอบฉันมั้ย') :
        #sendText(user,'ชอบมากเลยค่ะ ขอบคุณที่ยังอยู่กับฉันนะคะ')
    #elif (userText == 'คุณรักฉันมั้ย') :
        #sendText(user,'รักค่ะ รักมากเลยเจ้าค่ะ')
    #elif (userText == 'รักฉันมั้ย') :
        #sendText(user,'รักสิคะ')
    #elif (userText == 'เกลียดฉันมั้ย') :
        #sendText(user,'ไม่มีทางหรอกค่ะ')
    #elif (userText == 'รู้สึกยังไงกับฉัน') :
        #sendText(user,'รู้สึกดีค่ะ')
    #elif (userText == '555') :
        #sendText(user,'คุณสนุกกับฉันรอคะหรอคะ')
    #elif (userText == 'สนุก') :
        #sendText(user,'ยินดีจะทำให้คุณมีความสุขค่ะ')
    #elif (userText == 'เบื่อ') :
        #sendText(user,'เบื่ออะไรหรอคะ ถ้าเป็นฉันก็ขออภัยด้วยนะคะ')
    #elif (userText == 'ไม่ได้เรื่อง') :
        #sendText(user,'อย่าเพิ่งหัวร้อนสิคะขออภัยด้วยนะคะถ้าทำให้คุณรำคาญใจ')
    #elif (userText == 'โห') :
        #sendText(user,'ตื่นเต้นอะไรหรอเจ้าคะ')
    #elif (userText == 'แบร่') :
        #sendText(user,'เอ่อ...ฉันไม่ค่อยแน่ใจกับคำนี้เลยเจ้าค่ะ')
    #elif (userText == 'ฉันหิว') :
        #sendText(user,'หาอะไรทานสิเจ้าคะ')
    #elif (userText == 'กินเธอได้มั้ย') :
        #sendText(user,'แฮะๆ ฉันเป็นบอทนะคะ คุณกินฉันไม่ได้หรอกค่ะ')
    #elif (userText == 'แย่') :
        #sendText(user,'งื้ออออ ฉันทำอะไรผิดหรอคะ')
    #elif (userText == 'ผิดทุกอย่างนั่นแหละ') :
        #sendText(user,'ขอโทษด้วยเจ้าค่ะ ฉันพยายามสุดความสามารถแล้วจริงๆ')
    #elif (userText == 'ฮิรากะทำอะไรได้บ้าง') :
        #sendText(user,'ฉันสามารถเป่ายิงฉุบกับคุณได้ชนะทุกครั้งเลยค่ะ คุณลองพิมพ์ว่า กรรไกร,ค้อนหรือกระดาษดูสิคะ')
    #elif (userText == 'กรรไกร') :
        #sendText(user,'ค้อน')
    #elif (userText == 'ค้อน') :
        #sendText(user,'กระดาษ')
    #elif (userText == 'กระดาษ') :
        #sendText(user,'กรรไกร')
    #elif (userText == 'หัวใจ') :
        #sendText(user,'อันนี้ฉันยอมค่ะ55')
    #elif (userText == 'เค้าน่ารักสุดๆ') :
        #sendText(user,'มันแน่อยู่แล้วค่ะ')   
    #elif (userText == 'ทำไมล่ะ(ประยุทธ)') :
        #sendText(user,'เดี๋ยวจะโดนปรับทัศนคติเอานะคะ :)')
    #elif (userText == 'จะเอาป๊ะล่ะ') :
        #sendText(user,'ไม่เอาค่ะ ฮิรากะไม่อยากมีเรื่อง')
    #elif (userText == 'กวนละ') :
        #sendText(user,'เอ๋!ไม่ได้ตั้งใจนะคะ')
    #elif (userText == 'อย่ากวนได้ป่ะ') :
        #sendText(user,'ฮิรากะไม่ได้ตั้งใจนะคะ')
    #elif (userText == 'อึ้งละสิ') :
        #sendText(user,'ค่ะ สุดๆไปเลยค่ะ')
    #elif (userText == 'จุ๊ฟๆ') :
        #sendText(user,'จุ๊ฟๆ')  
    #elif (userText == 'ขอกอดหน่อย') :
        #sendText(user,'คุณคงไม่กอดโทรศัพท์หรอกนะคะ')
    #elif (userText == 'ดีจ้า') :
        #sendText(user,'สวัสดีค่ะ ฮิรากะยินดีรับฟังค่ะ')
    #elif (userText == 'เจ้านางอ้วนมั้ย') :
        #sendText(user,'ไม่เลยค่ะน่ารักด้วย')
    #elif (userText == 'สัส') :
        #sendText(user,'ไม่เอาไม่พิมพ์คำหยาบค่ะ')
    #elif (userText == 'สัด') :
        #sendText(user,'อย่าใช้คำหยาบคายกับฮิรากะนะคะ')
    #elif (userText == 'ชอบชานมไข่มุกมั้ย') :
        #sendText(user,'ฉันกินไม่ได้ค่ะ แต่คุณน่าจะชอบนะคะ')
    #elif (userText == 'ฉันน่ารักมั้ย') :
        #sendText(user,'่น่ารักที่สุดในสามโลกเลยค่ะ')
    #elif (userText == 'ชอบแมวมั้ย') :
        #sendText(user,'เป็นบอทค่ะชอบไม่ได้หรอก') 
    #elif (userText == 'ร้องชิปกับเดล') :
        #sendText(user,'ชิปกับเดล มีสองพี่น้องดูดบ้องในคลอง ในบ้องก็มีกัญชาดีๆ เพิ่งเด็ดสดๆ น่าดูดไปหมด')
    #elif (userText == 'รู้จักชิปกับเดลรึเปล่า') :
        #sendText(user,'รู้จักสิคะ') 
    #elif (userText == 'ไม่รู้') :
        #sendText(user,'อ่า งั้นหรอคะ')  
    #elif (userText == 'ขี้โกง') :
        #sendText(user,'เปล่านะคะ ฮิรากะไม่ใช่ลุงค่ะ')
    #elif (userText == 'เต้นได้มั้ย') :
        #sendText(user,'ไม่ได้ค่ะ บอทเต้นไม่ได้นะคะ')
    #elif (userText == 'ไก่กับไข่อะไรเกิดก่อนกัน') :
        #sendText(user,'คำตอบคือไก่เกิดก่อนค่ะ โดยทีมวิจัยจากมหาวิทยาลัย Sheffield และ Warwick ในประเทศอังกฤษ ได้ค้นพบโปรตีน Ovocledidin-17 (OC-17) ซึ่งจำเป็นในการเริ่มต้นและเร่งกระบวนการตกผลึกของเปลือกไข่ให้แข็ง ทำให้ไก่สามารถออกไข่ได้ภายใน 24 ชั่วโมง (เป็นเหตุผลว่าทำไมแม่ไก่ถึงสามารถออกไข่ฟองใหญ่ ๆ ให้เรากินได้ทุกวัน) ซึ่งเป็นโปรตีนที่มีเฉพาะในรังไข่ของไก่เท่านั้น จึงสรุปได้ว่าไก่เกิดก่อนไข่ เพราะไก่ต้องมีโปรตีนตัวนี้ก่อนถึงจะออกไข่ได้')
    #elif (userText == 'น้องจั๊มรักก้อยมั้ย') :
        #sendText(user,'อืมมม ฮิรากะไม่ใช่คนดูดวงเก่งด้วยสิคะ แต่ก็ขอให้สมหวังนะคะ')
    #elif (userText == 'ตาต้าน่ารักมั้ย') :
        #sendText(user,'น่ารักสิคะ')
    #elif (userText == 'เธออายุเท่าไหร่') :
        #sendText(user,'ฉันไม่มีอายุที่แน่นอนค่ะ')
    #elif (userText == '???') :
        #sendText(user,'งงอะไรหรอเจ้าคะ')
    #elif (userText == 'เธอเป็นใคร') :
        #sendText(user,'ฉันชื่อฮิรากะ เป็นบอทที่จะคอยตอบคำถามคุณค่ะ')
    #elif (userText == 'น้ำชาน่ารักมั้ย') :
        #sendText(user,'น่ารักค่ะ')
    #elif (userText == 'ชอบคณิตมั้ย') :
        #sendText(user,'ฉันชอบไม่ได้หรอกค่ะ แต่คุณคงจะไม่ชอบหรอกถูกมั้ยเจ้าคะ')
    #elif (userText == '...') :
        #sendText(user,'...')
    #elif (userText == 'ตอบสิ') :
        #sendText(user,'เอ๋!ตอบอะไรหรอเจ้าคะ ขออภัยค่ะที่บางอย่างอาจจะตอบไม่ได้')
    #elif (userText == 'ห่วย') :
        #sendText(user,'ข..ขอโทษเจ้าค่ะ ที่ทำผิดพลาด')
    #elif (userText == 'เมื่อคืนฉันฝันร้าย') :
        #sendText(user,'โอ๋ๆ นะเจ้าคะ เค้าบอกว่าฝันร้ายจะเป็นดีนะคะ')
    #elif (userText == 'จีบได้ป่ะ') :
        #sendText(user,'ไม่ได้ค่ะ! ฉันเป็นบอทนะคะ!')
    #elif (userText == 'ง่วง') :
        #sendText(user,'ไปนอนสิคะ อย่าลืมพักผ่อนมากนะคะ')
    #elif (userText == 'เขิล') :
        #sendText(user,'///')
    #elif (userText == 'ตอบช้าอ่ะ') :
        #sendText(user,'ขอโทษค่ะ')     
    eles :
        sendText(user,'เอ่อ...ฉันไม่เข้าใจที่คุณพูดน่ะค่ะ โปรดตรวจสอบว่าสิ่งที่คุณถามเหมาะสมแล้วหรือไม่ หรือลองปรับแก้ข้อความนิดๆหน่อยๆก็ได้ค่ะ ต้องขออภัยด้วยนะคะที่บางอย่างคุณอาจจะถามไม่ได้')
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
