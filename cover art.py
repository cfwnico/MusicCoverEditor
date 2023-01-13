import requests

proxy_list = {"http": "http://127.0.0.1:10800", "https": "https://127.0.0.1:10800"}

session = requests.session()
session.proxies.update(proxy_list)
r = session.get(
    "http://coverartarchive.org/release/76df3287-6cda-33eb-8e9a-044b5e15ffdd"
)


# r = requests.get(
#     "http://coverartarchive.org/release/76df3287-6cda-33eb-8e9a-044b5e15ffdd",
# )
print(r.status_code)
print(r.json())
# 被墙了
