import requests
import re
import json

def get_html():
    url = "https://www.maoyan.com/board/4?timeStamp=1786962120077&channelId=40011&index=4&signKey=3eee9ca0ff4391fcafc9b8365b736957&sVersion=1&webdriver=false&offset=0"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers, timeout=10)
    print( resp.status_code)
    with open('maoyan.html', 'w', encoding='utf-8') as f:
        f.write(resp.text)
    return resp.text
def extract_data(html):
    pattern = re.compile(
        '<dd>.*?<i class="board-index.*?">(\d+)</i>.*?<a href="(/films/\d+)" title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>',
        re.S
    )
    res = pattern.findall(html)
    movie_list = []
    for item in res:
        movie_dict = {
            "排名": item[0],
            "电影链接": item[1],
            "电影名称": item[2].strip(),
            "主演": item[3].strip(),
            "上映时间": item[4].strip(),
            "评分": item[5].strip().rstrip('.') + "." + item[6].strip()
        }
        movie_list.append(movie_dict)
    with open("maoyan_movie.json", "w", encoding="utf-8") as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=2)
    print(f"\n一共提取到 {len(movie_list)} 部电影：")
    for m in movie_list:
        print(m)
if __name__ == '__main__':
    html_text = get_html()
    extract_data(html_text)