import requests
import csv
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
# r = requests.get('https://tw.yahoo.com/')

r = requests.get('https://tw.appledaily.com/new/realtime')

#Google 搜尋 URL
google_url = 'https://www.google.com.tw/search'

# 查詢參數
my_params = {'q': '李登輝'}

# 下載 Google 搜尋結果
#r = requests.get(google_url, params = my_params)

  # 開啟輸出的 CSV 檔案
with open('output_test.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile, delimiter= ' ')

  # 寫入一列資料
  writer.writerow(['標題','網址'])

  # 確認是否下載成功
  if r.status_code == requests.codes.ok:
    # 以 BeautifulSoup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    # 觀察 HTML 原始碼
    #print(soup.prettify())

    # 以 CSS 的 class 抓出各類頭條新聞
    stories = soup.select('div.g > h3.r > a[href^="/url"]')
    # stories = soup.find_all('a', class_='story-title')
    # 以 CSS 的 class 抓出各類頭條新聞
    for s in stories:

      # 新聞標題 新聞網址
      print("標題：" + s.text + " 網址：" + s.get('href'))
      writer.writerow([s.text, s.get('href')])