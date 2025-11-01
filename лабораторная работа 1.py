import requests
import time
site='https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
my_list=[]
try:
    for i in range(11):
        response = requests.get(site,timeout=5)
        json= response.json()
        price = (float(json['price']))
        my_list.append(price)
        if len(my_list)>=2:
            if my_list[-1]*1.001>my_list[-2]:
                print(my_list[-1],'ALERT: рост больше на 0,01%')
            if my_list[-1]*1.001<my_list[-2]:
                print(my_list[-1],'ALERT: рост ниже на 0,01%')
        else:
            print(price)
        time.sleep(10)
except Exception as e:
    print(e)

