# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13md6bTHESIAbCcRbXQoWnPNAie58rwHA
"""

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, LocationSendMessage, TemplateSendMessage, MessageTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from linebot.models import *
from linebot.models import ImageSendMessage
import random


import os
line_bot_api = LineBotApi(os.environ.get('Channel_Access_Token'))
handler = WebhookHandler(os.environ.get('Channel_Secret'))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@今天要喝啥':
        sendCarousel(event)

    elif mtext == '@今天要吃啥':
        sendImgCarousel(event)
    

def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                       thumbnail_image_url='https://tcpass-static.taichung.gov.tw/storeFile/33558/33558_imageCover.png',
                        title='五桐號',
                        text='茶飲專賣',
                       actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我要看五桐號菜單'
                            ),
                            URITemplateAction(
                                label='我的網頁',
                                uri='https://www.wootea.com/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://photo.518.com.tw/photo/2/77/3152921/1689233745862094426.png',
                        title='COCO',
                        text='知名手搖',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我要看COCO菜單'
                            ),
                            URITemplateAction(
                              label='我的網頁',
                              uri='https://www.facebook.com/cocofreshtea.tw/?locale=zh_TW'
                            )
                        ]
                    ),
                    CarouselColumn(
                         thumbnail_image_url='https://meet.eslite.com/Content/Images/Brand/2-LOGO_20181221110420.png',
                        title='迷克夏',
                        text='鮮奶是我的專長',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我要看迷克夏菜單'
                            ),
                            URITemplateAction(
                               label='我的網頁',
                               uri='https://milksha.com/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.chingshin.tw/upload/image/%E6%B8%85%E5%BF%83.png',
                        title='清新福全',
                        text='隨處可見',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我要看清新福全菜單'
                            ),
                            URITemplateAction(
                               label='我的網頁',
                               uri='https://www.chingshin.tw/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://twcoupon.com/images/logo/p_freshnature.png',
                        title='先自然',
                        text='我就講求自然',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我要看先自然菜單'
                            ),
                            URITemplateAction(
                               label='我的網頁',
                               uri='https://freshnature.tw/'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))




def sendImgCarousel(event):  #圖片轉盤
    random_text1 = random.choice(texts1)
    random_text2 = random.choice(texts2)
    random_text1 = random.choice(texts3)
    random_text2 = random.choice(texts4)
    random_text2 = random.choice(texts5)
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='美式',
                            text='美式'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='中式',
                            text='美式'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='韓式',
                            text='美式'
                        )
                    ),
                     ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='泰式',
                            text='美式'
                        )
                    ),
                     ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='日式',
                            text='美式'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))



if __name__ == '__main__':
    app.run()
