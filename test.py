import requests

BASE = "http://127.0.0.1:5000/"

# sku_search, availability, sold_out

# response = requests.get(BASE + "products/" + "sku_search/" +"746607") # enter sku 746607
# print (response.text)

response = requests.put(BASE + "products/" + "sku_search/" +"746607")

# response = requests.get(BASE + "availability/")
# print (response.text)