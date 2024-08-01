from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

finance = list()

for page in range(1, 11) :
  finance_url = f'https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page={page}'
  print(finance_url)
  html = urllib.request.urlopen(finance_url)
  soup = BeautifulSoup(html, 'html.parser')
  tag_tbody = soup.find('table', class_='type_2')
  
  for sub in tag_tbody.find_all('tr') :
    fin_td = sub.find_all('td')
    if len(fin_td) > 1:
      fin_name = fin_td[1].get_text(strip=True)
      fin_price = fin_td[2].get_text(strip=True).replace(',', '')
      fin_compare = fin_td[3].get_text(strip=True).replace(',', '')
      fin_comPercent = fin_td[4].get_text(strip=True).replace(',', '')
      fin_tradecount = fin_td[9].get_text(strip=True).replace(',', '')
      
      print(fin_name)
      print(fin_price)
      print(fin_compare)
      print(fin_comPercent)
      print(fin_tradecount)
      
      if fin_td is not None:
        finance.append([fin_name] + [fin_price] + [ fin_compare] + [fin_comPercent] + [fin_tradecount])
        
print(f'RESULT : \r\n{finance}')

finance_tbl = pd.DataFrame(data = finance)

finance_tbl.to_csv('./finance_table_EXCEL.csv', encoding='cp949', mode='w', index=True)

finance_tbl.to_csv('./finance_table_NoIndex.csv', encoding='utf-8', mode='w', index=False)
