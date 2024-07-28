import requests
import json

def fetchApiDetailProduct(referer, shop_domain, product_key):

    url = 'https://gql.tokopedia.com/graphql/PDPGetLayoutQuery'
    headers = {
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'X-Version': '4c288b3',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'Referer': referer,
        'X-Source': 'tokopedia-lite',
        'x-device': 'desktop',
        'X-Tkpd-Lite-Service': 'zeus',
        'X-TKPD-AKAMAI': 'pdpGetLayout'
    }

    data = [
        {
            "operationName": "PDPGetLayoutQuery",
            "variables": {
                "shopDomain": shop_domain,
                "productKey": product_key,
                "layoutID": "",
                "apiVersion": 1,
                "tokonow": {
                    "shopID": "11530573",
                    "whID": "12210375",
                    "serviceType": "2h"
                },
                "deviceID": "YzAyNWZkZmM3ODUyMzdiMzAyYzJlMzlhODk5MWI1NWVlNTFmZGE1OTJmNzhhYTYwODk4M2NhMGYwYWY1MmFlNGFiY2UxNzBjN2FmYzU5OTRlYWE1MGM1NmVkNDZjZDhm47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
                "userLocation": {
                    "cityID": "176",
                    "addressID": "0",
                    "districtID": "2274",
                    "postalCode": "",
                    "latlon": ""
                },
                "extParam": "src%3Dshop%26whid%3D112155"
            },
            "query": """
            fragment ProductVariant on pdpDataProductVariant {
            errorCode
            parentID
            defaultChild
            sizeChart
            totalStockFmt
            variants {
                productVariantID
                variantID
                name
                identifier
                option {
                picture {
                    urlOriginal: url
                    urlThumbnail: url100
                    __typename
                }
                productVariantOptionID
                variantUnitValueID
                value
                hex
                stock
                __typename
                }
                __typename
            }
            children {
                productID
                price
                priceFmt
                slashPriceFmt
                discPercentage
                optionID
                optionName
                productName
                productURL
                picture {
                urlOriginal: url
                urlThumbnail: url100
                __typename
                }
                stock {
                stock
                isBuyable
                stockWordingHTML
                minimumOrder
                maximumOrder
                __typename
                }
                isCOD
                isWishlist
                campaignInfo {
                campaignID
                campaignType
                campaignTypeName
                campaignIdentifier
                background
                discountPercentage
                originalPrice
                discountPrice
                stock
                stockSoldPercentage
                startDate
                endDate
                endDateUnix
                appLinks
                isAppsOnly
                isActive
                hideGimmick
                isCheckImei
                minOrder
                __typename
                }
                thematicCampaign {
                additionalInfo
                background
                campaignName
                icon
                __typename
                }
                __typename
            }
            __typename
            }
            
            fragment ProductMedia on pdpDataProductMedia {
            media {
                type
                urlOriginal: URLOriginal
                urlThumbnail: URLThumbnail
                urlMaxRes: URLMaxRes
                videoUrl: videoURLAndroid
                prefix
                suffix
                description
                variantOptionID
                __typename
            }
            videos {
                source
                url
                __typename
            }
            __typename
            }
            
            fragment ProductCategoryCarousel on pdpDataCategoryCarousel {
            linkText
            titleCarousel
            applink
            list {
                categoryID
                icon
                title
                isApplink
                applink
                __typename
            }
            __typename
            }
            
            fragment ProductHighlight on pdpDataProductContent {
            name
            price {
                value
                currency
                priceFmt
                slashPriceFmt
                discPercentage
                __typename
            }
            campaign {
                campaignID
                campaignType
                campaignTypeName
                campaignIdentifier
                background
                percentageAmount
                originalPrice
                discountedPrice
                originalStock
                stock
                stockSoldPercentage
                threshold
                startDate
                endDate
                endDateUnix
                appLinks
                isAppsOnly
                isActive
                hideGimmick
                __typename
            }
            thematicCampaign {
                additionalInfo
                background
                campaignName
                icon
                __typename
            }
            stock {
                useStock
                value
                stockWording
                __typename
            }
            variant {
                isVariant
                parentID
                __typename
            }
            wholesale {
                minQty
                price {
                value
                currency
                __typename
                }
                __typename
            }
            isCashback {
                percentage
                __typename
            }
            isTradeIn
            isOS
            isPowerMerchant
            isWishlist
            isCOD
            preorder {
                duration
                timeUnit
                isActive
                preorderInDays
                __typename
            }
            __typename
            }
            
            fragment ProductCustomInfo on pdpDataCustomInfo {
            icon
            title
            isApplink
            applink
            separator
            description
            __typename
            }
            
            fragment ProductInfo on pdpDataProductInfo {
            row
            content {
                title
                subtitle
                applink
                __typename
            }
            __typename
            }
            
            fragment ProductDetail on pdpDataProductDetail {
            content {
                title
                subtitle
                applink
                showAtFront
                isAnnotation
                __typename
            }
            __typename
            }
            
            fragment ProductDataInfo on pdpDataInfo {
            icon
            title
            isApplink
            applink
            content {
                icon
                text
                __typename
            }
            __typename
            }
            
            fragment ProductSocial on pdpDataSocialProof {
            row
            content {
                icon
                title
                subtitle
                applink
                type
                rating
                __typename
            }
            __typename
            }
            
            fragment ProductDetailMediaComponent on pdpDataProductDetailMediaComponent {
            title
            description
            contentMedia {
                url
                ratio
                type
                __typename
            }
            show
            ctaText
            __typename
            }
            
            query PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation, $extParam: String, $tokonow: pdpTokoNow, $deviceID: String) {
            pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation, extParam: $extParam, tokonow: $tokonow, deviceID: $deviceID) {
                requestID
                name
                pdpSession
                basicInfo {
                alias
                createdAt
                isQA
                id: productID
                shopID
                shopName
                minOrder
                maxOrder
                weight
                weightUnit
                condition
                status
                url
                needPrescription
                catalogID
                isLeasing
                isBlacklisted
                isTokoNow
                menu {
                    id
                    name
                    url
                    __typename
                }
                category {
                    id
                    name
                    title
                    breadcrumbURL
                    isAdult
                    isKyc
                    minAge
                    detail {
                    id
                    name
                    breadcrumbURL
                    isAdult
                    __typename
                    }
                    __typename
                }
                txStats {
                    transactionSuccess
                    transactionReject
                    countSold
                    paymentVerified
                    itemSoldFmt
                    __typename
                }
                stats {
                    countView
                    countReview
                    countTalk
                    rating
                    __typename
                }
                __typename
                }
                components {
                name
                type
                position
                data {
                    ...ProductMedia
                    ...ProductHighlight
                    ...ProductInfo
                    ...ProductDetail
                    ...ProductSocial
                    ...ProductDataInfo
                    ...ProductCustomInfo
                    ...ProductVariant
                    ...ProductCategoryCarousel
                    ...ProductDetailMediaComponent
                    __typename
                }
                __typename
                }
                __typename
            }
            }
            """
        }
    ]

    response = requests.post(url, headers=headers, json=data)
    json_response = response.json()

    try:
        with open('detail-products.json', 'r') as f:
            try:
                data_lama = json.load(f)
            except json.JSONDecodeError:
                # Jika file kosong atau berisi data yang tidak valid, buat list kosong
                data_lama = []
    except FileNotFoundError:
        # Jika file belum ada, buat list kosong
        data_lama = []

    # Gabungkan data lama dan baru
    data_lama.extend(json_response)

    # Tulis kembali data ke file JSON
    with open('detail-products.json', 'w') as f:
        json.dump(data_lama, f, indent=4)
    
    print("Data berhasil ditambahkan ke file detail-products.json")
    
    # return json_response
    
# def tambah_data_ke_json(file_json, data_baru):

#     try:
#         with open(file_json, 'r') as f:
#             try:
#                 data_lama = json.load(f)
#             except json.JSONDecodeError:
#                 # Jika file kosong atau berisi data yang tidak valid, buat list kosong
#                 data_lama = []
#     except FileNotFoundError:
#         # Jika file belum ada, buat list kosong
#         data_lama = []

#     # Gabungkan data lama dan baru
#     data_lama.extend(data_baru)

#     # Tulis kembali data ke file JSON
#     with open(file_json, 'w') as f:
#         json.dump(data_lama, f, indent=4)

# value = json_response

# # Nama file JSON
# file_json = "detail-product.json"

# # Panggil fungsi untuk menambahkan data
# tambah_data_ke_json(file_json, value)

# print("Data berhasil ditambahkan ke file detail-product.json")