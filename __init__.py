import requests

class Wolt:
    def __init__(self):
        self.__wolt_api_url = "https://restaurant-api.wolt.com"
    
    def serach_restaurant(self,name,lat=None,lon=None,limit=50):
        if lat and lon:
            __request__ = requests.get(f"{self.__wolt_api_url}/v1/search?q={name}&lat={lat}&lon={lon}&limit={limit}")
        else:
            __request__ = requests.get(f"{self.__wolt_api_url}/v1/search?q={name}&limit={limit}")

        if __request__.status_code == 200:
            return __request__.json().get("results")
        
        return None

    def get_restaurant_menu(self,oid):
        __request__ = requests.get(f"{self.__wolt_api_url}/v3/menus/{oid}")

        if __request__.status_code == 200:
            return __request__.json().get("results")



class Wolt_Resterant:
    def __init__(self, oid, name):
        pass


class Wolt_Categorie:
    def __init__(self, __data__):
        self.o_id = __data__["_id"]['$oid']
        self.name = __data__['name'][0]['value']
        self.description =  __data__['description']

class Wolt_Meals:
    def __init__(self,__data__):
        self.o_id = __data__['_id']['$oid']
        self.alcohol_percentage = __data__['alcohol_percentage']
        self.allowed_delivery_methods = __data__['allowed_delivery_methods']
        self.baseprice = __data__['baseprice']
        self.image = __data__['image']
        self.name = __data__['name'][0]['value']

# exmpales
w = Wolt()

print(w.serach_restaurant("browny")[0]['value']['active_menu']['$oid'])
w.get_restaurant_menu("5cc5c17234c930d97e0b3245")