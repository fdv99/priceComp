from selenium import webdriver
"""Video Tutorial Link:
https://www.youtube.com/watch?v=rajXpxvHiV0
"""

web = webdriver.Chrome('support files/chromedriver.exe')

myupc = '65s421'
url_homedepot = 'https://homedepot.com/s/%2522'+myupc+'%2522?NCNI-5'
"""
web.get(url_homedepot)

title_homedepot = web.find_element_by_class_name('product-details__title').text
price_homedepot = web.find_element_by_class_name('price').text[:-2]+'.'+web.find_element_by_class_name('price').text[-2:]

print(myupc)
print(title_homedepot)
print(price_homedepot)
"""

url_walmart = 'https://www.walmart.com/search/?cat_id=0&query=%22'+myupc+'%22'
web.get(url_walmart)

title_walmart = web.find_element_by_class_name('product-title-link').text
price_walmart = web.find_element_by_class_name('price').text 

print(title_walmart)
print(price_walmart)