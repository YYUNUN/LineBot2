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
from linebot import LineBotApi, WebhookHandler
from linebot.models import TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction, ImageSendMessage, PostbackEvent
from linebot.exceptions import InvalidSignatureError
from flask import Flask, request, abort

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
    if mtext == '@轉盤樣板':
        sendCarousel(event)

    elif mtext == '@圖片轉盤':
        sendImgCarousel(event)
    
    elif mtext == '@星巴克位置':
        sendLocation(event)

def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='五桐號',
                        text='第一個轉盤樣板',
                        actions=[
                            URITemplateAction(
                                label='連結文淵閣網頁',
                                uri='http://www.e-happy.com.tw'
                            ),
                            PostbackTemplateAction(
                                label='查看菜單',
                                data='action=view_menu'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
                        title='COCO',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我們有賣飲料'
                            ),
                            URITemplateAction(
                                label='連結台大網頁',
                                uri='http://www.ntu.edu.tw'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='迷克夏',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我們有賣披薩'
                            ),
                            URITemplateAction(
                                label='連結文淵閣網頁',
                                uri='http://www.e-happy.com.tw'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='清新福全',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我們有賣披薩'
                            ),
                            URITemplateAction(
                                label='連結文淵閣網頁',
                                uri='http://www.e-happy.com.tw'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='先自然',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='菜單',
                                text='我們有賣披薩'
                            ),
                            URITemplateAction(
                                label='連結文淵閣網頁',
                                uri='http://www.e-happy.com.tw'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def handle_postback(event):
    print("Postback event received:", event)  # 添加日志查看事件
    postback_data = event.postback.data
    if postback_data == 'action=view_menu':
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url='https://starslifestyle.com.tw/wp-content/uploads/20200607191949_51.jpg',
                preview_image_url='https://starslifestyle.com.tw/wp-content/uploads/20200607191949_51.jpg'
            )
        )
        print('圖片消息已發送')

def sendImgCarousel(event):  #圖片轉盤
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='我們有賣披薩'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/qaAdBkR.png',
                        action=URITemplateAction(
                            label='連結星巴克',
                            uri='https://www.starbucks.com.tw/home/index.jspx'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/Qg0rsSk.jpg',
                        action=MessageTemplateAction(
                            label='座標位置',
                            text='@星巴克位置'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendLocation(event):
    try:
        message = LocationSendMessage(
            title='星巴克 景美門市', 
            address='116台北市文山區景興路185號1-2F', 
            latitude=24.99301856466003,
            longitude=121.54439425767183
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

if __name__ == '__main__':
    app.run()
