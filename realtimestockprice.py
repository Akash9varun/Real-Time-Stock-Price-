from yahoo_fin import stock_info
import smtplib
import requests 



brands = input("Enter The Company : ")


while True:
    price = stock_info.get_live_price(brands)
    print(price)
  
    
