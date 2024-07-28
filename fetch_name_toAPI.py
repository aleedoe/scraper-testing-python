from urllib.parse import urlparse

def extract_shop_and_product(url):
    # Parsing URL
    parsed_url = urlparse(url)
    
    # Mengambil path dan memecahnya berdasarkan '/'
    path_parts = parsed_url.path.split('/')
    
    # Mendapatkan shop_domain dan product_key
    if len(path_parts) > 2:
        shop_domain = path_parts[1]
        product_key = path_parts[2]
    else:
        shop_domain = ''
        product_key = ''
    
    return {
        'shop_domain': shop_domain,
        'product_key': product_key
    }

# Contoh penggunaan
dataku_1 = 'https://www.tokopedia.com/gateway/msi-summit-e16-ai-studio-touch-ultra-7-155h-rtx4050-6gb-16gb-1tb-w11-ohs-16-qhd-165hz-100-dcip3-non-bundle-4d23f?extParam=src%3Dshop%26whid%3D112155'
dataku_2 = 'https://www.tokopedia.com/liger-official/tripod-l-3121-plus-ring-light-46cm-tripod-stand-phone-holder?extParam=src%3Dshop%26whid%3D81897'

print(extract_shop_and_product(dataku_1))
print(extract_shop_and_product(dataku_2))
