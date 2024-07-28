from urllib.parse import urlparse

def extract_product_path(url):
    # Parsing URL
    parsed_url = urlparse(url)
    
    # Mengambil path dan memecahnya berdasarkan '/'
    path_parts = parsed_url.path.split('/')
    
    # Bagian terakhir dari path
    product_part = path_parts[-1]
    
    return product_part

# Contoh penggunaan
dataku_1 = 'https://www.tokopedia.com/gateway/msi-summit-e16-ai-studio-touch-ultra-7-155h-rtx4050-6gb-16gb-1tb-w11-ohs-16-qhd-165hz-100-dcip3-non-bundle-4d23f?extParam=src%3Dshop%26whid%3D112155'
dataku_2 = 'https://www.tokopedia.com/liger-official/tripod-l-3121-plus-ring-light-46cm-tripod-stand-phone-holder?extParam=src%3Dshop%26whid%3D81897'

print(extract_product_path(dataku_1))
print("===========")
print(extract_product_path(dataku_2))
