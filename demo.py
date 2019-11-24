import requests

import time
f=open('flag.txt','r')
ss=open('ss.txt','r')
postapi='http://www.cqooc.com/learnLog/api/add'
for i,a in zip(f,ss):

        print(i.strip())
        print(a.strip())
        id=a.strip()

        ssid=i.strip()
        cookie = {
            'player':'1',
            'xsid':'165F2725D2A57DB'
        }
        head={
            'Host': 'www.cqooc.com',
            'Content-Length': '159',
            'Origin': 'http://www.cqooc.com',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'http://www.cqooc.com/learn/mooc/structure?id=334566107',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
            'Cookie': 'xsid=488C219A327C5294; player=1',



        }

        data={
            "username": "你的账号", "ownerId": 1281232, "parentId": "11803860", "action": 0,
             "courseId": "334566107", "sectionId": ssid, "chapterId": id, "category": 2
        }
        ps = requests.post(url=postapi, json=data, headers=head, timeout=None)
        time.sleep(5)
        print('当前id'+ssid)
        print('当前ssid'+id)
        print(ps.reason)
        print(ps.cookies)
        print(ps.text)
        time.sleep(10)
