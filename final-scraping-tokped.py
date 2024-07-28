from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def fetchingProducts(wait, driver):
    page = 1
    
    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    driver.get(str(get_url) + '?perpage=10')
            
    while True:
        time.sleep(2)
        print(f"============= produk halaman: {page} ===============")
        try:
            products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1sn1xa2')))
            print(f"jumlah data: {len(products)}")
            
            for index in range(len(products)):
                try:
                    # Refresh the list of products to avoid stale element reference
                    container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="css-tjjb18"]')))
                    result_container = container.find_elements(By.CSS_SELECTOR, 'div[class="css-1sn1xa2"]')
                    
                    product = result_container[index]
                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", product)
                    wait.until(EC.element_to_be_clickable(product)).click()

                    current_url = driver.current_url
                    print(f"URL produk ke-{index + 1}: {current_url}")
                    
                    title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pdp_comp-product_content"]/div/div[1]/h1')))
                    print(f"nama ke-{index + 1}: {title.text}")
                    
                    driver.back()
                    
                    if index == len(products) - 1:
                        paginations = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="btnShopProductPageNext"]')))
                        driver.execute_script("arguments[0].click();", paginations)
                        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="css-1sn1xa2"]')))
                        page += 1
                except Exception as e:
                    print(f"Kesalahan saat memproses produk ke-{index + 1}: {e}")
                    continue
        except Exception as e:
            print(e)
            print("===== ambil produk selesai =======")
            return False



def startScraping(chrome_driver_path, keyword_search):
    chrome_options = Options()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    try:
        driver.get("https://www.tokopedia.com")
        wait = WebDriverWait(driver, 20)
        search_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'exxxdg63')))
        search_box.send_keys(keyword_search)
        search_box.send_keys(Keys.ENTER)
        search_toko = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="btnSRPShopTab"]')))
        search_toko.click()
        klik_toko = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="shop-card"]')))
        for result in klik_toko:
            try:
                toko_name_element = result.find_element(By.CSS_SELECTOR, 'span[data-testid="spnSRPShopName"]')
                toko_name = toko_name_element.text
                if keyword_search in toko_name:
                    toko_header = result.find_element(By.CSS_SELECTOR, 'a[data-testid="shop-card-header"]')
                    toko_header.click()
                    break
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
        else:
            print("Tidak ditemukan toko yang sesuai")
        klik_produk = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="Produk"]')))
        klik_produk.click()
        fetchingProducts(wait, driver)
    finally:
        driver.quit()


chrome_driver_path = "D:\\Programs\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
keyword_search = "Gateway Indonesia Comp"

startScraping(chrome_driver_path, keyword_search)
