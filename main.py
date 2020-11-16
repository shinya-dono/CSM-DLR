import os
import requests
import shutil

chap = input("enter chapter number: ")
page = 0
os.makedirs(f"{chap}", exist_ok=True)
while True:
    page += 1
    print(f"downloading {page}")
    file = f"https://s6.mangabeast01.com/manga/Chainsaw-Man/{chap.zfill(4)}-{str(page).zfill(3)}.png"
    r = requests.get(file, stream=True)
    if r.status_code == 200:
        with open(f"{chap}/{page}.png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        break
