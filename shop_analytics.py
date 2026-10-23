inventory = {"ლეპტოპი":{"price": 2500, "stock": 30},
             "მონიტორი":{"price": 500, "stock": 20},
             "კლავიატურა":{"price": 100, "stock": 50},
             "მაუსი":{"price": 50, "stock": 100}}
product_name = input("შეიყვანეთ პროდუქტის სახელი: ")
product_price = int(input("შეიყვანეთ პროდუქტის ფასი: "))
product_stock = int(input("შეიყვანეთ პროდუქტის რაოდენობა: "))
inventory[product_name] = {"price": product_price, "stock": product_stock}
active_users = {"elene,elena4@gmail.com","sandro,sandro123@gmail.com","maxime,maxime@gmail.com"}
vip_users = {"alex,alex234@gmail.com","nino,nino32@gmail.com","elene,elena4@gmail.com"}
all_users = active_users| vip_users
vip_active_users = active_users & vip_users
regular_users = active_users - vip_users
print("ყველა მომხმარებელი:", all_users)
print("აქტიური VIP მომხმარებლები:", vip_active_users)
print("რეგულარული მომხმარებლები:", regular_users)
for product_name,info in inventory.items():
    if info ["stock"] > 0:
        print("პროდუქტი:", product_name,"ფასი:", info["price"], "რაოდენობა:", info["stock"])
        most_expensive_product = max(inventory.items(), key=lambda x: x[1]["price"])
print("ყველაზე ძვირადღირებული პროდუქტი:", most_expensive_product[0])