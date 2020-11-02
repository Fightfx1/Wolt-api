from Wolt_api import Wolt

wolt = Wolt()

# find restaurant by her name returning json object
wolt.serach_restaurant("put here name") # there is option to enter location

# find restaurant menu by her oid (wold id) the search return wolt rest obeject 
wolt.get_restaurant_menu("oid")  # the oid can be find at the last function u can find him;
