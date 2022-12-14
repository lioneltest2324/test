import requests
import json
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjoxNjcwNzgzNDQ5fQ.cVTAEsCmyXg2h_ZRQJaMPYln0ujb-qGIkbNi0P64A60'
url1 = 'https://api-v2.douyin.wtf/douyin_profile_videos/'
videourl = 'https://v.douyin.com/hBXAnqb/'
count = 4
token = "Bearer" + " " + token
headers={
    "authorization": token
}
k =[]
i = 0
parameters = {'douyin_profile_url':videourl,'count':count}#加入参数来筛选数值
pro_res = requests.get(url1,headers=headers,params=parameters)
data1 = pro_res.content.decode()
a = json.loads(data1)
b = a['aweme_list']
for c in b:
 d = c['video']
 e = d['play_addr']
 f = e['url_list'][0]
 k.append(f)
while i < count:
 t = k[i]
 downlist = requests.get(t)
 with open(r'D:\下载视频源\page%s.mp4'%(i), 'wb') as e:
     e.write(downlist.content)
 i += 1
print("完成")

