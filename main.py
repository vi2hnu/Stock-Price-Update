from bs4 import BeautifulSoup
import requests
import threading

soup = BeautifulSoup(requests.get('https://www.screener.in/company/HCLTECH/consolidated/').text, 'lxml')
stack = []
stack.append(0)
stock_price = soup.find_all('span', class_='number')
name = soup.find_all('span', class_='name')
file_path = 'C:\\Users\\Vishnu\\Downloads\\output.txt'
def repeat_print():
    with open(file_path, 'a') as file:
        soup = BeautifulSoup(requests.get('https://www.screener.in/company/HCLTECH/consolidated/').text, 'lxml')
        stock_price = soup.find_all('span', class_='number')
        prev = stack[-1]
        file.write("Current stock price is " + str(stock_price[1].text) + "\n")
        stack.append(int(stock_price[1].text.replace(',', '')))
        if stack[-1] > prev:
            file.write("Stock price has gone up, might be a good time to sell\n")
            file.write("\n")
        elif stack[-1] < prev:
            file.write("Stock price has gone down, might be a good time to buy\n")
            file.write("\n")
        else:
            file.write("No change in stock price\n")
            file.write("\n")

    timer = threading.Timer(600, repeat_print)
    timer.start()

repeat_print()
