from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=D:\Programs\chrome-profile")
chrome_options.add_argument("--proxy-server=http://127.0.0.1:8080")

# Inisialisasi driver
driver = webdriver.Chrome(options=chrome_options)

# Navigasi ke halaman pengaturan sertifikat
driver.get("chrome://settings/certificates")

# Instruksi manual: Klik "Authorities" -> "Import" -> Pilih mitmproxy-ca-cert.crt dan aktifkan kepercayaan untuk HTTPS
