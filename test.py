import requests
#base url
BASE ="http://127.0.0.1:5000/"


# comment out the test case if its not necessary

#Create
# response = requests.post(BASE+"product", json={"name":"Product6","description":"DESCRIPTION6", "price":30, "quantity":40})
# print(response.json())
# print()


#Read all
response = requests.get(BASE+"product")
print(response.json())
# print()

# Read one
# response = requests.get(BASE+"product/5")
# print(response.json())


# #Update
# response = requests.put(BASE+"product/5",json={"name":"Product6","description":"DESCRIPTION6", "price":800, "quantity":20})
# print(response.json())


# #Delete
# response = requests.delete(BASE+'product/5')
# print(response.json())