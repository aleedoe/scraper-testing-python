from seleniumwire import webdriver  # Import from seleniumwire
from seleniumwire.utils import decode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get('https://www.tokopedia.com/temptacionid/temptacion-arrogant-edp-30ml-unisex?extParam=src%3Dshop%26whid%3D14303043')

# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        if "PDPGetLayoutQuery" in request.url:
            
            response = request.response
            body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
            body_content = body.decode('utf-8')
            print(body_content)