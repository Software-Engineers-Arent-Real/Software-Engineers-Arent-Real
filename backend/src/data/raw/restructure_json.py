import json

jsonPath = "/Users/armaancheema/Documents/GitHub/Software-Engineers-Arent-Real/backend/src/data/raw/deliveries.json"
resturants = {}
items = {}
customer = {}
delivery = {}
orders = {}

with open(jsonPath, "r") as file:
    allEntries = json.load(file)

for entry in allEntries:

    #---------- resturants grouping ----------
    restaurantId = entry["restaurant_id"]
    if restaurantId not in resturants:
        resturants[restaurantId] = {
            "items":[],
            "orders":[],
            "ratings":[]
        }
    
    foodItem = entry["food_item"]
    if foodItem not in resturants[restaurantId]["items"]:
        resturants[restaurantId]["items"].append(entry["food_item"])
    
    resturants[restaurantId]["orders"].append(entry["order_id"])
    resturants[restaurantId]["ratings"].append(entry["customer_rating"])

    #---------- items grouping ----------
    foodItem = entry["food_item"]
    restaurantId = entry["restaurant_id"]
    itemKey = f"{foodItem}_{restaurantId}"

    if itemKey not in items:
        items[itemKey] = {
            "food_item": entry["food_item"],
            "restaurant_id": entry["restaurant_id"],
            "orders":[],
            "ratings":[]
        }
    
    items[itemKey]["orders"].append(entry["order_id"])
    items[itemKey]["ratings"].append(entry["customer_rating"])

    #---------- orders grouping ----------
    orderId = entry["order_id"]
    if orderId not in orders:
        orders[orderId] = {
            "order_time": entry["order_time"],
            "delivery_time": entry["delivery_time"],
            "delivery_distance": entry["delivery_distance"],
            "order_value": entry.get("order_value"),
            "traffic_condition": entry["traffic_condition"],
            "weather_condition": entry["weather_condition"],
            "delivery_time_actual": entry["delivery_time_actual"],
            "delivery_delay": entry["delivery_delay"],
            "route_taken": entry["route_taken"],
            "customer_id": entry["customer_id"],
            "customer_rating": entry["customer_rating"],
            "food_temperature": entry["food_temperature"],
            "food_freshness": entry["food_freshness"],
            "packaging_quality": entry["packaging_quality"],
            "food_condition": entry["food_condition"],
            "customer_satisfaction": entry["customer_satisfaction"],
            "small_route": entry["small_route"],
            "bike_friendly_route": entry["bike_friendly_route"],
            "route_type": entry["route_type"],
            "route_efficiency": entry["route_efficiency"],
            "predicted_delivery_mode": entry["predicted_delivery_mode"],
            "traffic_avoidance": entry["traffic_avoidance"],
        }

    #---------- customer grouping ----------
    customerId = entry["customer_id"]
    if customerId not in customer:
        customer[customerId] = {
            "age": entry["age"],
            "gender": entry["gender"],
            "location": entry["location"],
            "order_history": entry["order_history"],
            "preferred_cuisine": entry["preferred_cuisine"],
            "order_frequency": entry["order_frequency"],
            "loyalty_program": entry["loyalty_program"],
            "orders":[],
            "ratings":[],
        }
    
    customer[customerId]["orders"].append(entry["order_id"])

    #---------- delivery grouping ----------
    deliveryMethod = entry["delivery_method"]
    if deliveryMethod not in delivery:
        delivery[deliveryMethod] = {
            "restaurant_ids":[],
            "orders":[],
        }
    
    if entry["restaurant_id"] not in delivery[deliveryMethod]["restaurant_ids"]:
        delivery[deliveryMethod]["restaurant_ids"].append(entry["restaurant_id"])
    
    delivery[deliveryMethod]["orders"].append(entry["order_id"])


#---------- create new json files ----------

resturantsPath = "/Users/armaancheema/Documents/GitHub/Software-Engineers-Arent-Real/backend/src/data/resturants.json"
with open(resturantsPath, "w", encoding="utf-8") as file:
    json.dump(resturants, file, indent = 1)

itemsPath = "/Users/armaancheema/Documents/GitHub/Software-Engineers-Arent-Real/backend/src/data/items.json"
with open(itemsPath, "w", encoding="utf-8") as file:
    json.dump(items, file, indent = 1)

ordersPath = "/Users/armaancheema/Documents/GitHub/Software-Engineers-Arent-Real/backend/src/data/orders.json"
with open(ordersPath, "w", encoding="utf-8") as file:
    json.dump(orders, file, indent = 1)

usersPath = "/Users/armaancheema/Documents/GitHub/Software-Engineers-Arent-Real/backend/src/data/users.json"
with open(usersPath, "w", encoding="utf-8") as file:
    json.dump(customer, file, indent = 1)

deliveryPath = "/Users/armaancheema/Documents/GitHub/Software-Engineers-Arent-Real/backend/src/data/delivery.json"
with open(deliveryPath, "w", encoding="utf-8") as file:
    json.dump(delivery, file, indent = 1)