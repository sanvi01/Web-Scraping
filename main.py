# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Connect to website
URL = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
page = requests.get(URL, headers=headers)

#Get data from source
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find_all('table')[0]
print(table)

#Find required table from html code
world_titles = table.find_all('th')
print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)

#Create Data frame
df = pd.DataFrame(columns = world_table_titles)
print(df)

column_data = table.find_all('tr')

#Loop to add table content in data frame
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length =len(df)
    df.loc[length] = individual_row_data

print(df)

#Convert data frame to csv file
df.to_csv(r'C:\Users\admin\PycharmProjects\web-scraping\Companies.csv',index= False)
