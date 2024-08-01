import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Naver Finance KOSDAQ market summary page
url = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=1'

# Request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Lists to store stock names and prices
stock_names = []
stock_prices = []

# Locate the table containing the stock data
table = soup.find('table', class_='type_2')
rows = table.find_all('tr')

# Loop through the rows and extract the stock names and prices
for row in rows:
    columns = row.find_all('td')
    if len(columns) > 1:  # Ensure the row contains data
        stock_name = columns[1].get_text(strip=True)
        stock_price = columns[2].get_text(strip=True)
        if stock_name and stock_price:  # Ensure both name and price are not empty
            stock_names.append(stock_name)
            stock_prices.append(stock_price)
            if len(stock_names) == 30:  # Stop after getting top 10 stocks
                break

# Create a DataFrame
df = pd.DataFrame({
    'Stock Name': stock_names,
    'Price': stock_prices
})

# Save DataFrame to a CSV file
df.to_csv('kosdaq_popular_stocks.csv', index=False)

# Print the DataFrame
print(df)
