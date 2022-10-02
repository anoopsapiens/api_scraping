import requests
cookies = '_gcl_au=1.1.1761880801.1662127441; _fbp=fb.1.1662127445336.198864170; BVBRANDID=4982d711-709a-442f-acea-bd18df9b8bd0; _pin_unauth=dWlkPU1EaGhOakkxTURNdE0yVXpNaTAwTVRJeExXRXlZMkV0T0dFM01EQTNNbUV5TURjeg; ajs_anonymous_id=0b3fc69d-f628-4bcb-9670-641d72ea7d8b; _pin_unauth=dWlkPU1EaGhOakkxTURNdE0yVXpNaTAwTVRJeExXRXlZMkV0T0dFM01EQTNNbUV5TURjeg; __stripe_mid=cec5f183-e70a-4d46-a472-d8d32a4e8aff6753fd; ajs_anonymous_id=0b3fc69d-f628-4bcb-9670-641d72ea7d8b; _gid=GA1.2.756828664.1663880396; _uetsid=83f7db603ab911ed87d0a3ebaf981ea4; _uetvid=1a4402502ac811ed82df57cd3d52c45d; _derived_epik=dj0yJnU9Rm1jN0cxQW5pbDlfQlJwaF8zRUNodTR5TTFsMFF2amombj1HaGxVdnV2cGtGbTV4YS0xWVpkb3ZRJm09MSZ0PUFBQUFBR01zek0wJnJtPTEmcnQ9QUFBQUFHTXN6TTA; dotcomSearchId=08da2d13-2192-4a2c-b0c0-5eb08a78aa73; ab.storage.deviceId.aeab3310-682f-4e08-9c9d-07d176b1452b={"g":"6986dca4-8580-0ea4-ae05-a68490f57376","c":1663880644625,"l":1663919777164}; ab.storage.sessionId.aeab3310-682f-4e08-9c9d-07d176b1452b={"g":"2e2b47a1-a79f-304e-9720-e83db53a470b","e":1663921644110,"c":1663919777160,"l":1663919844110}; session-sprouts=.eJwtjNFOgzAARf-lz9tCGSDwZticReliRAa8kBU6KJRCKCDr4r9Lorm5Lyfn3gfIbgOVFXBvVy7pBmQ9HdqroGIE7jhMK5FUStaJbOwaKoAL6N2vyClnZ-ajL4UgZr6zWyHM9ei-VuU6nwl3-tRDFj4EJlbBmlK9e39OrPMG1d2Cw9IIVLJg9SxR-9KQC5-KGPP8f0tEJIn3zZKLORPBR7KPFKp7LRcRX7_6JP5g5_qo4xotQZ1r-JA6uxqeKmJ8Xtp528Jwse1ytF_frMJSmEEeHkN_iy2UGClrwAZMkg4ZK4ALTdveW_BJ-_kFX8FcuQ.Fg-JbA.azcOzYhfeDHh3Z49LQ34cfeAOYY; _ga_LPZ816BHL5=GS1.1.1663956965.12.1.1663956973.52.0.0; _ga=GA1.2.20930352.1662127444; _gat_UA-47434162-1=1; BVBRANDSID=6699b7dc-9bc2-4313-96c1-d1429096d420; _derived_epik=dj0yJnU9UlNuWnVidVNFaGJLS2U4Tm9sUGhjb1JtbGtuMTNWMWkmbj03OFJFeHZsbHhyLTZkcWl1TEc5NUlRJm09MSZ0PUFBQUFBR010OV9NJnJtPTEmcnQ9QUFBQUFHTXQ5X00; _dd_s=rum=1&id=c7b23c2a-a9c1-4b95-a894-7e7e8bf8de77&created=1663956951811&expire=1663957881963'
headers = {
    'Accept-Language': "en-US,en;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    'cookie': cookies
    }

with open("keywords.txt") as f:
    keywords = f.readlines()

for keyword in keywords:
    keyword=keyword.rstrip('\n').split(',')[0]    
    try:
        API_Link = 'https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_is_autocomplete=false&search_provider=buffet&search_term='+keyword+'&secondary_results=false&sort=rank&unified_search_shadow_test_enabled=false'
        keyword.replace(
            ' ', '+')+"&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"
        response = requests.get(API_Link, headers=headers)
        data = response.json()
        # keyword,vendor name,name,brand,price,quantity,availability_status,categories
        items = keyword
        if data['items']:
            print(data)
        else:
            print("no results found")
    except:
        print("API Error (change cookies or check api link)")