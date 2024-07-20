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
    
    while True:
        
        print(f"============= produk halaman: {page} ===============")
        
        # Scroll down
        time.sleep(4)
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(4)
        
        try:
            paginations = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="btnShopProductPageNext"]')))
        except Exception as e:
            print(f"Error finding pagination: {e}")
            break
        
        if paginations:
            try:
                # Ambil nama produk
                products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1sn1xa2')))
                print(f"jumlah data: {len(products)}")
                
                for index, product in enumerate(products):
                    try:
                        product.click()
                        title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pdp_comp-product_content"]/div/div[1]/h1')))
                        print(f"nama ke-{index + 1}: {title.text}")
                    except Exception as e:
                        print(f"Error mendapatkan title: {e}")
                    
                    driver.back()
                
                try:
                    # Find the pagination element again before clicking
                    paginations = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="btnShopProductPageNext"]')))
                    paginations.click()
                    page += 1
                except Exception as e:
                    print(f"Error clicking pagination: {e}")
                    break

            except Exception as e:
                print(f"Error getting products: {e}")
                break
        else:
            print("===== ambil produk selesai =======")
            return False
    


def startScraping(chrome_driver_path, keyword_search):
    chrome_options = Options()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    try:
        driver.get("https://www.tokopedia.com")
        wait = WebDriverWait(driver, 20)  # Meningkatkan waktu tunggu

        # Cari kotak pencarian
        search_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'exxxdg63')))
        search_box.send_keys(keyword_search)
        search_box.send_keys(Keys.ENTER)

        # Cari tombol toko
        search_toko = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[1]/div/button[2]")))
        search_toko.click()

        # Klik toko
        klik_toko = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[2]/div[2]/div/div/a")))
        klik_toko.click()

        # Klik produk
        klik_produk = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="Produk"]')))
        klik_produk.click()
        
        fetchingProducts(wait, driver)

    finally:
        driver.quit()


chrome_driver_path = "D:\Programs\chromedriver-win64\chromedriver-win64\chromedriver.exe"
keyword_search = "Gateway Indonesia Comp"

startScraping(chrome_driver_path, keyword_search)
