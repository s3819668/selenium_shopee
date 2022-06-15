from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
import concurrent.futures
import time
import json
import SimplifiedTraditional
import os

def option_add(options):
    options.add_argument("--disable-notifications")
    # options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    return options

def crawler(page):
    def roll():
        for i in range(100):
            js = "var q=document.documentElement.scrollTop=" + str(i * 100)
            driver.execute_script(js)
            time.sleep(0.1)
    options = Options()
    options=option_add(options)
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920,1080)
    url = "https://shopee.tw/%E5%A8%9B%E6%A8%82%E3%80%81%E6%94%B6%E8%97%8F-cat.11041645"+'?page='+str(page)
    driver.get(url)
    roll()
    product_name=driver.find_elements(by=By.CLASS_NAME, value='Cve6sh')
    product_price=driver.find_elements(by=By.CLASS_NAME,value="rVLWG6")
    product=dict(zip([i.text for i in product_name],[i.text for i in product_price]))
    if len(product_name)==0:
        return
    print(product)
    with open('everypage/'+str(page)+".txt", "w",encoding='utf-8') as f:
        print(product,file=f)
    # print(len(product_name),len(product_price))
    driver.close()

def get_max_page():
    options = Options()
    options=option_add(options)
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    url = "https://shopee.tw/%E5%A8%9B%E6%A8%82%E3%80%81%E6%94%B6%E8%97%8F-cat.11041645"
    driver.get(url)
    max_page = driver.find_elements(by=By.CLASS_NAME, value='shopee-mini-page-controller__total')
    num=int(max_page[0].text)
    driver.close()
    return num

def translate(s):
    translate_table=SimplifiedTraditional.get_table(True)
    for i in translate_table:
        if i in s:
            s=s.replace(i,translate_table[i])
    return s

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(crawler, [i for i in range(get_max_page())])
    for file in os.listdir('everypage'):
        with open("everypage/"+file, 'r+', encoding="utf-8") as f:
            ori = f.read()
            f.seek(0)
            f.truncate()
            table = SimplifiedTraditional.get_table(True)
            for i in table:
                if i in ori:
                    ori = ori.replace(i, table[i])
            f.write(ori)

    arr = []
    for file in os.listdir("everypage"):
        with open("everypage/" + file, "r", encoding="utf-8")as f:
            arr.append(f.read())
    with open('shopee.json', 'w', encoding="utf-8") as f:
        print(json.dumps(arr, ensure_ascii=False), file=f)

if __name__=="__main__":
    main()
