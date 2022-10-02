
import requests

cookies = "_gcl_au=1.1.245543386.1656305748; _fbp=fb.1.1656305748011.580276669; _pin_unauth=dWlkPVpqSmpNbVJoTnpNdE5qa3lNQzAwTmprMkxXSXpaREF0TWpKbE1UZGtZamRrTm1WbQ; ajs_anonymous_id=aa37801f-fdb8-45f8-a717-bcea4019da88; ajs_anonymous_id=aa37801f-fdb8-45f8-a717-bcea4019da88; _pin_unauth=dWlkPVpqSmpNbVJoTnpNdE5qa3lNQzAwTmprMkxXSXpaREF0TWpKbE1UZGtZamRrTm1WbQ; __stripe_mid=ceba4184-f9d0-482a-8ad3-60c4b4413e2fbac6f5; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; AMCV_68B620B35350F1650A490D45%40AdobeOrg=1176715910%7CMCIDTS%7C19258%7CMCMID%7C15085762764880023844196951047668360211%7CMCAAMLH-1664452799%7C12%7CMCAAMB-1664452799%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1663855199s%7CNONE%7CMCCIDH%7C0%7CvVersion%7C5.4.0; wfm.tracking.sessionStart=1663847999720; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiYxNTA4NTc2Mjc2NDg4MDAyMzg0NDE5Njk1MTA0NzY2ODM2MDIxMVIPCI7VnqmaMBgBKgRJTkQx8AHz28aotjA=; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; wfmStoreId=16; at_check=true; s_loginSuccess=0; s_cc=true; dotcomSearchId=67875d72-fdc1-4622-8030-39efdaaaede3; session-prd-weg=.eJwtjslugzAARP_F56gKpqSCWwpNZVRAaVl7Qdhxgo1jFrNX_feitoe5PM0bzRfIrx1VJbCuhVB0B_KGdvdCUtkDq--GjSiqFKtl3tcVlcACdHFL_EpYwFwUrUjzmWs-bFAjMF62rASKEQuz-bTRIQjPcxCi1eOV8Wb_dVIoKsTr5ZevEfScSqH7qcKJGC6pL8i_i2WssD2xLDFGLEWP9XhFvNkTGYttq8nSMwv4C_S59-g7t8lztiN-I-bs6eSWKnnXiZj4nJvoOD-7Y3dsp-jWFtrohR8-bzOwA4OiXc4uwIIm1HXjsDe_fwBzx14e.Fg3fzA.0PG6boaY8su5cmOwVho6q-J9_TM; wfm.tracking.x2p=1; _uetsid=15eb60603a6e11edabe83fb0f13adc7e; _uetvid=69815f00f5d511ec823d855b9b8dd9fa; __stripe_sid=3cb2b11b-b41e-4c7d-81e9-6b858cef6cd9878dc9; wegmans.chatbot.closed=1; gpv_pn=Search%20Results%3A%20cakes%20%7C%20Wegmans; s_ips=625; mbox=PC#0531dfe2f49c473c88d26ef46c85a17d.31_0#1727092825|session#64c530c4f3034db88c496516d85dae4f#1663849885; s_tp=7995; s_ppv=Search%2520Results%253A%2520cakes%2520%257C%2520Wegmans%2C13%2C8%2C1053%2C6%2C53; s_sq=wegmansglobalprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DSearch%252520Results%25253A%252520cakes%252520%25257C%252520Wegmans%2526link%253DWegmans%252520Mini%252520Ultimate%252520Chocolate%252520Cake%252520with%252520Chocolate%252520Icing%2526region%253Dcontent%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DSearch%252520Results%25253A%252520cakes%252520%25257C%252520Wegmans%2526pidt%253D1%2526oid%253Dfunctionzr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT"
headers = {'Accept-Language': "en-US,en;q=0.9",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
           'cookie': cookies}

with open("keyword.txt") as f:
    keywords = f.readlines()

for keyword in keywords:
    try:
        API_Link = "https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=false&allow_autocorrect=true&limit=1&offset=0&search_is_autocomplete=false&search_provider=ic&search_term=" + \
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