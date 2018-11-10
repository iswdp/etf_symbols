from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, pickle
from etf_list import etf_symbols

browser = webdriver.Firefox(executable_path=r'/home/iswdp/geckodriver')

#----------------------------------------------------------------------------------------------------------------------------

with open('etf_attributes.dict', 'rb') as fi:
    data = pickle.load(fi)

for k in etf_symbols:
    if k not in list(data.keys()):
        browser.get('https://etfdb.com/etf/' + str(k) + '/')
        time.sleep(0)

        name = browser.find_elements_by_class_name('data-title')[0].text.split(' ',1)[1:][0]
        category = browser.find_elements_by_class_name('symbol')[1].text
        print(name, '------------------', category)

        data[k] = {'name': name, 'category': category}

with open('etf_attributes.dict', 'wb') as fi:
    pickle.dump(data, fi)