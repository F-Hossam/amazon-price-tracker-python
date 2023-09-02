from bs4 import BeautifulSoup
import requests
import smtplib

EMAIL = EMAIL
PASSWORD = PASSWORD

webpage_url = 'https://www.amazon.com/Countertop-Convection-50%C2%B0-500%C2%B0F-Temperature-Adjustments/dp/B00IXBMS6M/ref=sxin_14_pa_sp_search_thematic_sspa?content-id=amzn1.sym.52245a2c-8c16-4000-bf4a-60168de07fe4%3Aamzn1.sym.52245a2c-8c16-4000-bf4a-60168de07fe4&cv_ct_cx=oven&keywords=oven&pd_rd_i=B00IXBMS6M&pd_rd_r=033324b8-f495-4919-a1c8-582b267a9067&pd_rd_w=YAsnE&pd_rd_wg=YJxoX&pf_rd_p=52245a2c-8c16-4000-bf4a-60168de07fe4&pf_rd_r=HM5H34824HW0Y0T50HM9&qid=1693490247&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-1-b6abdd27-62b8-4289-b410-d963a80e3e5e-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1'
response = requests.get(
    url=webpage_url,
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept-Language':'en-US,en;q=0.9,fr;q=0.8',
}
)

#scrape the product page and get its price using beautifulsoup module
amazon_web = BeautifulSoup(response.text, 'html.parser')
price_tag = amazon_web.find(name='span', class_='a-price-whole')
title_tag = amazon_web.find(name='span', id='productTitle')
whole_price = price_tag.get_text()
fraction_price = amazon_web.find(name='span', class_='a-price-fraction').get_text()
price = whole_price + fraction_price
title = title_tag.get_text()
target_price = '130' #this is the price that we want it to exist in order to buy the oven

price_int = int(float(price))
target_price_int = int(target_price)

#send email if the oven price is below target_price
if (price_int <= target_price_int):
    message = f'{title} is now ${price}\n{webpage_url}'

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL, 
            msg=f'Subject:Amazon Price Alert\n\n{message}'.encode('utf-8')
        )

