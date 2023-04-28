from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon import TelegramClient, sync
from telethon import events
from telethon.tl.custom import Button
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from bs4 import BeautifulSoup
import time
import re, threading
from time import sleep
c = requests.session()
def css():
	api_id = '2192036'
	api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
	client = TelegramClient('session', api_id, api_hash)
	client.start()
	channel_username = '@zmmbot'
	channel_entity = client.get_entity(channel_username)
	client.send_message('zmmbot' ,'/start2')
	for cftf in range(99999):
	    sleep(4)
	    mssag = client.get_messages('zmmbot', limit=1)
	    mssag[0].click(2)
	    sleep(4)
	    mssag1 = client.get_messages('zmmbot', limit=1)
	    mssag1[0].click(0)
	    for ffguf  in range(10000):
	        sleep(3)
	        l = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	        j = l.messages[0]
	        
	        print('hi')
	        if j.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	            sleep(30)
	            mssag4 = client.get_messages('zmmbot', limit=1)
	            mssag4[0].click(1)
	            client.send_message('me','مافي قنوات بعد')
	            break
	        if j.message.find('• تم اضافة 10 نقاط الى حسابك (اذا قمت بمغادرة القناة سيتم خصم ضعف النقاط)\n\n• لا يوجد قنوات او مجموعات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	            print('خلصت القنات ')
	            sleep(30)
	            mssag5 = client.get_messages('zmmbot', limit=1)
	            mssag5[0].click(1)
	            break
	        url = j.reply_markup.rows[0].buttons[0].url
	        try :
	            try :
	               client(JoinChannelRequest(url))
	            except :
	                bott = url.split('/')[-1]
	                client(ImportChatInviteRequest(bott))
	            mssag2 = client.get_messages('zmmbot', limit=1)
	            mssag2[0].click(text="التالي")
              
	        except :
	            client.send_message('me','حظروك معلم ')
	            break
	            client.disconnect()



css()