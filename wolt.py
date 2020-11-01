import requests

class Wolt:
	def __init__(self):self.__wolt_api_url='https://restaurant-api.wolt.com'
	def serach_restaurant(self,name,lat=None,lon=None,limit=50):
		if lat and lon:__request__=requests.get(f"{self.__wolt_api_url}/v1/search?q={name}&lat={lat}&lon={lon}&limit={limit}")
		else:__request__=requests.get(f"{self.__wolt_api_url}/v1/search?q={name}&limit={limit}")
		if __request__.status_code==200:return __request__.json().get('results')
		return None
	def get_restaurant_menu(self,oid):
		__request__=requests.get(f"{self.__wolt_api_url}/v3/menus/{oid}")
		if __request__.status_code==200:return __request__.json().get('results')