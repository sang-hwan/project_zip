import requests
url = "http://nadocoding.tistory.com"
# what-is-my-user-agent로 user-agent 확인
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)