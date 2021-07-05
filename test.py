import  unittest
import requests

def add_two_numbers(a,b):
    return a+b

class api_test(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"
    def test1_add_product(self):
        response = requests.post(self.URL+"product", json={"name":"Product6","description":"DESCRIPTION6", "price":30, "quantity":40})
        self.assertEqual(response.status_code, 200)

    def test2_get_all_products(self):
        response = requests.get(self.URL+'all_products')
        self.assertEqual(response.status_code, 200)

    def test3_get_product_with_id(self):
        response = requests.get(self.URL+"product/1")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(),{"id":1,"name":"Product6","description":"DESCRIPTION6", "price":30, "quantity":40})
    
    def test4_update_product(self):
        response = requests.put(self.URL+"product/2", json={"name":"Product6","description":"DESCRIPTION6", "price":90, "quantity":20})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {"id":2,"name":"Product6","description":"DESCRIPTION6", "price":90, "quantity":20})