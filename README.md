# Shopee 爬蟲
這個 Python 程序可以從 Shopee 網站上爬取娛樂和收藏品類目的商品名稱和價格信息，並且可以將商品名稱進行繁簡體轉換，把繁體中文轉換為簡體中文。

## 安裝
安裝 Selenium
本程序需要使用 Selenium 模塊來獲取 Shopee 的商品信息，因此在使用前需要安裝 Selenium。可以使用以下命令安裝：

    pip install selenium

安裝 Simplified-Traditional 轉換庫
本程序使用 Simplified-Traditional 轉換庫進行繁簡體轉換。可以使用以下命令安裝：


    pip install Simplified-Traditional

安裝 Chrome 瀏覽器和 Chrome driver
使用 Selenium 模塊需要安裝 Chrome 瀏覽器和 Chrome driver。可以從以下鏈接下載 Chrome 瀏覽器和 Chrome driver：

Chrome 瀏覽器
Chrome driver
下載後，需要將 Chrome driver添加到系統的 PATH 環境變量中。

## 使用方法
運行程式：

python shopee_crawler.py
  
這個程序會爬取 Shopee 網站上娛樂和收藏品類目的商品信息，包括商品名稱和價格，並且將繁體中文轉換為簡體中文。程式運行後會生成一個名為 shopee.json 的文件，這個文件包含了所有爬取到的商品信息。

常見問題
如何指定爬取頁數？
本程序默認爬取 Shopee 網站上娛樂和收藏品類目的所有商品信息。如果想要指定爬取的頁數，可以修改 main() 函数中的以下代碼：


    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(crawler, [i for i in range(get_max_page())])
其中，range(get_max_page()) 代表了要爬取的頁數範圍。如果想要只爬取前 5 頁，可以修改為 range(5)。

## 爬不同蝦皮內容

        url = "https://shopee.tw/%E5%A8%9B%E6%A8%82%E3%80%81%E6%94%B6%E8%97%8F-cat.11041645"+'?page='+str(page)
