import requests
cookies = '_gcl_au=1.1.1761880801.1662127441; _fbp=fb.1.1662127445336.198864170; BVBRANDID=4982d711-709a-442f-acea-bd18df9b8bd0; _pin_unauth=dWlkPU1EaGhOakkxTURNdE0yVXpNaTAwTVRJeExXRXlZMkV0T0dFM01EQTNNbUV5TURjeg; ajs_anonymous_id=0b3fc69d-f628-4bcb-9670-641d72ea7d8b; _pin_unauth=dWlkPU1EaGhOakkxTURNdE0yVXpNaTAwTVRJeExXRXlZMkV0T0dFM01EQTNNbUV5TURjeg; __stripe_mid=cec5f183-e70a-4d46-a472-d8d32a4e8aff6753fd; ajs_anonymous_id=0b3fc69d-f628-4bcb-9670-641d72ea7d8b; _gid=GA1.2.1374089064.1664525121; _uetsid=157691f041a911edbbdf5b7ae63c1ef1; _uetvid=1a4402502ac811ed82df57cd3d52c45d; BVBRANDSID=9a5bdc65-6045-4127-982a-cf3577a6c3b0; _derived_epik=dj0yJnU9ZFBWSmlGM0pEblZNVWRqQ29WU2tORm5TU21nYW92MC0mbj1xTnVCT1hfVGR1NkVOVU9iTi00ZHpnJm09MSZ0PUFBQUFBR001bC1VJnJtPTEmcnQ9QUFBQUFHTTVsLVU; dotcomSearchId=93c244b7-92c5-40fd-b96b-d62cbb380bec; ab.storage.sessionId.aeab3310-682f-4e08-9c9d-07d176b1452b={"g":"3f72b2ca-12bf-392d-deb1-2b8c9e6afac8","e":1664720662793,"c":1664718862795,"l":1664718862795}; ab.storage.deviceId.aeab3310-682f-4e08-9c9d-07d176b1452b={"g":"6986dca4-8580-0ea4-ae05-a68490f57376","c":1663880644625,"l":1664718862800}; session-sprouts=.eJwtjFtvgjAARv9Ln43hpghvCroURw0bcnshtJZZqIVQcIDZfx_J9nBeTs73vUBedlTegV0WXNIVyFvaPQpBRQ_svhsWI6mUrBF539RUABvQybvjN8IuzIPXGaqIedZ6kSrRomlhJhp_Ym61mQO3yA0mP_Q13yXGu_PXJBqvYdWMKPwy_Dkd0byX8HGqccyHW4I4-d9iEUnsfLM03jyx4D3WoxlWrUJExJevNk0CdqmOGqrg6FdEQW5mrU96Uh1bRM_XNFRdoeh4bEzmF_vD2YknhX3sM6M0yedhCsAKDJJ2ObsBW93sdvpWNZWfX_QxXDU.FhsqYg.vVWS3bthh4iH97HCW8tp5z2DaTU; _derived_epik=dj0yJnU9akNTcWFGVmFra2UyQ2o1ZUhySHlHQ2J2alhIRGhJSkcmbj1QM3pvR0VUU01NSXhscmFkRFlzaEhBJm09MSZ0PUFBQUFBR001bU9NJnJtPTEmcnQ9QUFBQUFHTTVtT00; __stripe_sid=f7161855-c557-43ba-b567-50e98f9cf8cf574909; _ga=GA1.2.20930352.1662127444; _dd_s=rum=1&id=b25b47ad-1e1b-4ff2-80d3-774e49bdd179&created=1664718835677&expire=1664720552069; _gat_UA-47434162-1=1; _ga_LPZ816BHL5=GS1.1.1664718821.27.1.1664719653.60.0.0'
headers = {
    'Accept-Language': "en-US,en;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    'cookie': cookies
    }

with open("keyword.txt") as f:
    keywords = f.readlines()

for keyword in keywords:
    try:
        API_Link = 'https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_is_autocomplete=true&search_provider=buffet&search_term='+keyword.replace(' ','+')+'&secondary_results=false&sort=rank&unified_search_shadow_test_enabled=false'
        response = requests.get(API_Link, headers=headers)
        print(API_Link)
        # print(response.status_code)
        data = response.json()
        if int(data['item_count'])!=0:
            for i in range(int(data['item_count'])):
                print(data['items'][i]['name'])
        else:
            print("no results found")
    except:
        print("API Error (change cookies or check api link)")