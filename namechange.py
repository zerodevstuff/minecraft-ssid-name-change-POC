import requests
from requests.structures import CaseInsensitiveDict
ssid = input('ssid: ')
newname = input('new name: ')
url = ("https://api.minecraftservices.com/minecraft/profile/name/" + newname)
headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {ssid}"
resp = requests.put(url, headers=headers)
print(resp.status_code)