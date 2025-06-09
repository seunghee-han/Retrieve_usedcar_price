import requests
from xml.etree import ElementTree as ET
from urllib.parse import urlparse, urlencode, quote
import requests
import pandas as pd

def search_car(name,yy,kk):
    total_list=[]
    for num_page in range(1,3):
        url=f'https://mycarsave.lotterentacar.net/cr/search/ajax/list?country=&perPageNum=15&page={num_page}&orderType=&carType=&categoryGroup=%5B%22%22%5D&minYear=&maxYear=&minMileage=&maxMileage=&minPrice=&maxPrice=&minInstPrice=&maxInstPrice=&minRentPrice=&maxRentPrice=&minSalePrice=&maxSalePrice=&instPriceMonth=&color=&fuel=&option=&carNumber=&keyword=&themeId=&themeType=&brandCert=&retailShopId=&dealerRegKey=&sellAdminKey=&cert=&manage=&promotion=&reqDirect=&consult=&rentBuy=&tagList=&sTagList=&saleTyAll=&saleTyRent=&saleTySale=true&_=1749434478230'
        head = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'}
        r = requests.get(url, headers=head)
        data = r.json()
        if 'result' in data and 'data' in data['result']:
            car_data = data['result']['data']
            for i in range(len(car_data)):
                total_list.append({'brandName': car_data[i]['brandName'],'modelName': car_data[i]['modelName'],'regYear':car_data[i]['regYear'],
                                'mileage':car_data[i]['mileage'],'priceNew':car_data[i]['priceNew'],'returnPrice':car_data[i]['returnPrice']})

    total_dataframe=pd.DataFrame(total_list)
    serch_dataframe=total_dataframe[total_dataframe['brandName'] == str(name)]
    serch_dataframe=serch_dataframe[total_dataframe['regYear'].astype(int) >= yy] 
    serch_dataframe=serch_dataframe[serch_dataframe['mileage'].astype(int) >= kk]

    return serch_dataframe



def car_info(num):
    total_list=[]
    for num_page in range(1,num):
        url=f'https://mycarsave.lotterentacar.net/cr/search/ajax/list?country=&perPageNum=15&page={num_page}&orderType=&carType=&categoryGroup=%5B%22%22%5D&minYear=&maxYear=&minMileage=&maxMileage=&minPrice=&maxPrice=&minInstPrice=&maxInstPrice=&minRentPrice=&maxRentPrice=&minSalePrice=&maxSalePrice=&instPriceMonth=&color=&fuel=&option=&carNumber=&keyword=&themeId=&themeType=&brandCert=&retailShopId=&dealerRegKey=&sellAdminKey=&cert=&manage=&promotion=&reqDirect=&consult=&rentBuy=&tagList=&sTagList=&saleTyAll=&saleTyRent=&saleTySale=true&_=1749434478230'
        head = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'}
        r = requests.get(url, headers=head)
        data = r.json()
        if 'result' in data and 'data' in data['result']:
            car_data = data['result']['data']
            for i in range(len(car_data)):
                total_list.append({'brandName': car_data[i]['brandName'],'modelName': car_data[i]['modelName'],'regYear':car_data[i]['regYear'],
                                'mileage':car_data[i]['mileage'],'priceNew':car_data[i]['priceNew'],'returnPrice':car_data[i]['returnPrice']})

    total_dataframe=pd.DataFrame(total_list)
    return total_dataframe