import requests
import simplejson
headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.10171 SLBChan/105'
}
list_url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1668328342899&mid=b39690c4fb8230d4594cf15caa96d6bf&uuid=b39690c4fb8230d4594cf15caa96d6bf&dfid=11SwIK0V9y9y4fCnNn4dhY0N&keyword=%E5%A4%A7%E9%B1%BC&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=3bfd4bf6f0312594cc7fe4d284e54cb1'
list_resp = requests.get(list_url,headers=headers)
song_list=simplejson.loads(list_resp.text[12:-2])['data']['lists']
for i,s in enumerate(song_list):
    print(f'{i+1}----{s.get("SongName")}----{s.get("FileHash")}----{s.get("AlbumID")}')

num = input("请输入要下载第几首音乐：")


info_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={song_list[int(num)-1].get("FileHash")}&album_id={song_list[int(num)-1].get("AlbumID")}'
headers2= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.10171 SLBChan/105',
    'Cookie': 'kg_mid=b39690c4fb8230d4594cf15caa96d6bf; kg_dfid=11SwIK0V9y9y4fCnNn4dhY0N; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1668325191,1668327127; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1668340512'
}
info_resp = requests.get(info_url,headers=headers2)
m_url = info_resp.json()['data']['play_url']
m_resp = requests.get(m_url,headers=headers)
#创建文件用于储存爬取的东西
with open('sss.mp3','wb') as f:
    f.write(m_resp.content)









































