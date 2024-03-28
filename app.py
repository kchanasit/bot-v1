from flask import Flask, request
from linebot import *

app = Flask(__name__)

line_bot_api = LineBotApi('xxxxxx')
handler = WebhookHandler('xxxxxx')

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    return 'OK'

if __name__ == "__main__":
    app.run()