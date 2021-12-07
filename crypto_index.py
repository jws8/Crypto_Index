#Webscrapping program to get the current price 
# on set amount of cryptocurrencies
#Author: Joshua W Smith (https://www.github.com/jws8)
#Date: 11/28/2021
import requests
from bs4 import BeautifulSoup as BS
#urls
bitcoin_url = "https://www.google.com/search?q=bitcoin+price"
eth_url = "https://www.google.com/search?q=ethereum+price"
bnb_url = "https://www.google.com/search?q=Binance+coin+price"
sol_url = "https://www.google.com/search?q=Solana+price"
doge_url = "https://www.google.com/search?q=Doge+price"
#input
ans = ""
def write_data(pretty_soup):
    with open("html_fun.txt", "w") as f:
        f.write(pretty_soup)
def get_price(url):
    #data to parse
    data = requests.get(url)
    #what to parse from and parser from Beautiful Soup
    soup = BS(data.text, "html.parser")
    #Write data from html request to txt file (new each time: "a")
    
    write_data(soup.prettify())
    #Looking for something in our soup and put it to text...
    try:
        price = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
        news = soup.find("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).text
        #Write data from html request to txt file (new each time: "a")
        
        #Print results to console
        print (ans +" today is worth: " + str(price) + "s.")
        print("News for " + ans + " today! \n" + str(news)+ "\n")
    except AttributeError:
        print("Nothing found.")
def prompt():
    global ans
    ans = input("Enter the crypto you would like to learn about today (press ENTER or type \"exit\" to quit): ")
while True:
    prompt()
    if ans == "exit" or ans == "":
        break
    elif ans == "BTC" or ans == "btc" or ans =="bitcoin":
        get_price(bitcoin_url)
    elif ans == "ETH" or ans == "eth":
        get_price(eth_url)
    elif ans == "BNB" or ans == "bnb":
        get_price(bnb_url) 
    elif (ans == "Doge" or ans == "DOGE"
        or ans == "dogcoin" or ans == "doge"
        or ans == "dogecoin"):
        get_price(doge_url)
    elif ans == "SOL":
        get_price(sol_url)
    else:
        print("Your cryptocurrency is not listed by our application, sadly. :(")
           



