from yahoo_fin import stock_info
from threading import *
from time import sleep
import json

def threaded_price_stream(ticker):
    while True:
        print(stock_info.get_live_price(ticker))
        sleep(1)

def current_price(ticker):
    dict = {"current_price": str(stock_info.get_live_price(ticker))}
    print(json.dumps(dict))

if __name__ == '__main__':
    ticker = input("Enter the ticker you would like to live stream: ")
    thread = Thread(target=threaded_price_stream, args = (ticker))
    thread.start()
    
