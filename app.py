from flask import Flask, request
from linebot.models import *
from linebot import *

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "F69aqD7PK3XMPx7zQcIoN8BlS8/S/ZA37arzBYc+oVpwRLVrTws45FhkdCUUhUePNY/5B4I0+L4jcRGnqBC0KsXtZChXAA2cXRoI6EWW22F8VNNY33bpMVYhYzZ9tByGnW2rjmhW7JjWKNr7H9FyvwdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "0af95e2e39349ba767aa7e2d25998f09"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    reply(intent,text,reply_token,id,disname)

    return 'OK'


def reply(intent,text,reply_token,id,disname):
    if intent == 'intent-5':
        text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        line_bot_api.reply_message(reply_token,text_message)

if __name__ == "__main__":
    app.run()