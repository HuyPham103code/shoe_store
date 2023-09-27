
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from item import Item
import csv



#crawl category name 
def get_category_href():
    try:       
        categorys = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR,
         'ul#menu-main-menu > li > a')]
    except NoSuchElementException:
        # handle the case where the element is not found //*[@id="menu-main-menu"]
        print("Element not found")
    return categorys


#read category href
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        category_hrefs = file.readlines()
    category_hrefs = [href.strip() for href in category_hrefs]
    return category_hrefs


#write category href
def write_file(file_name, category_hrefs):
    with open(file_name, 'w', encoding='utf-8') as file:
        for href in category_hrefs:
            file.write(href + '\n')


#get content of one href
def get_content(url):
    driver.get(url)
    part = url.split('/')
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    sleep(10)
    items = []
    li_elements = driver.find_elements(By.CSS_SELECTOR, '#primary > ul > li')
    for li in li_elements:
        category = part[-2]
        img = li.find_element(By.CSS_SELECTOR, 'div.product-header > a > img').get_attribute('data-src')
        title = li.find_element(By.CSS_SELECTOR, 'h3 > a').text
        price = li.find_element(By.CSS_SELECTOR, '.price > span.woocommerce-Price-amount.amount').text
        price = price[:-1]    #remove last character
        items.append(Item(category, img, title, price))
    return items



### write to csv file
def write_to_csv(filename, items):
    headers = ["Category", "Image", "Title", "Price"]
    for item in items:
        print(item.category, item.img, item.title, item.price)
    data = [{'Category': item.category, 'Image': item.img, 'Title': item.title, 'Price': item.price} for item in items]
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)

        # Write the headers as the first row
        csv_writer.writeheader()
        print(1)
        # Write the data rows
        csv_writer.writerows(data)
        print(2)




########start grogramme
driver = webdriver.Chrome()
driver.get('https://giayxshop.vn/')
sleep(3)



# #lấy href theo loại
# categorys = get_category_href()
# sleep(2)
# print(categorys)
# # viết vào file
# write_file('category_hrefs.txt', categorys)


#===========đọc href ra
category_href = read_file('category_hrefs.txt')
print(category_href)
print('done')


#lấy data từ mỗi href
items = []
for href in category_href:
    items.extend(get_content(href))

# for item in items:
#     item.show()
sleep(5)
write_to_csv('data.csv', items)
print('Done')
driver.quit()

#mới lấy được


# ======================= đã lấy được data vào file csv, bây giờ trong ngày hôm nay phải tạo 
# được project django, model và đưa data vào mysql, rồi ngày mai làm render lên web là xong!!! :D

