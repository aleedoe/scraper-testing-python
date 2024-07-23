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
        time.sleep(4)  # Jika Anda tetap ingin memberikan waktu tidur, ini bisa dipertahankan
        driver.execute_script("window.scrollBy(0, 800);")
        try:
            # Tunggu sampai elemen terakhir muncul
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1sn1xa2')))
        except Exception as e:
            print(f"Error waiting after scroll: {e}")
            break
        
        
        try:
            # Ambil nama produk
            # products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-1sn1xa2')))
            products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-tjjb18')))

            # Find all product elements within the container
            produk2 = products.find_elements(By.CLASS_NAME, 'css-1sn1xa2')

            # Print each product element
            for i, produk in enumerate(produk2, start=1):
                products_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-tjjb18')))
                produk2 = products_container.find_elements(By.CLASS_NAME, 'css-1sn1xa2')
                produk = produk2[i]
                print(f"Product {i}:")
                print(produk.text)
                print("-" * 20)
                produk.click()
                driver.back()
            break
            
            for index, product in enumerate(products):
                try:
                    # Ambil ulang produk berdasarkan indeks
                    driver.execute_script("window.scrollBy(0, 800);")
                    products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1sn1xa2')))
                    
                    try:
                        # Tunggu sampai elemen terakhir muncul setelah scroll
                        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-1sn1xa2')))
                    except Exception as e:
                        print(f"Error waiting after scroll: {e}")
                        break
                    
                    product = products[index]
                    
                    # Klik produk
                    wait.until(EC.element_to_be_clickable(product)).click()
                    title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[data-testid="lblPDPDetailProductName"]')))
                    print(f"nama ke-{index + 1}: {title.text}")
                    
                    # Kembali ke halaman sebelumnya
                    driver.back()
                    
                    # Tunggu sampai halaman kembali sepenuhnya
                    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1sn1xa2')))
                    
                    if index == enumerate(products):
                        try:
                            # Find the pagination element again before clicking
                            paginations = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="btnShopProductPageNext"]')))
                            paginations.click()
                            page += 1
                        except Exception as e:
                            print(f"Error clicking pagination: {e}")
                            break
                        
                except Exception as e:
                    print(f"Error mendapatkan title: {e}")
                    break
                
        except Exception as e:
            print(f"Error getting products: {e}")
            break    


def startScraping(chrome_driver_path, keyword_search):
    chrome_options = Options()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(30)
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
