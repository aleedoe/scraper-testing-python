from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_and_open_w3schools_article(keyword):
    # Path ke ChromeDriver Anda
    chrome_driver_path = "D:\Programs\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    # Mengatur opsi untuk Chrome
    chrome_options = Options()

    # Membuat service object
    service = Service(chrome_driver_path)

    # Membuka browser
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Buka Google
        driver.get("https://www.google.com")

        # Cari kotak pencarian
        search_box = driver.find_element(By.NAME, 'q')
        
        # Masukkan kata kunci dan tekan Enter
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

        # Tunggu hasil pencarian muncul
        wait = WebDriverWait(driver, 5)
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3')))
        print(results)

        # Loop melalui hasil pencarian dan cari yang berasal dari w3schools
        for result in results:
            parent = result.find_element(By.XPATH, './..')
            link = parent.get_attribute('href')
            if 'w3schools.com' in link:
                result.click()
                break
        else:
            print("Tidak ditemukan artikel dari w3schools")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        # Tunggu beberapa detik sebelum menutup browser
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
        driver.quit()

# Contoh penggunaan
search_and_open_w3schools_article("learning python")
