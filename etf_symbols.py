from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, pickle
from etf_list import etf_symbols

browser = webdriver.Firefox(executable_path=r'/home/iswdp/geckodriver')

#----------------------------------------------------------------------------------------------------------------------------
#data = {}
with open('etf_holdings.dict', 'rb') as fi:
    data = pickle.load(fi)

for k in etf_symbols:
    if k not in list(data.keys()):
        try:
            browser.get('https://etfdb.com/etf/' + str(k) + '/')
            time.sleep(5)

            y = []

            last = browser.find_elements_by_class_name('page-last')[0]
            browser.execute_script("arguments[0].click();", last)

            try:
                total_pages = int(browser.find_elements_by_class_name('active')[1].text)

                first = browser.find_elements_by_class_name('page-first')[0]
                browser.execute_script("arguments[0].click();", first)

                for j in list(range(total_pages)):
                    time.sleep(2)
                    tags = browser.find_elements_by_tag_name('a')
                    for i in tags:
                        temp = i.get_attribute('href')
                        if '/stock/' in str(temp):
                            if 'Citigroup Inc ©' in i.text:
                                y.append('C')
                                print(i.text)
                            else:
                                if '(' in i.text:
                                    y.append(i.text.split('(')[1])
                                    print(i.text)

                    nxt = browser.find_elements_by_class_name('page-next')[0]
                    browser.execute_script("arguments[0].click();", nxt)

            except ValueError:
                tags = browser.find_elements_by_tag_name('a')
                for i in tags:
                    temp = i.get_attribute('href')
                    if '/stock/' in str(temp):
                        if 'Citigroup Inc ©' in i.text:
                            y.append('C')
                            print(i.text)
                        else:
                            if '(' in i.text:
                                y.append(i.text.split('(')[1])
                                print(i.text)

            y = [i.split(')')[0] for i in y]
            data[k] = y
        except:
            browser.get('https://etfdb.com/etf/' + str(k) + '/')
            time.sleep(5)

            y = []

            last = browser.find_elements_by_class_name('page-last')[0]
            browser.execute_script("arguments[0].click();", last)

            try:
                total_pages = int(browser.find_elements_by_class_name('active')[1].text)

                first = browser.find_elements_by_class_name('page-first')[0]
                browser.execute_script("arguments[0].click();", first)

                for j in list(range(total_pages)):
                    time.sleep(2)
                    tags = browser.find_elements_by_tag_name('a')
                    for i in tags:
                        temp = i.get_attribute('href')
                        if '/stock/' in str(temp):
                            if 'Citigroup Inc ©' in i.text:
                                y.append('C')
                                print(i.text)
                            else:
                                if '(' in i.text:
                                    y.append(i.text.split('(')[1])
                                    print(i.text)

                    nxt = browser.find_elements_by_class_name('page-next')[0]
                    browser.execute_script("arguments[0].click();", nxt)

            except ValueError:
                tags = browser.find_elements_by_tag_name('a')
                for i in tags:
                    temp = i.get_attribute('href')
                    if '/stock/' in str(temp):
                        if 'Citigroup Inc ©' in i.text:
                            y.append('C')
                            print(i.text)
                        else:
                            if '(' in i.text:
                                y.append(i.text.split('(')[1])
                                print(i.text)

            y = [i.split(')')[0] for i in y]
            data[k] = y

with open('etf_holdings.dict', 'wb') as fi:
    pickle.dump(data, fi)