import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

YOUR_EMAIL = ''
YOUR_PASSWORD = ''

URL = "https://www.amazon.com/Manduka-PRO-Alfombrilla-para-pilates/dp/B0066T7I54/ref=sr_1_2_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=5RD7LVDH2UXW&keywords=MANDUKA+MAT&qid=1676412905&sprefix=mandu%2Caps%2C2026&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSjNROU1JQ0FERzdaJmVuY3J5cHRlZElkPUEwMDA0MTExMjlPRUpSWDExR0dTUyZlbmNyeXB0ZWRBZElkPUEwNzI1MjAxMlBZS0E5STRWOENIQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

page = ''
while page == '':
    try:
        response = requests.get(url=URL, headers=headers)
        break
    except:
        print("Connection refused by the server..")
        print("Sleeping for 5 seconds")
        time.sleep(5)
        continue


soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())

price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(f'Price in USD: {price}')


BUY_PRICE = 150
title = soup.find(id="productTitle").get_text().strip()

if price< BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login()
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )