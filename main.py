from bs4 import BeautifulSoup
import requests
import threading

soup = BeautifulSoup(requests.get('https://www.screener.in/company/HCLTECH/consolidated/').text,'lxml')
stack = []
stack.append(0)
stock_price = soup.find_all('span',class_='number')
name = soup.find_all('span',class_='name')
def repeat_print():
    soup = BeautifulSoup(requests.get('https://www.screener.in/company/HCLTECH/consolidated/').text,'lxml')
    stock_price = soup.find_all('span',class_='number')
    prev = stack[-1]
    print("Current stock price is", stock_price[1].text)
    stack.append(int(stock_price[1].text.replace(',', '')))
    if stack[-1] > prev:
        print("Stock price has gone up, might be a good time to sell\n")
    elif stack[-1]<prev:
        print("Stock price has gone down, might be a good time to buy\n")
    else:
        print("No change in stock price\n")

    
    timer = threading.Timer(150, repeat_print)
    timer.start()

print("HCL Technologies Ltd currently holds mrket cap of",stock_price[0].text,"\n")
repeat_print()