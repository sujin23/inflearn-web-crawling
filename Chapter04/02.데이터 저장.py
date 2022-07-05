import requests 
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.load_workbook(r'C:\crawling\Chapter04\data.xlsx')
ws = wb.active # 현재 활성화된 시트(기본 시트)

# 종목 코드 리스트
codes = [
  '017670', # sk텔레콤
  '005930', # 삼성전자
  '035720' # 카카오
]

row = 2
for code in codes:
  url = f"https://finance.naver.com/item/sise.naver?code={code}"
  response = requests.get(url)

  html = response.text
  soup = BeautifulSoup(html, 'html.parser')

  price = soup.select_one("#_nowVal").text

  price = price.replace(',','')
  print(price)

  ws[f'B{row}'] = int(price)
  row = row + 1

wb.save(r'C:\crawling\Chapter04\data.xlsx')
