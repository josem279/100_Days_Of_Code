import requests
from bs4 import BeautifulSoup
import smtplib

target_price = 100
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url="https://appbrewery.github.io/instant_pot/", headers=header)
instant_pot_website = response.text

soup = BeautifulSoup(instant_pot_website, "html.parser")
price = int(soup.find(class_="a-price-whole").text.split(".")[0])
title = soup.find(id="productTitle").get_text().strip()

if price < target_price:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

print(price)