from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

viewership_chizizic = list() # 여기에 뷰어십 저장
for date1 in range(1, 9) :
  viewership = f'https://viewership.softc.one/stats/naverchzzk?statsDate=yesterday&statsDatestartDateTime=2024-05-0{date1}T15%3A00%3A00.000Z&statsDateendDateTime=2024-05-0{date1 + 1}T14%3A59%3A59.999Z'
  print(viewership)
  
  html = urllib.request.urlopen(viewership)
  #time.sleep(3)
  soup_viewership = BeautifulSoup(html, 'html.parser')
  
  # tag_class = soup_viewership.find('div', class_ = 'Card_TitleBox__TUsVC')
  store = soup_viewership.find_all(class_='Card_Title__yiAPT')[0]
  # store_td = store.find_all(class_='Card_Title__yiAPT')
  store_name = store.string
  
  # store_sido = store_td[0].string
  # store_add = store_td[3].string
  # store_phone = store_td[5].string
  viewership_chizizic.append([store_name])
  print('결과' + store_name)  
    # + [store_sido] + [store_add] + [store_phone
    
viewership = f'https://viewership.softc.one/stats/naverchzzk?statsDate=yesterday&statsDatestartDateTime=2024-05-09T15%3A00%3A00.000Z&statsDateendDateTime=2024-05-10T14%3A59%3A59.999Z'
print(viewership)
html = urllib.request.urlopen(viewership)
#time.sleep(3)
soup_viewership = BeautifulSoup(html, 'html.parser')
#tag_class = soup_viewership.find('div', class_='Card_TitleBox__TUsVC')
store = soup_viewership.find_all(class_='Card_Title__yiAPT')[0]
# store_td = store.find_all(class_='Card_Title__yiAPT')
store_name = store.string

# store_sido = store_td[0].string
# store_add = store_td[3].string
# store_phone = store_td[5].string
viewership_chizizic.append([store_name])
print('결과' + store_name) 
  
for date1 in range(10, 31) :
  viewership = f'https://viewership.softc.one/stats/naverchzzk?statsDate=yesterday&statsDatestartDateTime=2024-05-{date1}T15%3A00%3A00.000Z&statsDateendDateTime=2024-05-{date1 + 1}T14%3A59%3A59.999Z'
  print(viewership)
  
  html = urllib.request.urlopen(viewership)
  #time.sleep(3)
  soup_viewership = BeautifulSoup(html, 'html.parser')
  #tag_class = soup_viewership.find('div', class_='Card_TitleBox__TUsVC')
  store = soup_viewership.find_all(class_='Card_Title__yiAPT')[0]
  # store_td = store.find_all(class_='Card_Title__yiAPT')
  store_name = store.string
  
  # store_sido = store_td[0].string
  # store_add = store_td[3].string
  # store_phone = store_td[5].string
  viewership_chizizic.append([store_name])
  print('결과' + store_name)  
    # + [store_sido] + [store_add] + [store_phone
    
print(f'RESULT : \r\n{viewership_chizizic}')

viewership_chi_tbl = pd.DataFrame(data = viewership_chizizic, columns = ['viwership'])

viewership_chi_tbl.to_csv('./viewership_chizizic.csv', encoding = 'cp949', mode = 'w', index = True)

viewership_chi_tbl.to_csv('./viewership_chizizic_NoIndex.csv', encoding = 'utf-8', mode = 'w', index = False)