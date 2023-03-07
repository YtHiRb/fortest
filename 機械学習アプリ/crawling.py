# %%
#これで作ったぞ
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# %%
path = "env_for_api/.flkr/flkr.txt"
with open(path) as f:
    kands = f.read().split("\n")
key = kands[1]
secret = kands[4]
#print(key,secret)
wait_time = 1#1秒待ってからrequestする

#保存フォルダの設定
animal = sys.argv[1]#コマンドラインの1番目
#python crawling.py boarとかって打った時、pythonプログラムが受け取るsys.argvは
#["crawling.py","boar"]となる
save_dir = "env_for_api/" + animal

# %%
flicker = FlickrAPI(key, secret, format = 'parsed-json')
result = flicker.photos.search(
    text = animal,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)
# pprint(result)
photos = result['photos']
# pprint(photos)

for i, photo in enumerate(photos["photo"]):
    url = photo['url_q']
    file_path = save_dir + "/" + photo["id"] + ".jpg"
    if os.path.exists(file_path) == True:
        continue
    urlretrieve(url, file_path)
    time.sleep(wait_time)


