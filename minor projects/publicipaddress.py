# pip install requests
# import requests module
from requests import get
ip = get("https://api.ipify.org").text
print('your public ip address is ',ip)
