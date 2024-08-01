from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests

product_data = []
# product_prices = []

for page in range(1, 3) :
  url = f'https://www.e-himart.co.kr/app/display/showDisplayCategory?dispNo=1011020000#pageCount={page}'
  response = requests.get(url)
  print(url)
  if response.status_code == 200:
      html = response.text
      soup = BeautifulSoup(html, 'html.parser')
      products = soup.select('div.prdItem.cateGoods')
      for product in products :
        tag_name = product.select_one('p.prdName')
        tag_price = product.select_one('span.discountPrice strong')
        
        # print(tag_name.string)
        # print(tag_price.string)
        
        # product_.append([tag_name.string] + [tag_price.string])
        
        if tag_name and tag_price:
                name = tag_name.get_text(strip=True)
                price = tag_price.get_text(strip=True)
                product_data.append([name, price])
        
  else : 
      print(response.status_code)
      
print(f'RESULT : \r\n{product_data}')    

product_table = pd.DataFrame(data = product_data, columns=('제품명', '가격'))

product_table.to_csv('./product_table_EXCEL.csv', encoding = 'cp949', mode = 'w', index=True)

product_table.to_csv('./product_table_NoIndex.csv', encoding = 'utf-8', mode='w' , index=False)