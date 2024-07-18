from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def search_and_open_w3schools_article(keyword):
    chrome_driver_path = "D:\\Programs\\chromedriver-win64\\chromedriver.exe"  # Pastikan path ini benar

    chrome_options = Options()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://www.tokopedia.com")
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)  # Meningkatkan waktu tunggu

        # Cari kotak pencarian
        search_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'exxxdg63')))
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)

        # Cari tombol toko
        search_toko = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[1]/div/button[2]")))
        search_toko.click()

        # Klik toko
        klik_toko = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[2]/div[2]/div/div/a")))
        klik_toko.click()

        # Klik produk
        klik_produk = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='zeus-root']/div/div[2]/div[2]/div[2]/div/div/button[2]")))
        klik_produk.click()

        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Tunggu lebih lama untuk memastikan halaman telah di-scroll dan elemen telah dimuat

        # Ambil nama produk
        nama2_produk = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1sn1xa2')))
        
        for result, i in nama2_produk:
            product_link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
            driver.execute_script("window.open(arguments[0]);", product_link)
            driver.switch_to.window(driver.window_handles[-1])
            
            try:
                # Verifikasi XPath yang benar untuk halaman produk
                title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pdp_comp-product_content"]/div/div[1]/h1')))
                print(f"nama ke-{i +1}: {title.text}")
            except Exception as e:
                print(f"Error mendapatkan title: {e}")
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    finally:
        driver.quit()

# Contoh penggunaan
search_and_open_w3schools_article("Gateway Indonesia Comp")
