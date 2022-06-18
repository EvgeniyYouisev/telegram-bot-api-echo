
import requests
import time

TOKEN = 'XXXX'

class RecievedObjects:
    def __init__(self, file: dict):
        self.file = file
        if file['ok'] == True:
            self.status = True
        else:
            self.status = False

    def get_file(self):
        return self.file


offset = 0

while True:
    response = RecievedObjects(requests.get(url=f"https://api.telegram.org/bot{TOKEN}/getUpdates", data={'offset': offset+1} ).json())
    if response.status == True: 
        for message in response.get_file()['result']:
            offset = message['update_id']
            if 'text' in message['message'].keys():
                data = {
                    'chat_id': message['message']['chat']['id'], 
                    'text': message['message']['text']
                    }
                requests.get(url=f"https://api.telegram.org/bot{TOKEN}/SendMessage", data= data)
            else:

                data = {
                    'chat_id': message['message']['chat']['id'], 
                    'text': 'Отправленно не текстовое сообщение'
                    }
                requests.get(url=f"https://api.telegram.org/bot{TOKEN}/SendMessage", data= data)
    else: print ("Ошибка подключения")
    time.sleep(1)
      
# Пример возвращаемого объекта
#     "ok":True,
#     "result":[
#         {
#             "update_id":148093533,
#             "message":
#             {
#                 "message_id":4,
#                 "from":
#                    {
#                       "id":916605457,
#                       "is_bot":False,
#                       "first_name":"\u0416\u0435\u043d\u044f",
#                       "username":"yourisev",
#                       "language_code":"ru"
#                    },
#                 "chat":
#                    {
#                     "id":916605457,
#                     "first_name":"\u0416\u0435\u043d\u044f",
#                     "username":"yourisev",
#                     "type":"private"
#                     },
#                 "date":1654883806,
#                 "text":"asd"
#             }
#         }
#     ]
#     }