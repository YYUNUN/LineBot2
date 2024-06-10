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

texts1 = ['必勝客', '拿波里', '肯德基', '麥當勞', 'ABV 美式餐酒館', 'AK12美式小館', 'H&W Restaurant and Bar', '發福廚房', '金色三麥', 'the Chips', '樂子 the Diner', 'Campus cafe', 'Housebistro好適廚坊']
texts2 = ['頤宮', '興蓬萊台菜餐廳', '國賓中餐廳', '朧粵 Longyue', '捌伍添第 85TD', '喜來登', '私廚‧小酒棧', 'THE上海', '天香樓Tien Hsiang Lo', '今大滷肉飯', '吉甜不辣', '鑫鱻熱炒', '阿城鵝肉', '丰禾台式小館']
texts3 = ['偷飯賊', 'GG季吉韓國美食餐飲房', 'WAYO 哇優', '東輝韓食館', '米食 미식', '韓食堂한식당', '大發韓式特色料理', 'Tigerroar 韓虎嘯', '小飯館兒', '林家匠韓國部隊鍋', '首爾飯桌 - 서울밥상', 'NiL Kitchen 尼歐廚房', 'K bab 大叔的飯卷', '米花停', '朝鮮味', '韓華園']
texts4 = ['瓦城', '1010湘', '大心', '泰鑽泰式料理', '哈哈囉55泰式船面', 'Lisa泰式美食',  'Kanokwan 老麵攤', '泰街頭', '三攀泰泰國料理', '泰鼎泰式料理']
texts5 = ['欣葉日本料理', 'NAGOMI', '彩日本料理', '金子半之助 ', '九州鬆餅', '日本橋海鮮丼つじ半',  '丼飯店', '心 KOKORO 食堂', '大和日本料理', '三井料理美術館']


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
