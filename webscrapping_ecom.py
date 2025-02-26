from bs4 import BeautifulSoup
import requests 


url = "https://www.nike.com/in/t/zoom-vomero-5-shoes-MLm317/HV6417-001"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
# all_classes = soup.find_all(class_=True)
# print(all_classes)

# grid_item_class = soup.find(class_="grid-item")
# print("grid item class",grid_item_class)


nike_shop_id = soup.find(id='nike-shop-root')
print(nike_shop_id)