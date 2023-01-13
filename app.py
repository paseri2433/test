from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
import os

app = Flask(__name__)

@app.route("/")
def hello():
   return "<p>test message2222222222</p>"
   
   #環境変数取得
#YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
#YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

YOUR_CHANNEL_ACCESS_TOKEN = "eGzGOuKskF0sEl+T6b/G9QcV1LXRJCXhMsFcXAydgQx7DJf3eeTOqINB3o0Qpcn7QrzCZe30K5+W7sjaFe/Fa6Ns1ZTDJUgaXtkkUJU2mYmBEv2zFuTtu1b8hYmzWp4bUkpYuCtt4pR0cmN3mE1MSgdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "b46a202827ac29a95d363d2b2343867e"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    print(1)
    signature = request.headers['X-Line-Signature']
    print(2)

    # get request body as text
    body = request.get_data(as_text=True)
    print(3)
    print(body)
    app.logger.info("Request body: " + body)
    print(4)
    # handle webhook body
    try:
        print(5.1)
        handler.handle(body, signature)
        print(5)
    except InvalidSignatureError:
        print(6.1)
        abort(400)
        print(6)
    print(9)
    return 'OK'
    print(10)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(7)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    print(8)


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

print("hellow")