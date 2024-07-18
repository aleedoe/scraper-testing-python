from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def search_and_open_w3schools_article(keyword):
    # Path ke ChromeDriver Anda
    chrome_driver_path = "D:\\Programs\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

    # Mengatur opsi untuk Chrome
    chrome_options = Options()

    # Membuat service object
    service = Service(chrome_driver_path)

    # Membuka browser
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Buka Tokopedia
    driver.get("https://www.tokopedia.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Cari kotak pencarian
    search_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'exxxdg63')))
    
    # Masukkan kata kunci dan tekan Enter
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
    
    # Scroll down untuk memastikan elemen-elemen lainnya terlihat
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Tunggu sebentar untuk memastikan halaman telah tergulir
    
    # ambil nama produk
    nama2_produk = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1sn1xa2')))
    

    for i in range(len(nama2_produk)):
        # Perbarui elemen nama2_produk setiap kali kembali ke halaman sebelumnya
        nama2_produk = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1sn1xa2')))
        result = nama2_produk[i]

        # Scroll ke elemen dan klik menggunakan JavaScript
        driver.execute_script("arguments[0].scrollIntoView(true);", result)
        driver.execute_script("arguments[0].click();", result)
        
        # Tunggu hingga judul produk muncul
        title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pdp_comp-product_content"]/div/div[1]/h1')))
        print(title.text)
        
        # Kembali ke halaman sebelumnya
        driver.back()
    
    time.sleep(10)
    driver.quit()

# Contoh penggunaan
search_and_open_w3schools_article("gamingdistributorid")
